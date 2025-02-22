import asyncio
import atexit
import base64
import hashlib
import json
import os
import tempfile
import uuid
from dataclasses import asdict, dataclass, field
from io import BytesIO
from typing import TYPE_CHECKING, List, Optional

from datasets.utils.logging import disable_progress_bar
from huggingface_hub import CommitScheduler, login, metadata_update, whoami
from PIL import Image

from observers.stores.base import Store

if TYPE_CHECKING:
    from observers.base import Record


disable_progress_bar()


@dataclass
class DatasetsStore(Store):
    """
    Datasets store
    """

    org_name: Optional[str] = field(default=None)
    repo_name: Optional[str] = field(default=None)
    folder_path: Optional[str] = field(default=None)
    every: Optional[int] = field(default=5)
    path_in_repo: Optional[str] = field(default=None)
    revision: Optional[str] = field(default=None)
    private: Optional[bool] = field(default=None)
    token: Optional[str] = field(default=None)
    allow_patterns: Optional[List[str]] = field(default=None)
    ignore_patterns: Optional[List[str]] = field(default=None)
    squash_history: Optional[bool] = field(default=None)

    _filename: Optional[str] = field(default=None)
    _scheduler: Optional[CommitScheduler] = None
    _temp_dir: Optional[str] = field(default=None, init=False)

    def __post_init__(self):
        """Initialize the store and create temporary directory"""
        if self.ignore_patterns is None:
            self.ignore_patterns = ["*.json"]

        try:
            whoami(token=self.token or os.getenv("HF_TOKEN"))
        except Exception:
            login()

        if self.folder_path is None:
            self._temp_dir = tempfile.mkdtemp(prefix="observers_dataset_")
            self.folder_path = self._temp_dir
            atexit.register(self._cleanup)
        else:
            os.makedirs(self.folder_path, exist_ok=True)

    def _cleanup(self):
        """Clean up temporary directory on exit"""
        if self._temp_dir and os.path.exists(self._temp_dir):
            import shutil

            shutil.rmtree(self._temp_dir)

    def _init_table(self, record: "Record"):
        import logging

        logging.getLogger("huggingface_hub").setLevel(logging.ERROR)

        repo_name = self.repo_name or f"{record.table_name}_{uuid.uuid4().hex[:8]}"
        org_name = self.org_name or whoami(token=self.token).get("name")
        repo_id = f"{org_name}/{repo_name}"
        self._filename = f"{record.table_name}_{uuid.uuid4()}.json"
        self._scheduler = CommitScheduler(
            repo_id=repo_id,
            folder_path=self.folder_path,
            every=self.every,
            path_in_repo=self.path_in_repo,
            repo_type="dataset",
            revision=self.revision,
            private=self.private,
            token=self.token,
            allow_patterns=self.allow_patterns,
            ignore_patterns=self.ignore_patterns,
            squash_history=self.squash_history,
        )
        self._scheduler.private = self.private
        metadata_update(
            repo_id=repo_id,
            metadata={"tags": ["observers", record.table_name.split("_")[0]]},
            repo_type="dataset",
            token=self.token,
            overwrite=True,
        )

    @classmethod
    def connect(
        cls,
        org_name: Optional[str] = None,
        repo_name: Optional[str] = None,
        folder_path: Optional[str] = None,
        every: Optional[int] = 5,
        path_in_repo: Optional[str] = None,
        revision: Optional[str] = None,
        private: Optional[bool] = None,
        token: Optional[str] = None,
        allow_patterns: Optional[List[str]] = None,
        ignore_patterns: Optional[List[str]] = None,
        squash_history: Optional[bool] = None,
    ) -> "DatasetsStore":
        """Create a new store instance with optional custom path"""
        return cls(
            org_name=org_name,
            repo_name=repo_name,
            folder_path=folder_path,
            every=every,
            path_in_repo=path_in_repo,
            revision=revision,
            private=private,
            token=token,
            allow_patterns=allow_patterns,
            ignore_patterns=ignore_patterns,
            squash_history=squash_history,
        )

    def add(self, record: "Record"):
        """Add a new record to the database"""
        if not self._scheduler:
            self._init_table(record)

        with self._scheduler.lock:
            with (self._scheduler.folder_path / self._filename).open("a") as f:
                record_dict = asdict(record)

                # Handle JSON fields
                for json_field in record.json_fields:
                    if record_dict[json_field]:
                        record_dict[json_field] = json.dumps(record_dict[json_field])

                # Handle image fields
                for image_field in record.image_fields:
                    if record_dict[image_field]:
                        image_folder = self._scheduler.folder_path / "images"
                        image_folder.mkdir(exist_ok=True)

                        # Generate unique filename based on record content
                        filtered_dict = {
                            k: v
                            for k, v in sorted(record_dict.items())
                            if k not in ["uri", image_field, "id"]
                        }
                        content_hash = hashlib.sha256(
                            json.dumps(obj=filtered_dict, sort_keys=True).encode()
                        ).hexdigest()
                        image_path = image_folder / f"{content_hash}.png"

                        # Save image and update record
                        image_bytes = base64.b64decode(
                            record_dict[image_field]["bytes"]
                        )
                        Image.open(BytesIO(image_bytes)).save(image_path)
                        record_dict[image_field].update(
                            {"path": str(image_path), "bytes": None}
                        )

                # Clean up empty dictionaries
                record_dict = {
                    k: None if v == {} else v for k, v in record_dict.items()
                }
                sorted_dict = {
                    col: record_dict.get(col) for col in record.table_columns
                }
                try:
                    f.write(json.dumps(sorted_dict) + "\n")
                    f.flush()
                except Exception:
                    raise

    async def add_async(self, record: "Record"):
        """Add a new record to the database asynchronously"""
        await asyncio.to_thread(self.add, record)

    async def close_async(self):
        """Close the dataset store asynchronously"""
        if self._scheduler:
            await asyncio.to_thread(self._scheduler.__exit__, None, None, None)
            self._scheduler = None

    def close(self):
        """Close the dataset store synchronously"""
        if self._scheduler:
            self._scheduler.__exit__(None, None, None)
            self._scheduler = None

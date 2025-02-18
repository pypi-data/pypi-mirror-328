import os

from pydantic_settings import BaseSettings, SettingsConfigDict

FILE_FORMAT = os.environ.get("SPIRAL_FILE_FORMAT", "parquet")


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        env_prefix="SPIRAL_CORE__",
        frozen=True,
    )

    partition_file_min_size: int = 256 * 1024 * 1024  # 256MB
    flush_wal_on_write: bool = False

    # TODO(marko): Support config. Unused after migration to Rust.
    # #: Defaults to ThreadPoolExecutor's default (based on os.cpu_count().
    # scan_num_threads: int | None = 61  # 61 is used by Golang and Tokio, for some reason...
    #
    # #: The duration of WAL that is preserved to allow for txn conflict resolution.
    # transaction_window: int = 0 if DEV else timedelta(days=1).total_seconds()
    #
    # #: Truncation length of string statistics.
    # string_truncation_length: int = 1024

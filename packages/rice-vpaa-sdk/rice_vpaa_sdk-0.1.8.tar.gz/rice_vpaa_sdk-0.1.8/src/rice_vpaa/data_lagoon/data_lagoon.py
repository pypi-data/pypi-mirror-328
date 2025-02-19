import os
import tempfile
import boto3
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
import duckdb
from typing import Optional, Dict, Any, List

class _S3Connector:
    def __init__(self):
        self.client = boto3.client(
            's3',
            endpoint_url=f"{self.endpoint}",
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            region_name=self.region
        )
        super().__init__()

    def list_files(self, path: str) -> List[str]:
        response = self.client.list_objects_v2(Bucket=self.bucket, Prefix=path)
        files = [obj['Key'] for obj in response.get('Contents', [])]
        return files

    def write_parquet(self, df: pd.DataFrame, path: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        arrow_table = pa.Table.from_pandas(df)
        s3_metadata = {k: str(v) for k, v in (metadata or {}).items()}
        
        with tempfile.NamedTemporaryFile(suffix=".parquet", delete=False) as tmp:
            try:
                pq.write_table(arrow_table, tmp.name)
                tmp.close()
                self.client.upload_file(
                    tmp.name, 
                    self.bucket, 
                    path, 
                    ExtraArgs={"Metadata": s3_metadata}
                )
            finally:
                if os.path.exists(tmp.name):
                    os.unlink(tmp.name)

    def get_metadata(self, path: str) -> Dict[str, str]:
        response = self.client.head_object(Bucket=self.bucket, Key=path)
        return response.get('Metadata', {})


class _DuckDBParquetConnector:
    def __init__(self):
        if not all([self.bucket, self.access_key, self.secret_key, self.region]):
            raise ValueError(
                f"{self.__class__.__name__} missing one or more environment variables for S3 access. "
                f"S3_BUCKET: {self.bucket} S3_KEY: {self.access_key} S3_SECRET: {self.secret_key} "
                f"S3_REGION: {self.region}, S3_ENDPOINT: {self.endpoint}"
            )

        self.connection = duckdb.connect(":memory:")
        self._initialize_httpfs()
        super().__init__()

    def _initialize_httpfs(self):
        self.connection.execute("INSTALL httpfs;")
        self.connection.execute("LOAD httpfs;")
        self.connection.execute(f"SET s3_access_key_id='{self.access_key}';")
        self.connection.execute(f"SET s3_secret_access_key='{self.secret_key}';")
        self.connection.execute(f"SET s3_region='{self.region}';")
        self.connection.execute(f"SET s3_endpoint='{self.endpoint.lstrip('https://')}';")
        self.connection.execute("SET s3_url_style='path';")

    def read_parquet(self, relative_path: str):
        uri = f"s3://{self.bucket}/{relative_path}"
        return self.connection.execute(f"SELECT * FROM read_parquet('{uri}')").fetch_df()
        
class DataLagoon(_DuckDBParquetConnector, _S3Connector):
    def __init__(self):
        self.region = os.getenv("S3_REGION")
        self.bucket = os.getenv("S3_BUCKET")
        self.endpoint = os.getenv("S3_ENDPOINT")
        self.access_key = os.getenv("S3_KEY")
        self.secret_key = os.getenv("S3_SECRET")
        super().__init__()
        
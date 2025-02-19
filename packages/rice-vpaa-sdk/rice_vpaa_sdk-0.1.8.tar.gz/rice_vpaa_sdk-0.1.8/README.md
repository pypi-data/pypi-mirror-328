# Rice VPAA SDK

Internal SDK for accessing the Rice VPAA API. Requires an API key.

## Install
```bash
pip install rice-vpaa-sdk
```

## Documentation

Full Swagger API documentation is available [here](https://vpaa-api-server-stnkl.ondigitalocean.app/docs).

## Usage
```python
from rice_vpaa import VPAAClient
client = VPAAClient(api_key="your-api-key")
```

## Get Faculty
```python
faculty = client.get_faculty(
    unit_ids=[123],
    tenure_statuses=["TTT"],
    employment_statuses=["Full Time"]
)
```

## Get Divisions
```python
divisions = client.get_divisions(departments_only=True)
```

## Get Open Positions
```python
positions = client.get_open_positions()
```

## Data Lagoon

The DataLagoon class is a convenience class for accessing data from the VPAA data lagoon.

DataLagoon depends on the following environment variables:
- S3_REGION
- S3_BUCKET
- S3_ENDPOINT
- S3_KEY
- S3_SECRET

```python
data_lagoon = DataLagoon()
data_lagoon.read_parquet("path/to/file.parquet")
data_lagoon.write_parquet(<a pandas dataframe>, "path/to/file.parquet")
data_lagoon.list_files("path/to/directory")
data_lagoon.get_metadata("path/to/file.parquet")
```




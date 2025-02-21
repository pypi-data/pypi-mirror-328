import os
from pathlib import Path

import ddeutil.extensions.datasets.pl as pl_ds
import polars as pl


def test_polars_csv():
    dataset = pl_ds.PolarsCsv.from_loader(
        "ds_csv_local_file",
        externals={},
    )
    assert dataset.conn.endpoint == dataset.endpoint
    assert "demo_customer.csv" == dataset.object
    assert dataset.exists()
    df: pl.DataFrame = dataset.load()
    assert [
        "CustomerID",
        "CustomerName",
        "CustomerOrgs",
        "CustomerRevenue",
        "CustomerAge",
        "CreateDate",
    ] == df.columns
    assert 2 == df.select(pl.len()).item()
    dataset.save(df, _object="demo_customer_writer.csv")

    # NOTE: Teardown and remove file that create from ``save`` method.
    Path(f"{dataset.endpoint}/demo_customer_writer.csv").unlink(missing_ok=True)

    df: pl.LazyFrame = dataset.scan()
    assert [
        "CustomerID",
        "CustomerName",
        "CustomerOrgs",
        "CustomerRevenue",
        "CustomerAge",
        "CreateDate",
    ] == df.columns
    dataset.sink(df, _object="demo_customer_sink.csv")
    # NOTE: Teardown and remove file that create from ``sink`` method.
    Path(f"{dataset.endpoint}/demo_customer_sink.csv").unlink(missing_ok=True)


def test_polars_json_nested():
    dataset = pl_ds.PolarsJson.from_loader(
        "ds_json_local_file",
        externals={},
    )
    assert f"{os.getenv('ROOT_PATH')}/tests/data/examples" == dataset.endpoint
    assert "demo_iot.json" == dataset.object
    df = dataset.load(options={})
    print(df)
    df = df.unnest("data")
    print(df)
    df = df.explode("sensor")
    print(df.schema)

    print(
        dataset.format_object("demo_iot_{datetime:%Y%m%d}.json", "2024-01-01")
    )
    df = dataset.load(
        _object="demo_iot_{datetime:%Y%m%d}.json",
        options={},
        dt="2024-01-01",
    )
    print(df)


def test_polars_json_nested_ubuntu():
    dataset = pl_ds.PolarsJson.from_loader(
        "ds_json_local_file_ubuntu", externals={}
    )
    assert "/home/runner/work/examples" == dataset.endpoint
    assert "/home/runner/work/examples" == dataset.conn.endpoint


def test_polars_parquet_save(test_path):
    df = pl.read_csv(
        test_path / "data/examples/demo_customer.csv", separator="|"
    )
    print(df)
    dataset = pl_ds.PolarsParq.from_loader(
        "ds_parquet_local_file", externals={}
    )
    print(dataset.save(df))
    df = pl.read_parquet(
        test_path / "data/examples/demo_parquet.snappy.parquet"
    )
    print(df)

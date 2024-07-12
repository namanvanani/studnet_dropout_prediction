import pandas as pd


class DataSchema:
    AMOUNT = "amount",
    CATEGORY = "category",
    DATE = "date",
    MONTH = "month",
    YEAR = "year"


def load_transaction_data(path: str) -> pd.DataFrame:
    data = pd.read_csv(
        path,
        dtype={DataSchema.AMOUNT: float, DataSchema.CATEGORY: str},
    )
    data["date"] = pd.to_datetime(data["date"])
    data["year"] = data["date"].dt.year.astype(str)
    data["month"] = data["date"].dt.month.astype(str)

    return data

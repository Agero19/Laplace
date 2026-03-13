import pandas as pd


def median_price(df: pd.DataFrame) -> float:
    """
    Calculate the median price from a DataFrame containing a 'price' column.

    Parameters:
    df (pd.DataFrame): A DataFrame with a 'price' column.

    Returns:
    float: The median price.
    """
    if "price" not in df.columns:
        raise ValueError("DataFrame must contain a 'price' column.")

    return df["price"].median()


def top_brands(df: pd.DataFrame, n: int = 5) -> pd.Series:
    """
    Get the top N brands by count from a DataFrame containing a 'brand' column.

    Parameters:
    df (pd.DataFrame): A DataFrame with a 'brand' column.
    n (int): The number of top brands to return.

    Returns:
    pd.Series: A Series containing the top N brands and their counts.
    """
    if "brand" not in df.columns:
        raise ValueError("DataFrame must contain a 'brand' column.")

    return df["brand"].value_counts().head(n)


def category_distribution(df: pd.DataFrame) -> pd.Series:
    """
    Calculate the distribution of categories from a DataFrame containing a 'category' column.

    Parameters:
    df (pd.DataFrame): A DataFrame with a 'category' column.

    Returns:
    pd.Series: A Series containing the count of each category.
    """
    if "category" not in df.columns:
        raise ValueError("DataFrame must contain a 'category' column.")

    return df["category"].value_counts()

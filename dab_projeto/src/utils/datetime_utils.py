from pyspark.sql.functions import current_timestamp, to_date, col

def timestamp_to_date_col(spark, df, timestamp_col, output_col):
    """
    Extracts the date from a timestamp column and adds it as a new column in the DataFrame.

    Parameters:
    spark (SparkSession): The Spark session object.
    df (DataFrame): The input DataFrame containing the timestamp column.
    timestamp_col (str): The name of the column with the timestamp.
    output_col (str): The name of the output column to store the date.

    Returns:
    DataFrame: A new DataFrame with an additional column for the date.
    """
    #Use to_date to extract the date part from the timestamp
    return df.withColumn(output_col, to_date(col(timestamp_col)))
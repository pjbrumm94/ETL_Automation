import pandas as pd
import os

def extract(file_path):
    """Extracts data from a CSV file."""
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        print("Data extracted successfully.")
        return df
    else:
        raise FileNotFoundError(f"File {file_path} not found.")

def transform(df):
    """Transforms the data by cleaning and processing."""
    # Example transformations
    df.dropna(inplace=True)  # Remove missing values
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]  # Normalize column names
    print("Data transformation completed.")
    return df

def load(df, output_path):
    """Loads the transformed data to a new CSV file."""
    df.to_csv(output_path, index=False)
    print(f"Data loaded successfully into {output_path}.")

def etl_pipeline(input_file, output_file):
    """Runs the full ETL pipeline."""
    try:
        data = extract(input_file)
        transformed_data = transform(data)
        load(transformed_data, output_file)
        print("ETL pipeline executed successfully.")
    except Exception as e:
        print(f"Error in ETL pipeline: {e}")

# Example usage
if __name__ == "__main__":
    input_file = "input_data.csv"  # Change this to your actual file
    output_file = "output_data.csv"
    etl_pipeline(input_file, output_file)

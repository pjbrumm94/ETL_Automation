# ETL Pipeline

This project implements a basic ETL (Extract, Transform, Load) pipeline using Python and Pandas.

## Features
- Extracts data from a CSV file.
- Cleans and processes the data.
- Saves the transformed data into a new CSV file.

## Requirements
Ensure you have the following installed:
- Python 3.x
- Pandas library (`pip install pandas`)

## Usage

1. Place your input data in a CSV file (e.g., `input_data.csv`).
2. Modify `input_file` and `output_file` paths in `etl_pipeline.py`.
3. Run the script:

   ```sh
   python etl_pipeline.py
   ```

## Functions
- **extract(file_path)**: Reads data from a CSV file.
- **transform(df)**: Cleans and processes the data.
- **load(df, output_path)**: Saves the processed data to a new CSV file.
- **etl_pipeline(input_file, output_file)**: Executes the full ETL process.

## Example
```python
input_file = "input_data.csv"
output_file = "output_data.csv"
etl_pipeline(input_file, output_file)
```

## License
This project is open-source and free to use.


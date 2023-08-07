"""
Data Processing Pipeline.
1) De-duplicate entries (Cleans the data by removing any errors or inconsistencies)
2) Delete incomplete data.
3) Remove oversamples (his step is specific to your data and needs to be implemented based on your requirements)
4) Remove incomplete or irrelevant responses (This step is specific to your data and needs to be implemented based on your requirements.)
5) Identify and review data outliers. (This step is specific to your data and needs to be implemented based on your requirements.)
6) Code open-ended data. (This step is specific to your data and needs to be implemented based on your requirements.)
7) Check data for consistency (This step is specific to your data and needs to be implemented based on user requirements.)

This step performed in Transforms the data into a format that can be used for data modeling


"""




import json
import requests
import csv


def extract_data_from_csv(file_path):
  """Extracts data from a CSV file."""
  with open(file_path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    data = []
    for row in reader:
      data.append(row)
  return data


def clean_data(data):
  """Cleans the data by removing any errors or inconsistencies."""
  # Check for and remove rows with missing values.
  data = [row for row in data if not any(value == '' for value in row)]

  # Check for and correct incorrect data types.
  for row in data:
    for index, value in enumerate(row):
      try:
        int(value)
        row[index] = int(value)
      except ValueError:
        try:
          float(value)
          row[index] = float(value)
        except ValueError:
          pass

  # Check for and remove duplicate rows.
  data = set(tuple(row) for row in data)
  data = list(data)

  return data

def transform_data(data):
  """Transforms the data into a format that can be used by the product."""
  # TODO: Implement this function
  return data

def load_data(data):
  """Loads the data into the product."""
  # TODO: Implement this function
  return data

def main():
  """Runs the data processing pipeline."""
  data = extract_data_from_csv('datasets/food_coded.csv')
  data = clean_data(data)
  data = transform_data(data)
  load_data(data)

if __name__ == "__main__":
  main()
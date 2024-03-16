import pandas as pd
import gzip
from io import BytesIO
import os

def calculate_ncd(file1, file2):
  """
  Calculates the Normalized Compression Distance (NCD) between two files.

  Args:
    file1 (str): Path to the first file.
    file2 (str): Path to the second file.

  Returns:
    float: The NCD value between the two files (0 <= NCD <= 1).
  """

  with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
    data1 = f1.read()
    data2 = f2.read()

  combined_data = data1 + data2

  # Calculate compressed sizes for individual and combined data
  compressed_size1 = len(gzip.compress(BytesIO(data1)))
  compressed_size2 = len(gzip.compress(BytesIO(data2)))
  compressed_size_combined = len(gzip.compress(BytesIO(combined_data)))

  # Handle potential division by zero (empty files)
  if compressed_size1 == 0 and compressed_size2 == 0:
    return 0

  try:
    ncd = (min(compressed_size1, compressed_size2) + 1) / (compressed_size_combined + 1)
  except ZeroDivisionError:
    # If combined size is zero, consider them identical (NCD=0)
    ncd = 0

  return ncd

def process_files(data_path, output_path):
  """
  Processes a dataset of text files, calculates compression stats and NCD,
  and saves the results to a CSV file.

  Args:
    data_path (str): Path to the directory containing the text files.
    output_path (str): Path to save the output CSV file.
  """

  data = []
  for filename in os.listdir(data_path):
    if filename.endswith('.txt'):
      file_path = os.path.join(data_path, filename)
      file_size = os.path.getsize(file_path)

      # Compress using gzip
      with open(file_path, 'rb') as f:
        compressed_data = gzip.compress(f.read())
      compressed_size = len(compressed_data)

      # Calculate compression ratio
      compression_ratio = 1 - (compressed_size / file_size)

      data.append({
          'filename': filename,
          'original_size': file_size,
          'compressed_size': compressed_size,
          'compression_ratio': compression_ratio
      })

  # Add NCD later (explained in step 3)

  df = pd.DataFrame(data)
  df.to_csv(output_path, index=False)

def main():
  """
  Processes the dataset, calculates statistics, and saves the results.
  """

  # Replace with your data and output paths
  data_path = 'Dataset/News Articles'
  output_path = 'Data_Mining/newspaper_data.csv'

  process_files(data_path, output_path)

if __name__ == "__main__":
  main()
import os
import gzip
import csv


# made a change

def compress_text_files(folder_path):
    # Create an output folder for compressed files
    output_folder = os.path.join(folder_path, "compressed")
    os.makedirs(output_folder, exist_ok=True)

    # Dictionary to store file information
    compression_info = {}

    # Iterate through all text files in the specified folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            file_path = os.path.join(folder_path, file_name)
            output_file_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.txt.gz")

            with open(file_path, 'rb') as file:
                # Compress the text file using gzip
                with gzip.open(output_file_path, 'wb') as compressed_file:
                    compressed_file.write(file.read())

            # Display the original and compressed file sizes
            original_size = os.path.getsize(file_path)
            compressed_size = os.path.getsize(output_file_path)

            print(f"Original: {file_name} - {original_size} bytes")
            print(f"Compressed: {os.path.basename(output_file_path)} - {compressed_size} bytes\n")

            # Store file info in the dictionary
            compression_info[file_name] = {
                'Original Size': original_size,
                'Compressed Size': compressed_size
            }

    print(f"Compression completed. Compressed files are stored in: {output_folder}")

    csv_file_path = os.path.join(folder_path, "compression_info.csv")
    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['File Name', 'Original Size (bytes)', 'Compressed Size (bytes)'])
        for file_name, info in compression_info.items():
            csv_writer.writerow([file_name, info['Original Size'], info['Compressed Size']])

    print(f"Dictionary exported to CSV file: {csv_file_path}")



# Set the path to the folder containing text files
# folder_path = r"C:\Users\ryand\Code\research_methods_cw02\mirror_data"
folder_path = r"C:\Users\ryand\Code\Data\Dataset News Articles\News Articles"

# Call the function to compress text files
compress_text_files(folder_path)


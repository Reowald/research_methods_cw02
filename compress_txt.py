import os
import gzip

def compress_text_files(folder_path):
    # Create an output folder for compressed files
    output_folder = os.path.join(folder_path, "compressed")
    os.makedirs(output_folder, exist_ok=True)

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

    print(f"Compression completed. Compressed files are stored in: {output_folder}")

# Set the path to the folder containing text files
folder_path = r"C:\Users\ryand\Code\research_methods_cw02\mirror_data"

# Call the function to compress text files
compress_text_files(folder_path)

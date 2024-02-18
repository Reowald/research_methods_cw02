import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def analyze_metadata(metadata, input_folder):
    # Display basic statistics of the metadata
    print(metadata.describe())

    # Match file_id with filename
    metadata['filename'] = 'xc' + metadata['file_id'].astype(str) + '_spectrogram.png'

    # Use apply to calculate file size for each row
    metadata['file_size'] = metadata['filename'].apply(lambda filename: os.path.getsize(os.path.join(input_folder, filename)) / 1024)

    # Group by english_cname and calculate average file size
    avg_file_size = metadata.groupby('english_cname')['file_size'].mean().reset_index(name='average_file_size')

    return avg_file_size

def plot_file_size_vs_bird_type(metadata_analysis):
    plt.figure(figsize=(12, 6))
    plt.bar(metadata_analysis['english_cname'], metadata_analysis['average_file_size'], color='skyblue')
    plt.xlabel('English Bird Name')
    plt.ylabel('Average File Size (KB)')
    plt.title('Average File Size vs. English Bird Name')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
    plt.tight_layout()
    plt.show()

def plot_scatter_file_size_vs_species(metadata):
    # Get unique species and assign a color to each
    unique_species = metadata['species'].unique()
    cmap = plt.get_cmap('tab10')  # Using the 'tab10' colormap

    # Split data into three batches
    num_batches = 3
    batch_size = len(unique_species) // num_batches

    # Iterate through batches and create a separate figure for each batch
    for batch in range(num_batches):
        start_idx = batch * batch_size
        end_idx = (batch + 1) * batch_size if batch < num_batches - 1 else len(unique_species)

        # Create a new figure for each batch
        plt.figure(figsize=(12, 6))
        plt.title(f'Scatter Plot: File Size vs. Species - Batch {batch + 1}')

        # Plot scatter points for the current batch
        for i in range(start_idx, end_idx):
            species = unique_species[i]
            species_data = metadata[metadata['species'] == species]
            color = cmap(i % 10)  # Ensure we don't go out of bounds for the colormap
            plt.scatter(species_data['file_size'], species_data['species'], label=species, color=color, alpha=0.7)

        plt.xlabel('File Size (KB)')
        plt.ylabel('Species')
        plt.legend()  # Show legend with species names
        plt.tight_layout()
        plt.show()



if __name__ == "__main__":
    metadata_file = 'C:\\Users\\ryand\\Code\\Data\\archive\\birdsong_metadata.csv'
    input_folder = 'C:\\Users\\ryand\\Code\\Data\\archive\\songs\\songs\\spectrograms'

    # Read metadata using pandas
    metadata = pd.read_csv(metadata_file)

    # Display the general dimensions
    print("Dimensions of the DataFrame:")
    print(metadata.shape)

    # Display basic information about the DataFrame
    print("\nInformation about the DataFrame:")
    print(metadata.info())

    # # Display summary statistics of the DataFrame
    # print("\nSummary statistics of the DataFrame:")
    # print(df.describe())

    # Display the first few rows of the DataFrame
    print("\nFirst few rows of the DataFrame:")
    print(metadata.head())

    # Analyze metadata and calculate average file size
    metadata_analysis = analyze_metadata(metadata, input_folder)

    # Plot the correlation between file size and English bird names
    plot_file_size_vs_bird_type(metadata_analysis)

    # Plot scatter plot for file size and species
    plot_scatter_file_size_vs_species(metadata)


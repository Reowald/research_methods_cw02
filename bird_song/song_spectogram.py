import soundfile as sf
import librosa
import matplotlib.pyplot as plt
import os
import numpy as np


def create_spectrogram(input_file, output_path, duration=10, image_format='png'):
    audio_data, sample_rate = librosa.load(input_file, duration=duration)
    spectrogram = librosa.feature.melspectrogram(y=audio_data, sr=sample_rate)
    spectrogram_db = librosa.power_to_db(spectrogram, ref=np.max)
    plt.figure(figsize=(10, 6))
    librosa.display.specshow(spectrogram_db, sr=sample_rate, x_axis='time', y_axis='mel')
    plt.axis('off') 
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)  # Remove padding
    plt.margins(0, 0)

    filename = os.path.splitext(os.path.basename(input_file))[0]
    
    output_file = f"{output_path}/{filename}_spectrogram.{image_format}"
    plt.savefig(output_file, format=image_format, bbox_inches='tight', pad_inches=0)
    plt.close()

if __name__ == "__main__":
    input_folder = r'C:\\Users\\ryand\\Code\Data\\archive\\songs\\songs'
    output_folder = r'C:\\Users\\ryand\\Code\Data\\archive\\songs\\songs\\spectrograms'

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each FLAC file in the input folder
    for file in os.listdir(input_folder):
        if file.endswith(".flac"):
            input_file = os.path.join(input_folder, file)
            create_spectrogram(input_file, output_folder, duration=10)

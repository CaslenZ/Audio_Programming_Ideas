import tkinter as tk
from tkinter import filedialog, messagebox
import librosa
import librosa.display
import matplotlib.pyplot as plt
import os
import numpy as np

filename = None


def load_audio_file():
    global filename
    root = tk.Tk()
    root.withdraw()
    audio_file = filedialog.askopenfilename(
        title="Select audio file",
        filetypes=[("Audio Files", "*.wav;*.mp3;*.ogg;*.flac;*.aiff;*.au;*.raw")]
    )
    if not audio_file:
        return None
    filename = os.path.basename(audio_file)
    return filename


def audio_to_image(audio_file, output_image):
    y, sr = librosa.load(audio_file, sr=None)
    stft = np.abs(librosa.stft(y))
    f = np.fft.fftfreq(stft.shape[-1], d=1 / sr)
    plt.figure(figsize=(12, 4))
    librosa.display.specshow(stft, sr=sr, x_axis='time', y_axis='log', fmax=sr / 2)
    plt.colorbar(format='%+2.0f dB')
    plt.title('Audlazyr Spectrogram')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    output_path = os.path.join(desktop_path, output_image)
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0.1)
    plt.close()


def open_file_dialog():
    global filename
    root = tk.Tk()
    root.withdraw()
    audio_file = filedialog.askopenfilename(
        title="Audlazyr Spectrogram (Github: @CaslenZ)",
        filetypes=[("Audio Files", "*.wav;*.mp3;*.ogg;*.flac;*.au;*.aiff;*.wavpack"), ("All files", "*.*")]
    )
    if audio_file:
        filename = os.path.basename(audio_file)
        output_image = filename + '.png'
        audio_to_image(audio_file, output_image)
        messagebox.showinfo("Success!", f"The spectrogram has been created and saved to the desktop: {output_image}")
    else:
        messagebox.showerror("Error!", "No file selected! ")


open_file_dialog()
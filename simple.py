from scipy.io import wavfile
import os
import numpy as np

class SoundFile:
  file_name: str
  full_path: str
  sample_rate: int
  len: int
  data: np.array

  def __init__(self, file_name: str, full_path: str):
    self.file_name = file_name
    self.full_path = full_path

    self.load_audio_data()

  def __repr__(self):
    number_of_channels = 1 if len(self.data.shape) == 1 else self.data.shape[1]
    length = self.data.shape[0] / self.sample_rate

    return f"File name: {self.file_name}, Number of channels: {number_of_channels}, Length: {length}s"

  def load_audio_data(self):
    sample_rate, data = wavfile.read(self.full_path)
    
    self.sample_rate = sample_rate
    self.data = np.array(data, dtype=np.int16)
    self.len = self.data.shape[0]


def load_sound_files() -> list[SoundFile]:
  data_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'audio')
  sound_files: list[SoundFile] = []
  for file_name in os.listdir(data_directory):
    full_file_path = os.path.join(data_directory, file_name)
    if os.path.isfile(full_file_path):
      sound_files.append(SoundFile(file_name, full_file_path))

  return sound_files


if __name__ == "__main__":
  print(load_sound_files())

import os
import pandas as pd
from classes.FileSource import FileSource


class TxtSource(FileSource):
    def create_path(self):
        current_dir = os.getcwd()
        self.folder_path = os.path.join(current_dir, 'data', 'txt_files')
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previous_files and file.endswith('.txt')]

        if new_files:
            print(f"New .txt files detected {new_files}")
            self.previous_files = current_files
        else:
            print("No new .txt files detected.")
            self.get_data()

    def get_data(self):
        data_frames = []
        for file_path in self.previous_files:
            try:
                path = os.path.join(self.folder_path, file_path)
                data = pd.read_csv(path, sep='\t')
                data_frames.append(data)
            except Exception as e:
                print(f"An error ocurred while reading the .txt file: {e}")
        
        if data_frames:
            self.combined_data = pd.concat(data_frames, ignore_index=True)
            print(self.combined_data)
            return self.combined_data
        else:
            return None
        
    def transform_data_to_df(self):
        return super().transform_data_to_df()
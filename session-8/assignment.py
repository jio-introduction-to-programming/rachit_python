import pandas as pd
import pickle
import json
import os
import cv2

def persist_data(data, filename):
    # pass  # Use Python built-in functions to write 'data' to 'filename'
    with open(filename, 'w') as f:
        f.write(data)

def read_file(filename):
    # pass  # Use Python built-in functions to read contents of 'filename' and print them to screen
    with open(filename, 'r') as f:
        data = f.read()
    return data

def write_file(filename, data):
    # pass  # Use Python built-in functions to write 'data' to 'filename'
    with open(filename, 'w') as f:
        data = f.read()
    return data

def delete_file(filename):
    # pass  # Use Python built-in functions to delete 'filename'
    os.remove(filename)

def overwrite_file(filename, data):
    # pass  # Use Python built-in functions to overwrite 'filename' with 'data'
    with open(filename, 'w') as f:
        f.write(data)

def append_file(filename, data):
    # pass  # Use Python built-in functions to append 'data' to 'filename'
    with open(filename, 'a') as f:
        f.write(data)

def write_binary_file(filename, data):
    # pass  # Use Python built-in functions to write 'data' as binary to 'filename'
    with open(filename, 'wb') as f:
        f.write(data)

def read_image_file(filename):
    # pass  # Use OpenCV to read 'filename' as an image
    img = cv2.imread(filename, flags=cv2.COLOR_BGR2RGB)
    return img


def read_csv_file(filename):
    # pass  # Use Pandas to read 'filename' as a csv
    df = pd.read_csv(filename)
    return df

def write_csv_file(filename, df:pd.DataFrame):
    # pass  # Use Pandas to write dataframe 'df' to 'filename'
    df.to_csv(filename)

def read_json_file(filename):
    # pass  # Use json to read 'filename' as a json
    dict_json = {}
    with open(filename, 'r') as f:
        dict_json = json.load(filename)
    return dict_json

def write_json_file(filename, data):
    # pass  # Use json to write 'data' to 'filename'
    with open(filename, 'w') as f:
        json.dump(data, f)

def write_pickle_file(filename, data):
    # pass  # Use pickle to write 'data' to 'filename'
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def read_pickle_file(filename):
    # pass  # Use pickle to read 'filename'
    with open(filename, 'rb') as f:
        data = pickle.load(f)

    return data

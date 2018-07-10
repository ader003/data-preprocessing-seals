import numpy as np
import pandas as pd
import scipy.io as sio # for saving as .mat
import os # for getting filepath
import copy

def main():
    dir_name = input("Directory name: ")
    # get list of files
    contents = os.listdir(dir_name)
    filename = copy.deepcopy(contents)
 
    # for each file, preprocess data and save as .mat
    for i in range(len(contents)):
        contents[i] = os.path.join(os.path.relpath(dir_name), contents[i])
        data = pd.read_csv(contents[i], sep=",", names=['number', 'behaviour_event', 'value', 'type_event', 'fps', 'time', 'depth', 'x', 'y', 'z', 'behaviour', 'type', 'location', 'place', 'raw', 'date', 'doe'])

        # drop columns
        drop_cols = ['behaviour_event', 'type_event', 'fps', 'time', 'location', 'raw', 'date', 'doe']
        data.drop(drop_cols, axis=1, inplace=True)
        print(data.head())
        # save as .mat
        # dict_data = {'number': data['number'], 'value': data['value'], 'depth': data['depth'], 'x': data['x'], 'y': data['y'], 'z': data['z'], 'behaviour': data['behaviour'], 'type': data['type'], 'place': data['place'], } # dictionary to save MATLAB data in/to
        # sio.savemat(filename[i], dict_data, appendmat=True)
        data.to_csv(filename[i], sep=",")


if __name__ == "__main__":
    main()

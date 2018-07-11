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
 
    # for each file, preprocess data and save as .csv
    for i in range(len(contents)):
        contents[i] = os.path.join(os.path.relpath(dir_name), contents[i])
        data = pd.read_csv(contents[i], sep=",", header=0, names=['number', 'behaviour_event', 'value', 'type_event', 'fps', 'time', 'depth', 'x', 'y', 'z', 'behaviour', 'type', 'location', 'place', 'raw', 'date', 'doe'])

        # drop columns
        drop_cols = ['behaviour_event', 'type_event', 'fps', 'time', 'location', 'raw', 'date', 'doe']
        data.drop(drop_cols, axis=1, inplace=True)
        
        # replace values in 'behaviour', 'type', and 'place'
        data['behaviour'].replace(to_replace={'other': 0, 'moving': 1, 'in': 2, 'foraging': 3, 'manipulation': 4, 'chewing': 5, 'thrash': 6, 'slow': 7, 'swimming': 8, 'holdntear': 9, 'still': 10, 'out': 11, 'sitting': 12}, inplace=True)
        data['type'].replace(to_replace={'Other': 0, 'Travelling': 1, 'Foraging': 2, 'Resting': 3}, inplace=True)
        data['place'].replace(to_replace={'land': 1, 'surface': 0, 'underwater': -1}, inplace=True)
        # print(data.head())
        print("Processed " + str(filename[i]))

        # save as .mat
        # dict_data = {'number': data['number'], 'value': data['value'], 'depth': data['depth'], 'x': data['x'], 'y': data['y'], 'z': data['z'], 'behaviour': data['behaviour'], 'type': data['type'], 'place': data['place'], } # dictionary to save MATLAB data in/to
        # sio.savemat(filename[i], dict_data, appendmat=True)
        
        # UNCOMMENT AFTER TESTING:
        data.to_csv(filename[i], sep=",", header=['number', 'value', 'depth', 'x', 'y', 'z', 'behaviour', 'type', 'place'])


if __name__ == "__main__":
    main()

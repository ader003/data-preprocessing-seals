import numpy as np
import pandas as pd
import scipy as sp # for saving as .mat
import os # for getting filepath

# find file and open

# get list of filenames 

# for filename in filenames: (do the following)
data = pd.read_csv(os.path.abspath(filename), sep=",", names=['number', 'behaviour_event', 'value', 'type_event', 'fps', 'time', 'depth', 'x', 'y', 'z', 'behaviour', 'type', 'location', 'place', 'raw', 'date', 'doe'])

# drop columns
data.drop(['behaviour_event', 'type_event', 'fps', 'time', 'location', 'raw', 'date', 'doe'], axis=1)

# save as .mat
# sp.io.savemat(filename, appendmat=True)


def main():

    return

if __name__ == "__main__":
    main()

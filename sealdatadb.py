import pandas as pd
import numpy as np
import os
# import sqlite3
# conn = sqlite3.connect('fursealdata.db')
# c = conn.cursor()
# c.execute('''DROP TABLE fursealdata''')
# c.execute('''CREATE TABLE fursealdata
#              (behavior integer, filename text, range text)''')

# iterate through files and insert information into the db file
dir_name = input("Directory name: ")
contents = os.listdir(dir_name) # the filenames

for i in contents:
    i = os.path.join(os.path.relpath(dir_name), i)
    data = pd.read_csv(i, sep=",", 
        header=0, names=['depth', 'x', 'y', 'z', 'behaviour', 'type', 'place'],
        low_memory=False)

    print(i[5:]) # to remove /
    for b in range(0, 27):
        temp = data.loc[data['behaviour'] == b]
        if len(temp) > 0:
            print(temp.index.values) # this is a list of the indexes in the file that are of behavior b
#         c.execute("INSERT INTO fursealdata(?, ?, ?) VALUES ('" + b + "','" + i[5:] + "','" + "1-2" + "')")
#         conn.commit()
# conn.close()

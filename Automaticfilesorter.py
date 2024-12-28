

# AUTOMATIC FILE SORTER

import os,shutil

tri9= r"F:/Disque dur E/DATA SCIENCE/Power bi/"
file_name = os.listdir(tri9)
folder_names = ['Power bi','Excel']
for loop in range(0,2):
    if not os.path.exists(tri9+folder_names[loop]):
        os.makedirs(tri9+folder_names[loop])

for file in file_name:
    if '.xlsx' in file and not os.path.exists(tri9+'Excel/'+file):
        shutil.move(tri9+file,tri9+'Excel/'+file)
    elif '.pbix' in file and not os.path.exists(tri9+'Power bi/'+file):
        shutil.move(tri9+file,tri9+'Power bi/'+file)       
  

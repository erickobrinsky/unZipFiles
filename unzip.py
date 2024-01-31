# A python program that copies all PBIX files within subfolders in a folder, copies them into a single folder and then unzip each on in its own folder.
#

import  os, shutil, zipfile

# Get the path of the folder where the PBIX files are stored
path = r"C:\Users\E901895\OneDrive - Allscripts Healthcare, LLC\Desktop\pbi\pbix"

# Get the path of the folder where the PBIX files will be copied  and unzipped
path_copy = r"C:\Users\Desktop\pbi\unzippbix"

# Get the name of the folder where the PBIX files will be copied and unzipped
folder_copy = "unzippbix"

# Get the path of the folder where the PBIX files will be copied and unzipped
path_copy = path_copy + "\\" + folder_copy

 # Create a folder to store the PBIX files
os.mkdir(path_copy)

# Get the list of all the subfolders in the folder
subfolders = [f.path for f in os.scandir(path) if f.is_dir()]

# Copy all PBIX files within subfolders in a folder, copies them into a single folder
for subfolder in subfolders:
    for file in os.listdir(subfolder):
        if file.endswith(".pbix"):
            shutil.copy(subfolder + "\\" + file, path_copy)

# Get the list of all the PBIX files in the folder
files = [f.path for f in os.scandir(path_copy) if f.is_file()]

# Unzip each  on in its own folder
for file in files:  # loop through all the files in the folder
    with zipfile.ZipFile(file, 'r') as zip_ref:  # open the file
        try:
            zip_ref.extractall(file.replace(".pbix", ""))  # extract the file to the folder
        except:
            continue
        zip_ref.close()  # close the file

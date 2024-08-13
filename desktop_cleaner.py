import os
import shutil

def create_subfolders(folder_path, subfolder_name):
    pass


def clean_folders(folder_path):
    # Loop through the directory files
    for filename in os.listdir(folder_path):
        #If the file is a valid file, take the subfolder name to sort it into different files
        if os.path.isfile(os.path.join(folder_path, filename)):
            # search the file for the '.' till the end of the str, and make it lowercase
            file_extension = filename.split('.')[-1].lower()
            # if there is a file extension, then make the subfolder name the exension + Files
            if file_extension: 
                subfolder_name = f"{file_extension.upper()} Files"




if __name__ == "__main__":
    print("Desktop Cleaner Script")
    print("Please enter your computer username:")
    username = input()

    print("Please enter the name of the path you want to clean up.")

    folder_name = input()
    # Create the folder_path variable through the username + folder_name input
    folder_path  =  '/Users/' + username + '/' + folder_name
    # Check if the path is a directory
    if os.path.isdir(folder_path):
        clean_folders(folder_path)
    else:
        print("Path not found, please ensure that the path is correct and please try again.")



    
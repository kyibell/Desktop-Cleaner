import os
import shutil

def clean_folders(folder_path):
    pass




if __name__ == "__main__":
    print("Desktop Cleaner Script")
    print("Please enter your computer username:")
    username = input()

    print("Please enter the name of the path you want to clean up.")

    folder_name = input()

    folder_path  =  '/Users/' + username + '/' + folder_name

    print(folder_path) 

    if os.path.isdir(folder_path):
        clean_folders(folder_path)
    else:
        print("Path not found, please ensure that the path is correct and please try again.")



    
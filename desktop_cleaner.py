import os
import shutil

def create_subfolders(current_directory, subfolder_name):
    sub_folder_path = os.path.join(current_directory, subfolder_name)


def clean_folders(current_directory):
    # Loop through the directory files
    for filename in os.listdir(current_directory):
        
        #If the file is a valid file, take the subfolder name to sort it into different files
        if os.path.isfile(os.path.join(current_directory, filename)):
            # search the file for the '.' till the end of the str, and make it lowercase
            file_extension = filename.split('.')[-1].lower()
            # if there is a file extension, then make the subfolder name the extension + Files
            if file_extension: 
                subfolder_name = f"{file_extension.upper()} Files"
                subfolder_path = create_subfolders(current_directory, filename)
                shutil.move(current_directory, subfolder_name)




if __name__ == "__main__":
    print("Desktop Cleaner Script")
    
    current_directory = os.path.dirname(__file__)
    print(current_directory)

    print(f"You are running this script in: {current_directory}. Would you like to continue? Y/N")
    response = input().lower() 


    if response == 'y' or 'yes':
        print("Yes")
       # clean_folders(current_directory)
    else:
        print("Please run this script in the directory you want to clean.")


    
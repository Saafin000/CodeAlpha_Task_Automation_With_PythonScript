import os
import shutil

def organize_files(source_folder):
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]

    file_types = set(os.path.splitext(file)[1][1:] for file in files)
    for file_type in file_types:
        folder_path = os.path.join(source_folder, file_type.upper() + "_Files")
        os.makedirs(folder_path, exist_ok=True)

    for file in files:
        file_type = os.path.splitext(file)[1][1:]
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(source_folder, file_type.upper() + "_Files", file)
        shutil.move(source_path, destination_path)

    print("Files organized successfully!")

def main():
    source_folder_path = input("Enter the path of the folder to organize: ")


    if not os.path.exists(source_folder_path):
        print("Error: The specified path does not exist.")
        return

    organize_files(source_folder_path)

if __name__ == "__main__":
    main()
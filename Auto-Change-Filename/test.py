import os

def change_file_extensions(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") and not filename.endswith(".full.jpg"):
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, filename.replace(".jpg", ".full.jpg"))
            os.rename(old_file, new_file)
            print(f"Renamed: {old_file} -> {new_file}")

# Replace with the path to your folder
folder_path = r"C:\Users\aiden\Desktop\New folder (3)\testtest"
change_file_extensions(folder_path)
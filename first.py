import os
import shutil

# NOTE: You can write every single extension inside tuples
dict_extensions = {
    'audio_extensions': ('.mp3', '.m4a', '.wav', '.flac'),
    'videos_extensions': ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'documents_extensions': ('.doc', '.pdf', '.txt', '.docx')
}

folderpath = input('enter folder path: ')


def file_finder(folder_path, file_extensions):
    files = []
    for file in os.listdir(folder_path):
        for extension in file_extensions:
            if file.endswith(extension):
                files.append(file)
    return files


for extension_type, extension_tuple in dict_extensions.items():
    folder_name = extension_type.split('_')[0] + ' Files'
    folder_path = os.path.join(folderpath, folder_name)
    # Check if folder already exists
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    else:
        print(f"Folder '{folder_name}' already exists.")
    for item in file_finder(folderpath, extension_tuple):
        item_path = os.path.join(folderpath, item)
        item_new_path = os.path.join(folder_path, item)
        # Check if file already exists in the destination folder
        if not os.path.exists(item_new_path):
            shutil.move(item_path, item_new_path)
        else:
            print(f"File '{item}' already exists in '{folder_name}'.")


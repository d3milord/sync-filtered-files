import os
import shutil

start_path = 'F:\\'
destination_path = 'C:\\Users\\davide.pecorari\\Desktop\\nk'
filename_filter = '.xml.tsd'


def list_files_to_move(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for current_file in files:
            if filename_filter in current_file:
                file_list.append(os.path.join(root, current_file))
    return file_list


def recreate_folder_tree(folder_list):
    final_path = destination_path
    for index in range(0, len(folder_list) - 1):
        final_path = os.path.join(final_path, folder_list[index])
        if not os.path.exists(final_path):
            os.makedirs(final_path)


def copy_file_to_destination(file_to_copy, path_relativo):
    shutil.copy(file_to_copy, os.path.join(destination_path, path_relativo))


for file in list_files_to_move(start_path):
    relative_file_path = file.replace(start_path, '')
    recreate_folder_tree(relative_file_path.split('\\'))
    copy_file_to_destination(file, relative_file_path)





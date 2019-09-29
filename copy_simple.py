import os
import shutil


def simple_copy(src, dest):
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, dest)


if __name__ == '__main__':
    src_path = ''
    dest_path = ''
    # simple_copy(src_path, dest_path)

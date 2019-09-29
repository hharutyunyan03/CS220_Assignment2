import os
import shutil
from concurrent.futures import ProcessPoolExecutor


def copy_with_processes(src, dest):
    src_files = os.listdir(src)
    with ProcessPoolExecutor(max_workers=5) as executor:
        for file_name in src_files:
            full_file_name = os.path.join(src, file_name)
            if os.path.isfile(full_file_name):
                # submit() version
                executor.submit(shutil.copy, full_file_name, dest)


if __name__ == '__main__':
    src_path = ''
    dest_path = ''
    # copy_with_processes(src_path, dest_path)

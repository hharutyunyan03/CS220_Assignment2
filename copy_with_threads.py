import os
import shutil
from concurrent.futures import ThreadPoolExecutor
from functools import partial


def copy_with_threads(src, dest):
    src_files = os.listdir(src)
    src_files_path = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        for file_name in src_files:
            full_file_name = os.path.join(src, file_name)
            src_files_path.append(full_file_name)
        shutil_for_map = partial(shutil.copy, dst=dest)
        # map() version
        executor.map(shutil_for_map, src_files_path)


if __name__ == '__main__':
    src_path = ''
    dest_path = ''
    # copy_with_threads(src_path, dest_path)

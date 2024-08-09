import zipfile
import os
import re

base_path = './extracted_content'

if not os.path.exists(base_path):
    zip_obj = zipfile.ZipFile('unzip_me_for_instructions.zip','r')
    zip_obj.extractall(".")
    print("Unzipped directory")
else: 
    print("The directory already exists")

dirs = os.listdir(base_path)
print(dirs)

for dir in dirs:
    if os.path.isdir(base_path + '/' + dir):
        print(f"Dirname: {dir}")
        sub_dirs = os.listdir(base_path + '/' + dir)
        for files in sub_dirs:
            print(f"\tThis is the file {files}")
            some_file = open(base_path + '/' + dir + '/' + files, "r")
            telephone = re.findall(r'(\d{3})-(\d{3})-(\d{4})', some_file.read())
            if len(telephone) > 0:
                print(f'\t\tThis is the telephone: {'-'.join(telephone[0])}')
    else:
        print(f"This is a file: {dir}")

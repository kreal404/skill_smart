import os
from zipfile import ZipFile

def create_archive(file_name, ext):
    archive = []

    for f in os.listdir('.'):
        if f.endswith(ext):
            archive.append(f)

    with ZipFile(file_name, 'w') as zip_archive:
        for f in archive:
            zip_archive.write(f)

file_name = 'test.zip'
ext = '.txt'

create_archive(file_name, ext)
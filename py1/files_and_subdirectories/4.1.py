import os

def list_files_and_directories(path, ext, flag):
    file_list = []
    directory_list = []

    for root, directories, files in os.walk(path):
        if flag:
            for directory in directories:
                directory_list.append(os.path.join(root, directory))

        for file in files:
            if file.endswith(ext):
                file_list.append(os.path.join(root, file))

    return [file_list, directory_list]

# path = 'C:/Users/jws-8/Desktop/Softwise/skill_smart/python1/py1'
# ext = '.txt'
# flag = False

# result = list_files_and_directories(path, ext, flag)
# print(result)
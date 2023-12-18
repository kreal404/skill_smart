import os

def del_dir(dir):
    success = False
    no_subdirs = True

    for item in os.listdir(dir):
        item_path = os.path.join(dir, item)

        if os.path.isdir(item_path):
            no_subdirs = False
            break

    if no_subdirs:
        for root, dirs, files in os.walk(dir):

            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)

            for dir in dirs:
                dir_path = os.path.join(root, dir)
                os.rmdir(dir_path)

        os.rmdir(dir)
        success = True
    else:
        print(f"Каталог не может быть удален, так как он содержит подкаталоги")

    return success

# dir = "C:/Users/jws-8/Desktop/Softwise/skill_smart/python1/py1/files_and_subdirectories/test"
# result = del_dir(dir)

# print(result)
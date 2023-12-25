import os
from PIL import Image

def convert_images(from_ext, to_ext):
    current_dir = os.getcwd()
    files = os.listdir(current_dir)
    from_files = []
    
    for file in files:
        if file.endswith(from_ext):
            from_files.append(file)

    for file in from_files:
        image_path = os.path.join(current_dir, file)
        image = Image.open(image_path)
        new_path = os.path.join(current_dir, os.path.splitext(file)[0] + to_ext)
        image.save(new_path, to_ext[1:])
    
    print("Конвертация завершена!")

convert_images(".jpg", ".png")
import os
from PIL import Image, ImageDraw, ImageFont

def convert_images(from_ext, to_ext):
    current_dir = os.getcwd()
    files = os.listdir(current_dir)
    from_files = []
    
    for file in files:
        if file.endswith(from_ext):
            from_files.append(file)

    for file in from_files:
        image_path = os.path.join(current_dir, file)
        image = Image.open(image_path).convert("RGBA")
        width, height = image.size
        
        square_size = min(width, height) // 2
        square_center = (width // 2, height // 2)
        square_coords = (
            square_center[0] - square_size // 2,
            square_center[1] - square_size // 2,
            square_center[0] + square_size // 2,
            square_center[1] + square_size // 2
        )
        square_image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(square_image)
        
        text = "Hello,\nWorld!"
        font_size = 30
        font_color = (255, 0, 255)
        font = ImageFont.truetype("font.ttf", font_size)
        draw.text(square_center, text, font=font, fill=font_color, anchor="mm")
        
        result_image = Image.alpha_composite(image, square_image)
        
        new_path = os.path.join(current_dir, os.path.splitext(file)[0] + to_ext)
        result_image.save(new_path)
    
    print("Конвертация завершена!")

convert_images(".jpg", ".png")
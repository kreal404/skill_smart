def find_files(path: str) -> list[str]:
    files = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            files.append(item_path)
        elif os.path.isdir(item_path):
            files.extend(find_files(item_path))
    return files


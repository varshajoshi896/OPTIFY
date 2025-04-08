import os

def rename_files(folder_path, prefix):
    files = os.listdir(folder_path)
    for count, filename in enumerate(files):
        ext = os.path.splitext(filename)[1]
        new_name = f"{prefix}_{count+1}{ext}"
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        os.rename(src, dst)
        print(f'Renamed: {filename} -> {new_name}')

# Example usage:
folder = r"c:\Users\Admin\Documents\Filestorename"  # Change this path
rename_files(folder, "file")

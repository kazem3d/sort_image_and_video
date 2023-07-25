import os

def find_files_formats(directory):
    file_formats = {}
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_format = filename.split('.')[-1].lower()
            if file_format:
                file_formats.setdefault(file_format, []).append(os.path.join(dirpath, filename))

    return file_formats

if __name__ == "__main__":
    target_directory = '/media/darvin/My Book/src'

    if not os.path.isdir(target_directory):
        print("Invalid directory path.")
    else:
        all_file_formats = find_files_formats(target_directory)
        print("\nFile Formats and Their Corresponding Files:")
        for file_format, files in all_file_formats.items():
            print(f"{file_format}")
            # for file_path in files:
            #     print(f"  {file_path}")
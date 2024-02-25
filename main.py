import os
import shutil
from datetime import datetime
import jdatetime
 
# WARNING : THE source_directory AND distination_directory MUST HAVE NO COMMON
# EXAMPLE 
# source_directory = "/home/darvin/Pictures/
# distination_directory = "/home/darvin/Pictures/
# IS WRONG


def get_persian_month_name(finglish_month):
    persian_months = {
        'far': 'فروردین',
        'ord': 'اردیبهشت',
        'kho': 'خرداد',
        'tir': 'تیر',
        'mor': 'مرداد',
        'sha': 'شهریور',
        'meh': 'مهر',
        'aba': 'آبان',
        'aza': 'آذر',
        'dey': 'دی',
        'bah': 'بهمن',
        'esf': 'اسفند'
    }

    # Make sure the input is in lowercase to handle case-insensitive matching
    finglish_month_lower = finglish_month.lower()

    # Use the provided Finglish month to retrieve the Persian month name from the dictionary
    if finglish_month_lower in persian_months:
        return persian_months[finglish_month_lower]
    else:
        return "Invalid Finglish month representation."
    

def get_creation_month(file_path):
    timestamp = os.path.getctime(file_path)
    create_date = datetime.fromtimestamp(timestamp)
    persian_date = jdatetime.datetime.fromgregorian(datetime=create_date)
    # Get the month's full name in Persian
    persian_month_name = get_persian_month_name(persian_date.strftime('%b'))
    return f'{persian_date.strftime("%Y/%m")} {persian_month_name}'

 
def get_unique_filename(destination_dir, filename):
    base_name, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(destination_dir, new_filename)):
        new_filename = f"{base_name}_{counter}{ext}"
        counter += 1
    return new_filename


def copy_file_with_unique_name(source_file, destination_dir,duplicates_folder):
    destination_file = os.path.join(destination_dir, os.path.basename(source_file))
    duplicates_file = os.path.join(duplicates_folder, os.path.basename(source_file))
    if os.path.exists(destination_file):
        new_filename = get_unique_filename(duplicates_folder, os.path.basename(source_file))
        duplicates_file = os.path.join(duplicates_folder, new_filename)

        shutil.copy(source_file, duplicates_file)
        print(f"Copied {source_file} to duplicates dir")
    else:
        shutil.copy(source_file, destination_file)
        print(f"Copied {source_file} to {destination_file}")


def search_and_sort_files(src_dir,dist_dir):
    jpeg_folder = os.path.join(dist_dir, 'images')
    mp4_folder = os.path.join(dist_dir, 'vidoes')
    duplicates_folder = os.path.join(dist_dir, 'duplicates')

    os.makedirs(jpeg_folder, exist_ok=True)
    os.makedirs(mp4_folder, exist_ok=True)
    os.makedirs(duplicates_folder, exist_ok=True)

    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.lower().endswith(('.jpeg', '.jpg')):
                file_path = os.path.join(root, file)
                creation_month = get_creation_month(file_path)
                destination_folder = os.path.join(jpeg_folder, creation_month)
                os.makedirs(destination_folder, exist_ok=True)
                copy_file_with_unique_name(file_path,destination_folder,duplicates_folder)
            elif file.lower().endswith(('.mp4','.3gp')):
                file_path = os.path.join(root, file)
                creation_month = get_creation_month(file_path)
                destination_folder = os.path.join(mp4_folder, creation_month)
                os.makedirs(destination_folder, exist_ok=True)
                copy_file_with_unique_name(file_path,destination_folder,duplicates_folder)

if __name__ == "__main__":
    source_directory = "/media/darvin/My Book/kazem"
    distination_directory = "/media/darvin/My Book/dist"
    search_and_sort_files(source_directory,distination_directory)

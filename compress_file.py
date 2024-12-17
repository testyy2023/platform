import time
import zipfile
import os

def compress_folders(folder_path,zip_path):
    import zipfile
    import os

    # def compress_folder_to_zip(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

# 使用示例
print(os.getcwd())
compress_folders('allure_report', './test{}.zip'.format(time.strftime("%Y%m%d%H%M%S")))

import os
import uuid
from datetime import datetime

from werkzeug.utils import secure_filename


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        os.chmod(folder_path, os.O_RDWR)  # 修改 创建的 文件夹权限 可读可写


# 修改又件名称 原文件名不保存
def change_filename_with_timestamp_uuid(filename):
    fileinfo = os.path.splitext(filename)
    # datetime.now().strftime("%Y%m%d%H%M%S") 时间戳
    # str(uuid.uuid4().hex) uuid
    # fileinfo[-1] 文件后缀名
    filename = datetime.now().strftime("%Y%m%d%H%M%S") + str(uuid.uuid4().hex) + fileinfo[-1]
    return filename


# 确保文件名安全性并添加时间戳
def secure_filename_with_timestamp(filename):
    filename = secure_filename(filename)
    print(filename)
    fileinfo = os.path.splitext(filename)
    filename = fileinfo[0] + "_" + datetime.now().strftime(" %Y%m%d%H%M%S") + fileinfo[-1]
    return filename


# 确保文件名安全性并添加随机uuid
def secure_filename_with_uuid(filename):
    filename = secure_filename(filename)
    fileinfo = os.path.splitext(filename)
    filename = fileinfo[0] + "_" + str(uuid.uuid4().hex)[0:6] + fileinfo[-1]
    return filename

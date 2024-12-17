import os
import paramiko

# 设置SSH连接参数
hostname = '43.143.244.172'
port = 22
username = 'root'
password = '123456'

# 设置本地和远程文件夹路径
local_folder = '/common/'
remote_folder = '/home/'

# 创建SSH客户端
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, port, username, password)

# 创建SFTP客户端
sftp = client.open_sftp()

# 上传文件夹
for dirpath, dirnames, filenames in os.walk(local_folder):
    for filename in filenames:
        local_file_path = os.path.join(dirpath, filename)
        remote_file_path = os.path.join(remote_folder, dirpath.split(local_folder, 1)[1], filename)
        sftp.put(local_file_path, remote_file_path)

# 关闭SFTP和SSH客户端
sftp.close()
client.close()

# upload_file_to_server('testlogin.py','/43.143.244.172/home','root','123456')
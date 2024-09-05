from pathlib import Path
import os
from zipfile import ZipFile
import paramiko
import shutil

from env import Env


def Upload_Images() -> None:
    if not Path("tmp").is_dir():
        os.mkdir("tmp")
    with ZipFile("productimages.zip", "r") as zip_file:
        zip_file.extractall("tmp")
    env = Env()
    files = os.listdir("tmp")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(policy=paramiko.AutoAddPolicy())
    client.connect(hostname=env.SSH_HOST, username=env.SSH_USER, password=env.SSH_PASS)
    sftp = client.open_sftp()
    localPath = os.getcwd() + "/tmp/"
    for file in files:
        picturePath = localPath + file
        savePath = env.FTP_PATH + "/" + file
        sftp.put(localpath=picturePath, remotepath=savePath)
    sftp.close()
    client.close()
    if Path("tmp").is_dir():
        shutil.rmtree("tmp")


def Delete_Images(Server: str, User: str, Pass: str, UploadPath: str) -> None:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(policy=paramiko.AutoAddPolicy())
    client.connect(hostname=Server, username=User, password=Pass)
    client.exec_command(command="rm -rf " + UploadPath + "/*")

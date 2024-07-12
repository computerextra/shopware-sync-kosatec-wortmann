from pathlib import Path
import os
from zipfile import ZipFile
import paramiko
from __config__ import SSH_PASS, SSH_HOST, SSH_USER, FTP_PATH
import shutil


def upload_wortmann_images() -> None:
    if not Path("tmp").is_dir():
        os.mkdir("tmp")
    with ZipFile("productimages.zip", "r") as zip_file:
        zip_file.extractall("tmp")
    files = os.listdir("tmp")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(policy=paramiko.AutoAddPolicy())
    client.connect(hostname=SSH_HOST, username=SSH_USER, password=SSH_PASS)
    sftp = client.open_sftp()
    localPath: str = os.getcwd() + "/tmp/"
    serverPath = FTP_PATH
    for file in files:
        picturePath: str = localPath + file
        savePath = serverPath + "/" + file
        sftp.put(localpath=picturePath, remotepath=savePath)
    sftp.close()
    client.close()
    if Path("tmp").is_dir():
        shutil.rmtree("tmp")
    return


def delete_images_from_ftp() -> None:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(policy=paramiko.AutoAddPolicy())
    client.connect(hostname=SSH_HOST, username=SSH_USER, password=SSH_PASS)
    client.exec_command(command="rm -rf " + FTP_PATH + "/*")
    return

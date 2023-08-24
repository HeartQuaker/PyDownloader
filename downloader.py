from __future__ import annotations
from tqdm import tqdm
import requests
import multitasking
import signal
from retry import retry
from fake_useragent import UserAgent
import sys
import os
from math import *

ua = UserAgent()

signal.signal(signal.SIGINT, multitasking.killall)

MB = 1024**2
 
def split(start: int, end: int, step: int) -> list[tuple[int, int]]:
    parts = [(start, min(start+step, end))
             for start in range(0, end, step)]
    return parts
 
def download_1(url: str, file_name: str):
    headers = {'User-Agent' : ua.random}
    print('正在下载文件......')
    try:
        response = requests.get(url, headers=headers)
        content = response.content
        with open(file_name, mode = 'wb') as f:
            f.write(content)
        print(f'文件{file_name}下载成功！')
    except:
        print('该文件不支持下载！')

def get_file_size(url: str, file_name) -> int:
    response = requests.head(url)
    file_size = response.headers.get('Content-Length')
    if file_size is None:
        print('该文件不支持多线程分段下载！正在启动单线程下载器……')
        download_1(url, file_name)
        os.system('pause')
        sys.exit()
    return int(file_size)
 
 
def download(url: str, file_name: str, retry_times: int = 3, each_size = 16 * MB) -> None:
    f = open(file_name, 'wb')
    file_size = get_file_size(url, file_name)
 
    @retry(tries = retry_times)
    @multitasking.task
    def start_download(start: int, end: int) -> None:
        headers = {'User-Agent' : ua.random}
        _headers = headers.copy()
        _headers['Range'] = f'bytes={start}-{end}'
        response = session.get(url, headers=_headers, stream=True)
        chunk_size = 128
        chunks = []
        for chunk in response.iter_content(chunk_size=chunk_size):
            chunks.append(chunk)
            bar.update(chunk_size / 1024 / 1024)
        f.seek(start)
        for chunk in chunks:
            f.write(chunk)
        del chunks
    session = requests.Session()
    each_size = min(each_size, file_size)
 
    parts = split(0, file_size, each_size)
    print(f'分块数：{len(parts)}')
    bar = tqdm(total=float('%.2f' % (file_size / 1024 / 1024)), desc=f'下载文件：{file_name}', unit = 'MB', dynamic_ncols=True)
    for part in parts:
        start, end = part
        start_download(start, end)
    multitasking.wait_for_tasks()
    f.close()
    bar.close()
 
 
if "__main__" == __name__:
    argvs = sys.argv
    if len(argvs) != 3:
        print('参数传入有误！')
        os.system('pause')
        sys.exit()
    url = argvs[1]
    file_name = argvs[2]
    download(url, file_name)
    os.system('pause')

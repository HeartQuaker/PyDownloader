# PyDownloader
High-speed multi-threaded file downloader implemented in Python.

You can either download downloader.exe for quick access to this feature, or download the source files for further development of your project.

## Introduction

The Python file downloader uses multithreading to download files in chunks. If the file cannot be downloaded in chunks, the downloader will also automatically start the built-in single-threaded high-speed downloader.

## Instructions

Downloading is performed using the command `downloader [url] [filename]`, where `url` refers to the link to the file you want to download and `filename` refers to the name of the file to save. The file is automatically downloaded to the location indicated by `filename`. If `filename` does not specify an absolute path, the file will be installed in the directory where the downloader is located.

Example: `downloader https://nchc.dl.sourceforge.net/project/orwelldevcpp/Setup%20Releases/Dev-Cpp%205.11%20TDM-GCC%204.9.2%20Setup.exe D. /devcpp-setup.exe` will download the DEV-CPP installation package to the root directory of D drive, named `devcpp-setup.exe`.

---

# Python 文件下载器
Python 实现的高速多线程文件下载器

您可以选择下载 downloader.exe 以快捷地使用此功能，或下载源文件以对项目进行进一步开发。

## 功能简介

Python 文件下载器使用多线程功能实现分块下载文件。若文件不能被分块下载，下载器还会自动启动内置的单线程高速下载工具。

## 操作说明

使用指令 `downloader [url] [filename]` 进行下载，其中 `url` 指想要下载的文件链接，`filename` 指保存的文件名。文件会自动下载到 `filename` 所指示的位置。若 `filename` 未指定绝对路径，文件将安装到下载器所在的目录下。

示例：`downloader https://nchc.dl.sourceforge.net/project/orwelldevcpp/Setup%20Releases/Dev-Cpp%205.11%20TDM-GCC%204.9.2%20Setup.exe D:/devcpp-setup.exe` 会将 DEV-CPP 的安装包下载到 D 盘根目录下，命名为 `devcpp-setup.exe`。

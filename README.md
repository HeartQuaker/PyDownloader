# PyDownloader
High-speed multi-threaded file downloader implemented in Python.

You can either download downloader.exe for quick access to this feature, or download the source files for further development of your project.

## Introduction

The Python file downloader uses multithreading to download files in chunks. If the file cannot be downloaded in chunks, the downloader will also automatically start the built-in single-threaded high-speed downloader.

## Instructions

A download is performed using the command `downloader [url] [filename]`, where `url` refers to the link to the file you want to download and `filename` refers to the name of the file to save. The file is automatically downloaded to a subfolder named `files` in the filename directory.

Example: `downloader https://github.com/HeartQuaker/PyDownloader/edit/main/README.md D:/readme.md` will download the markdown file you are looking at now to the `files` folder in the root directory of your D drive. Name it `readme.md`.

---

# Python 文件下载器
Python 实现的高速多线程文件下载器

您可以选择下载 downloader.exe 以快捷地使用此功能，或下载源文件以对项目进行进一步开发。

## 功能简介

Python 文件下载器使用多线程功能实现分块下载文件。若文件不能被分块下载，下载器还会自动启动内置的单线程高速下载工具。

## 操作说明

使用指令 `downloader [url] [filename]` 进行下载，其中 `url` 指想要下载的文件链接，`filename` 指保存的文件名。文件会自动下载到 filename 目录下的一个名叫 `files` 的子文件夹中。

示例：`downloader https://github.com/HeartQuaker/PyDownloader/edit/main/README.md D:/readme.md` 会将您现在看到的 markdown 文件下载到 D 盘根目录下的 `files` 文件夹，命名为 `readme.md`。

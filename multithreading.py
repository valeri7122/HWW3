from pathlib import Path
import os
import shutil
from threading import Thread
from time import time


images_end = ('JPEG', 'PNG', 'JPG', 'SVG')
video_end = ('AVI', 'MP4', 'MOV', 'MKV')
documents_end = ('DOC', 'DOCX', 'docx', 'TXT', 'PDF', 'XLSX', 'PPTX')
audio_end = ('MP3', 'OGG', 'WAV', 'AMR')
archives_end = ('ZIP', 'RAR', 'TAR')

def dir_craeator():
    if not os.path.exists('images'):
        os.mkdir('images')
    else:
        pass
    if not os.path.exists('video'):
        os.mkdir('video')
    else:
        pass
    if not os.path.exists('documents'):
        os.mkdir('documents')
    else:
        pass
    if not os.path.exists('audio'):
        os.mkdir('audio')
    else:
        pass
    if not os.path.exists('archives'):
        os.mkdir('archives')
    else:
        pass

path = Path(input('Введіть шлях до папки, яку треба опрацювати: '))

def dir_iteration(path):
    if len(os.listdir(path)) > 0:
        main_sort(path)
    else:
        try:
            os.removedirs(path)
        except:
            pass

def file_handler(path):
    file_name_split = path.name.split('.')
    if len(file_name_split) > 1:
        file_end_up = file_name_split[-1].upper()
    if file_end_up in images_end:
        try:
            shutil.move(path, 'images')
        except:
            pass
    elif file_end_up in video_end:
        try:
            shutil.move(path, 'video')
        except:
            pass
    elif file_end_up in documents_end:
        try:
            shutil.move(path, 'documents')
        except:
            pass
    elif file_end_up in audio_end:
        try:
            shutil.move(path, 'audio')
        except:
            pass
    elif file_end_up in archives_end:
        arc_name = path.name[:-4]
        try:
            shutil.unpack_archive(path, os.path.join('archives', arc_name))
            os.remove(path)
        except:
            pass

def main_sort(path):
    for p in path.iterdir():
        if p.is_dir():
            thread1 = Thread(target=dir_iteration, args=(p,))
            thread1.start()
        else:
            thread2 = Thread(target=file_handler, args=(p,))
            thread2.start()

        
if __name__ == '__main__':

    timer = time()
    dir_craeator()
    thread = Thread(target=main_sort, args=(path,))
    thread.start()
    print(time() - timer)
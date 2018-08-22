#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
from PIL import Image
import re
path1 = "C:\\Users\\0145180182\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets\\"
path = 'C:\\Users\\0145180182\\Pictures\\picture\\'

#機能説明：壁紙ファイルを自動で整理する
#
def oldfile(new_path):
    a = 0
    fs2 = []
    list0 = []
    for fpathe, dirs, fs in os.walk(new_path):
        fs2 = [(re.search("[0-9]+", x).group(), x) for x in fs]
        fs2.sort(key=lambda x: int(x[0]))
        list0 = [x[1] for x in fs2]
        print(list0)
        for f in list0:
            a += 1
            newname = new_path + str(a) + ".jpg"
            oldname = os.path.join(fpathe, f)  # 1920*1080だけ残り、他の削除する
            singleimg = Image.open(oldname)
            singleimg.close()
            if singleimg.size != (1920, 1080):  #壁紙フィルタ
                os.remove(oldname)
            else:
                os.rename(oldname, newname)
    return a
#以下の関数を簡単にする
def oldfile2(new_path):
    a = 0
    for fpathe, dirs, fs in os.walk(new_path):
        for f in fs:
            a += 1
    return a


def newfile(old_path, new_path, number):
    Sum = 0
    for fpathe, dirs, fs in os.walk(old_path):
        for f in fs:
            if os.path.getsize(os.path.join(fpathe, f)) > 204800:
                newname = new_path + str(a) + ".jpg"
                shutil.copy(os.path.join(fpathe, f), newname)
                singleimg = Image.open(newname)
                singleimg.close()
                if singleimg.size == (1920, 1080):
                    Sum += 1
                    number += 1
                else:
                    os.remove(newname)
    return Sum


if (__name__ == '__main__'):
    a = oldfile2(path)
    print("もう保存したファイルの数量は%d" % a)
    Sum = newfile(path1, path, a)
    print("今回増加ファイル数量は%d" % Sum)

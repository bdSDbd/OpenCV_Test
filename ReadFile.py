import os
import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('test_Form')
root.geometry('200x200')


def GetFilePath():  # return String
    src = filedialog.askopenfilename()


def show():
    file_path = filedialog.askopenfilename()  # 選擇檔案後回傳檔案路徑與名稱
    read_file = cv2.imread(file_path)
    cv2.resize(read_file, (1024, 1024), interpolation=cv2.INTER_AREA)
    cv2.imshow("read_pic", read_file)
    print(file_path)  # 印出路徑

    return file_path


# Button 設定 command 參數，點擊按鈕時執行 show 函式
btn_LoadFile = tk.Button(root,
                         text='開啟檔案',
                         font=('Arial', 20, 'bold'),
                         command=show
                         )

btn_LoadFile.pack()

root.mainloop()

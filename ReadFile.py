import os
import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.title('test_Form')
root.geometry('200x200')


def show():
    file_path = filedialog.askopenfilename(parent = root,
                                           filetypes = (
                                               ("Bitmap Image", "*.bmp"),
                                               ("jpeg files", "*.jpeg"),
                                               ("jpg files", "*.jpg"),
                                               ("all files", "*.*")
                                           ))  # 選擇檔案後回傳檔案路徑與名稱
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("output", 1024, 1024)
    img = cv2.imread(file_path)
    cv2.imshow("output", img)
    print(file_path)  # 印出路徑

    return file_path


def ReadFile():  # 顯示檔案選擇器後開啟影像
    btn_LoadFile = tk.Button(root,  # Button 設定 command 參數，點擊按鈕時執行 show 函式
                             text='開啟檔案',
                             font=('Arial', 20, 'bold'),
                             command=show
                             )
    btn_LoadFile.pack()
    root.mainloop()
    return show()

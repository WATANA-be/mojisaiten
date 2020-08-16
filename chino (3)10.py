import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk
import random

# 機械学習で使うモジュール
import sklearn.datasets
import sklearn.svm
import numpy

# 画像ファイルを数値リストに変換
def imageToData(filename):
    #画像を8x8のグレースケールに変換
    grayImage = PIL.Image.open(filename).convert('L')
    grayImage = grayImage.resize((8,8),PIL.Image.ANTIALIAS)
    #その画像を表示
    dispImage = PIL.ImageTk.PhotoImage(grayImage.resize((300,300)))
    imageLabel.configure(image = dispImage)
    imageLabel.image = dispImage
    #数値をリストに変換
    numImage = numpy.asarray(grayImage,dtype = float)
    numImage = numpy.floor(16 - 16 * (numImage / 256))
    numImage = numImage.flatten()
    return numImage
    #　数値予測
def predictDigits(data):
    #学習用データ読み込み
    digits = sklearn.datasets.load_digits()
    #機械学習する
    clf = sklearn.svm.SVC(gamma = 0.001)
    clf.fit(digits.data, digits.target)
    #予測結果を表示
    n = clf.predict([data])
    textLabel.configure(text = 'この画像は'+str(n)+'です！')

# ファイルダイアログを開く
def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        #　画像ファイルを数値リストに変換
        data = imageToData(fpath)
        #数値を予測
        predictDigits(data)


def dispLabel():
    point = ['0','10','20','30','50','70','80','90','99','100','絶句']
    tk.lbl2(text=u"採点結果は"+str(point)+'点です。')

# アプリのウィンドウ作成
root = tk.Tk()
root.geometry('600x500')

btn = tk.Button(root, text='ファイルを開く', command = openFile,font=('Helvetica',40))
imageLabel = tk.Label()
btn.pack()

btn2 = tk.Button(root,text='ここから採点',command = dispLabel)
btn2.pack()

#予測結果の表示ラベル
textLabel = tk.Label(text='手書きの数字を認識しますね')
textLabel.pack()


textLabel2 = tk.Label(text='採点します')
textLabel2.pack()

tk.mainloop()
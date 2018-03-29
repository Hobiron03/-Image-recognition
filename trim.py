# -*- coding:utf-8 -*-
import cv2
import os
import sys

def facedetect(file):

    """画像を受け取り顔部分をトリミングしてディレクトリに保存"""
    i = 0
    #トリミング後の保存先ファイル
    file_name = "save_path"
    #カスケードファイルのパス(アニメ顔)
    #cascade_path = "lbpcascade_animeface.xml"
    #リアルの人間の顔
    cascade_path = "haarcascade_frontalface_alt2.xml"
    #cascade_path = "haarcascade_frontalface_default.xml"
    #ファイル読み込み
    name = str(file)
    image = cv2.imread(file)
    if(image is None):
    	print ('画像を開けません。')
    	quit()

    #グレースケール変換
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #カスケード分類器の特徴量を取得する
    cascade = cv2.CascadeClassifier(cascade_path)
    #物体認識（顔認識）の実行
    #facerect = cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=1, minSize=(50, 50))
    facerect = cascade.detectMultiScale(image_gray, 1.1, 5, minSize=(1,1))

    print ("face rectangle")
    print (facerect)
    print(name)

    if len(facerect) > 0:
        if not os.path.exists(file_name):
            os.mkdir(file_name)

    for rect in facerect:
        #顔だけ切り出して保存
        x = rect[0]
        y = rect[1]
        width = rect[2]
        height = rect[3]
        dst = image[y:y+height, x:x+width]
        num = len(os.listdir(file_name)) + 1
        new_image_path = file_name + '/' + "image_" + str(num) + ".jpg"
        cv2.imwrite(new_image_path, dst)

if __name__ == "__main__":
    #学習する画像が保存されているディレクトリのパス
    image_file_path = "iamge_path"
    if os.path.exists(image_file_path):
        images = os.listdir(image_file_path)
        images.pop(0)
        for image in images:
            image_path = "image_path" + image
            facedetect(image_path)
    else:
        print("no directory")

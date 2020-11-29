#####################################################
#
# 課題は，※印のコメントの部分についての処理を書く．
# アドバンスのモザイクをする場合は， 
# モザイク用の部分のコメントを外して，処理を書く．
#
#####################################################
import cv2
import numpy as np
from PIL import Image

dir = 'C:\\opencv\\build\\etc\\haarcascades\\' #パラメーターフォルダ
cascade_path = dir + 'haarcascade_frontalface_alt.xml' #顔認識用パラメーター
#カスケード分類器の特徴量を取得
cascade = #※特徴量の取得
cap = cv2.VideoCapture(0) # 0はカメラのデバイス番号

#※ 枠の色の設定（色の設定は各自で決める）
color = (???, ???, ???) #※色の設定はBGRの順

while True:
    # retは画像の取得成功フラグ
    ret, image = cap.read()
    #下記の処理はアドバンスのモザイク用．課題では不要
    #img = Image.fromarray(image[:, :, : :-1]) #PIL形式に変換 BGR->RGB

    # グレースケール変換（顔認識用）
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 分類器を用いて顔検出を行う
    facerect = #※分類器による顔検出
    if len(facerect) > 0:
        # 検出した顔を加工（四角枠の描画もしくはモザイク化）
        for rect in facerect:
            #※四角枠の描画
            #下記の処理はアドバンスのモザイク用．課題では不要
            #face = 顔だけ切り取り
            #face = 1/10サイズに圧縮
            #face = 元の大きさに戻せばモザイク画像の完成
            #img.paste モザイク画像を元の画像の切り取った場所に貼り付ける

    else:
        print("no face")

    #下記の処理はアドバンスのモザイク用．課題では不要
    #frame_cv = np.asarray(img) #OpenCV形式に変換
    #image = frame_cv[:, :, : :-1] #RGB->BGR

    # フレームを表示する
    cv2.imshow("Face", image)

    key = cv2.waitKey(1) # 1m秒待つ
    if key == 27: # ESCキーで終了
        break
        
# キャプチャを解放する
cap.release()
cv2.destroyAllWindows()

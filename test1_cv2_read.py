import cv2
import numpy as np

#画像読み込む
img = cv2.imread("image1.jpg")

#グレースケールに変換
gray = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)

#結果を出力
cv2.imshow("gray", gray)

while True:
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()




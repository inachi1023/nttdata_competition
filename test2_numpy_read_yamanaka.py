# -*- coding: utf-8 -*-
# 画像処理に使用するモジュールをインポート
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import glob


def plot_img(image1, image2):
    # 画像読み込む(グレースケール(白黒写真)として読み込み)
    img1 = np.array(Image.open(image1).convert('L'))  # 変化前の画像
    img2 = np.array(Image.open(image2).convert('L'))  # 変化後の画像(ライトが消えた)

    # plt.imshow(img1)
    # plt.imshow(img2)

    # plt.show()

    # 配列に格納された値の総和を算出
    arr_sum1 = img1.sum()  # 変化前
    arr_sum2 = img2.sum()  # 変化後

    # 配列を表示してみる
    # np.set_printoptions(threshold=np.inf) # 配列を省略せず表示するにはコメント外す。
    # print(arr_sum1)
    # print(arr_sum2)

    # ndarrayの形状（shape）をタプルで表したもの
    print(img1.shape)
    print(img2.shape)

    # 総和を表示
    print(arr_sum1)
    print(arr_sum2)

    # 差分を計算
    arr_difference = arr_sum1 - arr_sum2

    # 値がデカすぎるので調整
    arr_difference_param = arr_difference / 1000000000
    print(arr_difference)

    # ファイル出力保存
    img_gray1 = Image.fromarray(img1)
    img_gray1.save('sample1_gray.jpg')
    img_gray2 = Image.fromarray(img2)
    img_gray2.save('sample2_gray.jpg')

    # プロットしてみる
    plt.title("economy to light")
    plt.xlabel("light of difference")
    plt.ylabel("Economic impact ")

    x = [arr_difference_param]  # 夜間照明の差
    y = [1.2]  # 経済影響(GDPとか)　※今回はテキトーに1.2%下がったとか

    # x = np.random.rand(100)
    # y = np.random.rand(100)

    plt.scatter(x, y)

    plt.savefig("plot_result.png")
    # plt.show()

    '''いろんな夜間照明画像突っ込んでみてプロットしてみると相関関係見えるかーと思った'''


# 写真を設定
files = sorted(glob.glob('night_image/*'))

for i in range(len(files) - 1):
    night_img1 = files[i]
    night_img2 = files[i + 1]

    plot_img(night_img1, night_img2)


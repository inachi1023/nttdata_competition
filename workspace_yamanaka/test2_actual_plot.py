# -*- coding: utf-8 -*-
# 画像処理に使用するモジュールをインポート
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def read_light(yyyy, light):
    """夜間光取得メソッド"""

    # 写真(夜間光)を設定
    image = 'night_image/' + yyyy + '.jpg'

    # 画像読み込む(グレースケール(白黒写真)として読み込み)
    gray = np.array(Image.open(image).convert('L'))

    # 配列に格納された値の総和を算出
    # (デフォルト(uint64)では演算が正しくできないため、dtype指定)
    sum_gray = gray.sum(dtype=int)  # 変化前

    # 夜間照明を設定
    light.append(sum_gray)

    # 光度をコンソールに表示
    print('光度: ' + str(sum_gray))


def read_economy(yyyy, economy):
    """経済指標取得メソッド"""

    # CSV(経済指標)を設定
    index = pd.read_csv('economy_index/GDP.csv')[yyyy][0]

    # 指標を設定
    economy.append(index)

    # CSVの指標をコンソールに表示
    print('指標: ' + str(index))


"""メインメソッド"""

x = []  # プロット_x軸
y = []  # プロット_y軸

years = range(1992, 2013)  # 1992年から2013年まで

for year in years:
    year_str = str(year)

    # CSVの指標をコンソールに表示
    print('')
    print('西暦: ' + year_str)

    # 夜間光取得
    read_light(year_str, x)

    # 経済指標取得
    read_economy(year_str, y)


# タイトル、軸名設定
plt.title("economy to light")
plt.xlabel("light")
plt.ylabel("Economic impact ")

# 値をプロットする
plt.scatter(x, y)
plt.savefig("result_actual_plot.png")

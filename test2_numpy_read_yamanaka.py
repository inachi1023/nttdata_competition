# -*- coding: utf-8 -*-
# 画像処理に使用するモジュールをインポート
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def read_light_diff(image_before, image_after, light_diff):
    """夜間光差分取得メソッド"""

    # 画像読み込む(グレースケール(白黒写真)として読み込み)
    gray_before = np.array(Image.open(image_before).convert('L'))  # 変化前の画像
    gray_after = np.array(Image.open(image_after).convert('L'))  # 変化後の画像

    # 配列に格納された値の総和を算出
    # (デフォルト(uint64)では演算が正しくできないため、dtype指定)
    sum_before = gray_before.sum(dtype=int)  # 変化前
    sum_after = gray_after.sum(dtype=int)  # 変化後

    # 差分を計算
    difference_sum_gray = sum_after - sum_before + 3000000
    print(difference_sum_gray)

    # 夜間照明の差を設定
    light_diff.append(difference_sum_gray)


def read_economy_diff(value1, value2, economy_diff):
    """経済指標差分取得メソッド"""

    # 差分を計算
    val_difference_param = value1 - value2

    # 経済指標の差を設定
    economy_diff.append(val_difference_param)


"""メインメソッド"""

x = []  # プロット_x軸
y = []  # プロット_y軸

years = range(1992, 2013)  # 1992年から2013年まで

for year in years:
    before_year = str(year)
    after_year = str(year + 1)
    print(before_year)

    # 写真(夜間光)を設定
    night_img_before = 'night_image/' + before_year + '.jpg'
    night_img_after = 'night_image/' + after_year + '.jpg'

    # 夜間光差分取得
    read_light_diff(night_img_before, night_img_after, x)

    # CSV(経済指標)を設定
    economy_index_before = pd.read_csv('economy_index/GDP.csv')[before_year][0]
    economy_index_after = pd.read_csv('economy_index/GDP.csv')[after_year][0]

    # 経済指標差分取得
    read_economy_diff(economy_index_before, economy_index_after, y)


# タイトル、軸名設定
plt.title("economy to light")
plt.xlabel("light of difference")
plt.ylabel("Economic impact ")

# 値をプロットする
plt.scatter(x, y)
plt.savefig("plot_result_yamanaka.png")

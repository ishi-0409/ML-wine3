
# 概要
UCIのWine Qualityのデータセット（赤ワイン）を用いて、説明変数それぞれの回帰係数と切片を求める

# 使用データ

データの出典([https://archive.ics.uci.edu/dataset/186/wine+quality])

データの形式(CSV,区切り文字;)

# 環境、依存ライブラリ
python(3.12.9),pandas,scikit-learn

# データの理解
ワインの質(quality)を目的変数fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,
total_sulfur_dioxide,density,pH,sulphates,alcoholを説明変数とする。

説明変数、目的変数はともに量的データ

データは全部で1599件,種類は1359件

# データの前処理
欠損値はない

# モデルの構築
scikit-learnのlinear_modelモジュールからLinearRegressionクラスをインポートし、線形回帰モデルを作成する
説明変数が複数あるため重回帰分析

# モデルの評価
最小二乗法によって切片と回帰係数が推定される  
切片: 21.965208449448582  
係数: [ 2.49905527e-02 -1.08359026e+00 -1.82563948e-01  1.63312698e-02
 -1.87422516e+00  4.36133331e-03 -3.26457970e-03 -1.78811638e+01       
 -4.13653144e-01  9.16334413e-01  2.76197699e-01]
 





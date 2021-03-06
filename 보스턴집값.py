# -*- coding: utf-8 -*-
"""보스턴집값.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ecdeNfZOxU6EHtR-A5dGrUo9ki4sq4gW

보스턴 집값 예측
github csv url : https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv
"""

# 라이브러리 사용
import tensorflow as tf
import pandas as pd

# 1. 과거의 데이터를 준비합니다.
파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'
보스턴 = pd.read_csv(파일경로)
print(보스턴.columns)
보스턴.head()

# 독립변수, 종속변수
독립 = 보스턴[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax',
       'ptratio', 'b', 'lstat']]
종속 = 보스턴[['medv']]
print(독립.shape, 종속.shape)

# 모델의 구조를 만듭니다
X = tf.keras.layers.Input(shape=[13])
Y = tf.keras.layers.Dense(1)(X)
model = tf.keras.models.Model(X,Y)
model.compile(loss='mse')

# 데이터로 모델을 학습(FIT)합니다.
model.fit(독립, 종속, epochs=1000, verbose= 0)
model.fit(독립, 종속, epochs=10)

# 모델을 이용합니다.
model.predict(독립[0:5])

종속[0:5]

# 모델의 수식 확인
model.get_weights()

집값 = -0.088217 * x1 + 0.07502375 * x2 + -0.06276634 * x3 +
 3.39031 * x4 + 2.406157 * x5 + 3.8978293 * x6 + 
 0.01440577 * x7 + -0.9008312 * x8 + 0.14697045 * x9 +
  -0.00975282 * x10 + 0.02125786 * x11 + 0.0147361 * x12 + -0.58878493 * x13 + 2.8826687
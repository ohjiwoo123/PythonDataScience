# -*- coding: utf-8 -*-
"""레모네이드.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11BpT9lR5FBkux62R6fXSaVSWl5Mlz_h1
"""

# 라이브러리 사용
import tensorflow as tf
import pandas as pd

# 데이터 준비 
파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
데이터 = pd.read_csv(파일경로)
데이터.head()

# 종속변수, 독립변수
독립 = 데이터[['온도']]
종속 = 데이터[['판매량']]
print(독립.shape, 종속.shape)

# 모델을 만듭니다.
X = tf.keras.layers.Input(shape=[1])
Y = tf.keras.layers.Dense(1)(X)
model = tf.keras.models.Model(X,Y)
model.compile(loss='mse')

# 모델을 학습합니다.
model.fit(독립, 종속, epochs=1000, verbose=0)

# 모델을 이용합니다.
model.predict(독립)

model.predict([[15]])
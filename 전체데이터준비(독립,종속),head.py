# -*- coding: utf-8 -*-
"""전체데이터준비(독립,종속),head.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jMTZg4wGP2P75xTnCMUeEESN5KdjEdhV

데이터 준비하기 1
데이터를 불러온다
종속변수와 독립변수로 분리한다.
실습을 통해 배울 도구들

파일 읽어오기: read_csv('/경로/파일명.csv')
모양 확인하기: 데이터.shape
칼럼 선택하기: 데이터[['칼럼명1', '칼럼명2', '칼럼명3']]
칼럼 이름 출력하기: 데이터.columns
맨 위 5개 관측치 출력하기: 데이터.head()
샘플 데이터

GitHub github link: https://github.com/blackdew/tensorflow1/tree/master/csv
레모네이드: https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv
보스톤: https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv
아이리스: https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv
"""

import pandas as pd

# 파일로부터 데이터 읽어오기
파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/lemonade.csv'
레모네이드 = pd.read_csv(파일경로)

파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'
보스톤 = pd.read_csv(파일경로)

파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
아이리스 = pd.read_csv(파일경로)

# 데이터 모양으로 확인하기
print(레모네이드.shape)
print(보스톤.shape)
print(아이리스.shape)

# 칼럼이름 출력
print(레모네이드.columns)
print(보스톤.columns)
print(아이리스.columns)

독립 = 레모네이드[['온도']]
종속 = 레모네이드[['판매량']]
print(독립.shape, 종속.shape)

독립 = 보스톤[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax',
       'ptratio', 'b', 'lstat', 'medv']]
종속 = 보스톤[['medv']]
print(독립.shape, 종속.shape)

독립 = 아이리스[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
종속 = 아이리스[['품종']]
print(독립.shape, 종속.shape)

레모네이드.head()

보스톤.head()

아이리스.head()
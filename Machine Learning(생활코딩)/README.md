# [생활코딩 머신러닝 1기](https://ml.yah.ac/)

### 🔘  수업소개 :
    - 코드로 딥러닝을 구현해보는 딥러닝 기초 수업 

    - 텐서플로우를 이용하여 가장 간단한 형태의 텐서플로우 딥러닝 모델을 작성


### 🔘  케라스를 이용한 모델 작성
    1. 독립변수와 종속변수로 사용할 데이터를 준비한다.  
        - 독립변수 : 하나의 결과를 관찰하기 위해 실험적으로 조작되거나 혹은 통제된 변수, 즉 영향을 주는 변수
        
        - 종속변수 : 독립변수에 영향을 받아 값이 달라지는 변수, 즉 영향을 받는 변수
            
```python
boston_path = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'; // 사용할 데이터
boston_data = pd.read_csv(boston_path)

boston_inV = boston_data[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax','ptratio', 'b', 'lstat']] //독립변수
boston_deV = boston_data[['medv']]     //종속변수 
```
<br/>

    2. 모델의 구조를 작성한다.

```python
X = tf.keras.layers.Input(shape=[13]) // shape=[13] 모델에 적용할 독립변수의 수
Y = tf.keras.layers.Dense(1)(X)       // X개를 입력 받아 1개의 결과 
model = tf.keras.models.Model(X,Y)
model.compile(loss='mse') // lose는 손실 함수       
```
---
```python
// 입력과 결과 사이에 히든 레이어를 추가한 멀티레이터 신경망
X = tf.keras.layers.Input(shape=[13])
H = tf.keras.layers.Dense(10, activation='swish')(X)  // activation은 활성화 함수
Y = tf.keras.layers.Dense(1)(H)
model = tf.keras.models.Model(X,Y)
model.compile(loss='mse')
```
<br/>

    3. 데이터로 모델을 학습(FIT)시킨다.

```python
model.fit(독립변수, 종속변수, epochs=1000, verbose=0)
```
<br/>

    4. 모델을 활용하여 결과를 예측한다.
```
model.predict(예측할 데이터)
```
<br/>

### 🔘  어려웠던점 및 느낀점

    - 모델 작성시 케라스를 활용하여 모델을 만들 때 어떤 것을 종속변수로 잡을지 독립변수로 잡을지 결정하기가 쉽지 않겠다라고 느꼈다.
    


![머신야학 수료증](https://github.com/dongy094/ETC/blob/master/Machine%20Learning(%EC%83%9D%ED%99%9C%EC%BD%94%EB%94%A9)/%EB%A8%B8%EC%8B%A0%EC%95%BC%ED%95%99.JPG?raw=false)



### 출처 : [생활코딩](https://www.opentutorials.org/module/4966), https://blog.naver.com/yk60park/221551280577

# -*- coding: utf-8 -*-
"""laba6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cEq5F8ss9bKUtJYvgyEazydEZbPSkUKE
"""

from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib import pyplot as plt


fahrenheit = [[-67.0], [-34.0], [0], [34.0], [54.0], [67.0], [100]]
kelvin = [[(f[0] - 32) * 5 / 9 + 273.15] for f in fahrenheit]


plt.figure(figsize=(15, 8), dpi=50)
plt.scatter(fahrenheit, kelvin, label='Исходные значения', color='green', marker='$f$')
plt.xlabel('Fahrenheit')
plt.ylabel('Kelvin')
plt.legend()
plt.grid(True)
plt.show()

for c, k in zip(fahrenheit, kelvin):
    print(f'Фаренгейт {c[0]} = Кельвин {k[0]}')

lr = LinearRegression()
lr.fit(fahrenheit, kelvin)
kelvin_predictions = lr.predict([[256], [123]])

print("Коэффициент наклона (slope):", lr.coef_[0][0])
print("Пересечение с осью (intercept):", lr.intercept_[0])

fahrenheit_test = [[-50], [10], [30], [20], [10], [70], [87]]
kelvin_test = lr.predict(fahrenheit_test)

for c, k in zip(fahrenheit_test, kelvin_test):
    print(f'Фаренгейт {c[0]} предсказанное Кельвин {k[0]}')

x_range = np.arange(-70, 120)
y_range = (x_range - 32) * 5 / 9 + 273.15

plt.figure(figsize=(15, 8), dpi=280)
plt.plot(x_range, y_range, label='Уравнение перевода', linewidth=1)
plt.scatter(fahrenheit, kelvin, label='Исходные данные', color='green')
plt.scatter(fahrenheit_test, kelvin_test, label='Предсказанные значения', color='blue')
plt.xlabel('Fahrenheit')
plt.ylabel('Kelvin')
plt.legend()
plt.grid(True)
plt.show()

!apt-get install git

!git clone https://github.com/warhogz/Proj_1sem_Khsasaev.git

import os
os.chdir('Proj_1sem_Khsasaev/PZ_10')

import PZ_10_1

print(dir(PZ_10_1))

import numpy as np
from matplotlib import pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF

plt.style.use('_mpl-gallery')

x = 0.5 + np.arange(8)
y = [2.3, 4.0, 3.8, 5.0, 7.2, 4.9, 2.2, 3.7]

fig, ax = plt.subplots()
ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set(xlim=(0, 8), xticks=np.arange(1, 9),
       ylim=(0, 8), yticks=np.arange(1, 9))
plt.show()

y = [3.2, 4.1, 5.5, 2.7, 6.0, 5.5, 3.0, 4.5]

fig, ax = plt.subplots()
ax.stairs(y, linewidth=2.5)

ax.set(xlim=(0, 8), xticks=np.arange(1, 9),
       ylim=(0, 8), yticks=np.arange(1, 9))
plt.show()

np.random.seed(1)
x = 5 + np.random.normal(0, 1.2, 200)

ecdf = ECDF(x)
fig, ax = plt.subplots()
ax.plot(ecdf.x, ecdf.y, marker='.', linestyle='none')

ax.set(xlim=(0, 10), ylim=(0, 1.1))
plt.show()

import math

number = 19
memory = 128

print("1. Число Эйлера =", math.e)
print("2. Число Пи =", math.pi)
print("3. Значение nan =", math.nan)
print("4. Факториал числа", number, "=", math.factorial(number))
print("5. Наибольший общий делитель чисел", number, "и", memory, "=", math.gcd(number, memory))

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
import matplotlib.pyplot as plt
import numpy as np

cifar10 = tf.keras.datasets.cifar10
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

class_names = ['Самолет', 'Автомобиль', 'Птица', 'Кошка', 'Олень',
               'Собака', 'Лягушка', 'Лошадь', 'Корабль', 'Грузовик']

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train[i])
    plt.xlabel(class_names[y_train[i][0]])
plt.show()

x_train, x_test = x_train / 255.0, x_test / 255.0

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10)

test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print('\nТочность модели на тестовых данных:', test_acc)

predictions = model.predict(x_test)

plt.figure(figsize=(10,10))
for i in range(15):
    plt.subplot(3,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_test[i])
    plt.xlabel(f"Верно: {class_names[y_test[i][0]]}\nПредсказано: {class_names[np.argmax(predictions[i])]}")
plt.show()
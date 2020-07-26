# fris-stolp
Алгоритм FRiS-СТОЛП (FRiS-STOLP) - алгоритм отбора эталонных объектов для метрического классификатора на основе FRiS-функции.

Полное описание алгоритма можно найти [здесь]( http://www.machinelearning.ru/wiki/index.php?title=%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_FRiS-%D0%A1%D0%A2%D0%9E%D0%9B%D0%9F)

###### Пример FRiS-СТОЛП находит эталоны (большие круги), имея выборку - маленькие круги
![](https://raw.githubusercontent.com/okiochan/fris-stolp/master/pic1.png)
![](https://raw.githubusercontent.com/okiochan/fris-stolp/master/pic2.png)

# Классификация с Fris-function
Функция конкурентного сходства или FRiS-функция – мера сходства двух объектов, исчисляемая относительно некоторого иного объекта.

На рисунке ниже приведён пример случая, когда FRiS функция, как мера сходства, работает лучше, чем KNN
На данной выборке знак вопроса должен быть отнесен к плюсикам
<figure>
  <img src="https://raw.githubusercontent.com/okiochan/fris-stolp/master/FRiS.jpg" alt="uniform"/>
</figure>

Вот так на данной выборке отработала моя [программа]( https://github.com/okiochan/fris-stolp/blob/master/fris.py)
###### Пример классиф. с Fris-function
<figure>
  <img src="https://raw.githubusercontent.com/okiochan/fris-stolp/master/aider_data1.png" alt="uniform"/>
</figure>

###### Пример классиф. с KNN
<figure>
  <img src="https://raw.githubusercontent.com/okiochan/fris-stolp/master/aider_data2.png" alt="uniform"/>
</figure>

###### Еще примеры классификации с Fris-function
<figure>
  <img src="https://raw.githubusercontent.com/okiochan/fris-stolp/master/Figure_1.png" alt="uniform"/>
  <img src="https://raw.githubusercontent.com/okiochan/fris-stolp/master/Figure_2.png" alt="uniform"/>
  <img src="https://raw.githubusercontent.com/okiochan/fris-stolp/master/Figure_3.png" alt="uniform"/>
</figure>

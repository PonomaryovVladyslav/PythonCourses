# Урок 15. Введение в ООП. Основные парадигмы ООП. Классы и объекты.

![](https:habrastorage.org/files/06e/20d/7b3/06e20d7b37544511b800687df9b2a63e.png)

## Что такое ООП, и что же такое класс и объект.

Объектно-ориентированное программирование (в дальнейшем ООП) — парадигма программирования, в которой основными концепциями являются понятия объектов и классов.

В центре ООП находится понятие объекта.

Класс это шаблон для создания объекта, допустим у нас есть класс автомобиль, автомобиль это класс, а конктретный лексус 2015 года выпуска, это уже объект класса автомобиль.

Объект — это сущность, экземпляр класса, содержащая свои аттрибуты и свои методы.

Аттрибут класса это данные принадлежащие классу, например цвет автомобиля (каждый автомобиль какого-то цвета, но пока у нас нет "экзмпляра" мы не можем сказать какого автомобиль именно цвета)

Метод класса, это функция описанная внутри объекта и описывающая определенное действие, например автомобиль может ехать.

Что такое `self` - `self` это специальный аргумент метода, для получения ссылки на экземпляр объекта.
Селф должен быть первым аргументом метода.

Если у нас есть класс студент, то через селф мы можем получить доступ ко всем атрибутам и методам конктретного студнета, например списку оценок, или методу "прогулять занятие" :)
Доступ к атрибутам и свойствам получается через точку.

Объяснение self в python
- у котов внутри есть мурчалка
- она реализована для всех котов в классе кот
- в объекте кот надо как то вызвать метод мурчало у класса кот
‎- как ты это сделаешь?
- кот.мурчало()
‎- ежели ты вызовешь кот.мурчало(), муркнут сразу все коты на свете
‎- а ежели ты вызовешь self.мурчало(), муркнет только тот кот, на которого указывает self

Пример кода:

```python
class Car:
    color = 'red'
    top_speed = 250
    
    def find_color_and_top_speed(self):
        return 'this car top speed is {} and color is {}'.format(self.top_speed, self.color)

    def is_car_can_go_with_needed_speed(self, speed):
        return speed < self.top_speed

lamborgini = Car()
print(lamborgini.find_color_and_top_speed())
print(lamborgini.is_car_can_go_with_needed_speed(200))
cherry = Car()
print(cherry.find_color_and_top_speed())
cherry.top_speed = 140
cherry.color = 'yellow'
cherry.some_new_attribute = 33 # Можно добавлять атрибуты к любому объекту если это необходимо
print(cherry.is_car_can_go_with_needed_speed(200))
print(cherry.find_color_and_top_speed())
```

## Парадигмы ООП

ООП держится на трёх основных и одной второстепенной парадигме.

Основные:

### Инкапсуляция

`Инкапсуляция` - Принцип скрытия функционала или данных, предоставляя только вход и выход, например в автомобиле если повернуть руль налево, то колёса тоже повернутся налево, но как именно это происходит от нас скрыто, мы не знаем какие именно рычаги и шестерёнки в этот момент двигаются внутри автомобиля.

В языке програмирования python инкапсуляция является довольно таки условной, для того, что бы скрыть данные для внешнего испольвания нужно называть аттрибуты или методы начиная с нижнего подчёркивания `_` одинарное подчёркиваение вызовет предупреждение о том что элемент скрыт, два подчеркивания не позволят получить доступ к этому атрибуту из вне (хотя и есть способы).

В первую очеред код пишется для людей, по этому инкапсуляция все таки условная (именно в питоне, в большинстве других языков это строго ограничено)

#### Пример кода

```python
class Car:
    color = 'red'
    _top_speed = 250
    __max_carrying = 1000
    def find_color_and_top_speed(self):
        return 'this car top speed is {} and color is {}'.format(self._top_speed, self.color)

    def is_can_go_with_needed_speed(self, speed):
        return speed < self._top_speed

    def is_can_get_weight(self, weight):
        return self.__max_carrying > weight

    def change_max_carrying(self, new_carrying):
        self.__max_carrying = new_carrying

    def __hidden_method(self):
        print('this is hidden method')

    def _this_is_protected_method(self):
        print('this is protected method')

    def run_hidden_and_protected_methods(self):
        self.__hidden_method()
        self._this_is_protected_method()

car = Car()
car.color # всё нормально
car._top_speed # сработает, но с предупреждением
car.__max_carrying # не сработает
car.__max_carrying = 800 # не сработает
car.chacnge_max_carrying(800) # сработает
сar.__hidden_method() # не сработает
car._this_is_protected_method() # сработает c предупреждением
car.run_hidden_and_protected_methods() # сработает
```
 
### Наследование

`Наследование` — это свойство системы, позволяющее описать новый класс на основе уже существующего с частично или полностью заимствующейся функциональностью. Класс, от которого производится наследование, называется базовым, родительским или суперклассом. Новый класс — потомком, наследником или производным классом

Например у нас есть базовый класс автомобиль и три наследника, легковой, самосвал и фура, все три класса могут иметь общие атрибуты, например двигатель или материал лобового стекла, или методы, например газ и торомоз, но при этом иметь свои обенные атрибуты или методы, например, только у фуры будет больше чем 4 колеса, или у самосвала, будет метод поднять кузов, или у фуры отцепить груз.

#### Пример кода

```python
class Car:
    wheels = 4
    doors = 4
    curent_speed = 0
    max_speed = 200
    def go(self):
        self.curent_speed = self.max_speed/2
    
    def stop(self):
        self.curent_speed = 0

class Track(Car):
    doors = 2
    max_speed = 120

class SportCar(Car):
    max_speed = 350

track = Track()
sport = SportCar()

track.go()
sport.go()
print(track.curent_speed) # 60
print(sport.curent_speed) # 175
```
### Полиморфизм

Полиморфизм — это свойство системы использовать объекты с одинаковым интерфейсом без информации о типе и внутренней структуре объекта.

По сути это возможность использовать одни и теже методы или интрефесы к различным структурам, например обычный знак `+`, ведь мы можем сложить числа, а можем и строки, и получим разный результат, но применим один и тот же метод.


```python
class English:
    
    def greeting(self):       
        print ("Hello")
        
        
class French:
    
    def greeting(self):
        print ("Bonjour")
  
  
def intro(language):               
    
    language.greeting()
    
    
flora  = English()
aalase = French()   
 
 
intro(flora)
intro(aalase)
```

### Абстракция

Не самый обязательный пункт но знать о его существовании обычно нужно, это абстракция.

Абстракция это предварительное описание без реализации (заготовка для будущего метода)

```python
# Абстрактный класс (Abstract class).
class AbstractDocument :
     
    def __init__(self, name):
         
        self.name = name
         
    # Метод невозможно использовать, так как всегда выбрасывает ошибку.
    def show(self):
        # это абстракция
        raise NotImplementedError("Subclass must implement abstract method")    
     
 
class PDF(AbstractDocument):
     
    # Переопределить метод родительского класса
    def show(self):
        print ("Show PDF document:", self.name)
         
         
class Word(AbstractDocument):     
     
    def show(self):
        print ("Show Word document:", self.name)
 
# ----------------------------------------------------------
documents = [ PDF("Python tutorial"),
              Word("Java IO Tutorial"),
              PDF("Python Date & Time Tutorial") ]     
 
 
for doc in documents :
     
    doc.show()
``` 
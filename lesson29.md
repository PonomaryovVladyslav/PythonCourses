# Декораторы классов @staticmethod @classmethod @property


## Декоратор @classmethod

В этот декоратор есть смысл оборачивать методы, которые работают с атрибутами-данных и другими методами класса,
которые не зависят от экземляра (instance). Методы с `@classmethod` работают на уровне класса,
именно поэтому для первого аргумента используют `cls` давая понять разработчику, что имеется доступ только
для атрибутов класса, а не конкретному экземпляру после выполнения  `__init__`.

```python
class MyClass:
    class_attr = "class_attr"
    
    def __init__(self):
        self.instance_attr = "instance_attr"

    @classmethod  # применение декоратора
    # конвенция имени cls даёт понять, что работаем непосредственно с классом
    def my_class_method(cls):
        print(cls.class_attr)
        # print(cls.instance_attr)  # доступа к атрибутам экземпляра не будет

    # При этом у обычного метода есть доступ по всем атрибутам
    def my_method(self):
        print(self.class_attr)
        print(self.instance_attr)

# При этом для работы методов класса создание instance является не обязательно
MyClass.my_class_method()
# Даже если экземпляр создан, метод все равно будет работать
MyClass().my_class_method()
# Для работы обычного метода создание экземпляра обязательно!!!
# MyClass.my_method()  # приведёт к ошибки
MyClass().my_method()
```

## Декоратор @staticmethod
Этот декоратор нужно оборачивать методы, которые по логике тесно связаны с классом,
но для работы которых не нужны не `cls`, не `self`.
> P.S. По-сути такие методы можно вынести из класса в утилиты, и они не нарушат своей работоспособности.

Главное, что держит этот метод в классе, `смысловая связь с самим классом`.
```python
class MyClass:
    @staticmethod
    def my_static_method(*args, **kwargs):
        # logic
        pass

# Статический метод работает независимо создан экземпляр класса или нет
MyClass.my_static_method()
MyClass().my_static_method()
```

## Декоратор @property

Это питонический подход к созданию `getter`, `setter`, `deleter` для атрибутов экземпляра класса.

`Getter` - метод, для `получения` атрибута-данных, доступ к которому напрямую ограничен.

`Setter` - метод, для `установки` атрибута-данных, доступ к которому напрямую ограничен.

`Deleter` - метод, для `удаления` текущего значения атрибута-данных.
Вызывается при вызове `del` на атрибут экземпляра класса.

```python
class MyClass:
    def __init__(self):
        self.__my_attr = "Initial Data"

    @property
    def my_test(self):
        print("getter called")
        return self.__my_attr

    @my_test.setter
    def my_test(self, value):
        print("setter called")
        self.__my_attr = f"extra logic {value}"

    @my_test.deleter
    def my_test(self):
        print("deleter called")
        del self.__my_attr


my_instance = MyClass()  # создание экземпляра класса
print(my_instance.my_test)  # вызов getter, то есть @property

my_instance.my_test = "TEST"  # вызов setter, то есть @my_test.setter
print(my_instance.my_test)  # вызов getter, то есть @property

del my_instance.my_test  # вызов deleter, то есть @my_test.deleter
# print(my_instance.my_test)  # попытка вызвать getter ещё раз приведёт к ошибки
```

> P.S. Стоит заметить, что все атрибуты-методы при реализации `getter`, `setter`, `deleter` имеют одинаковые названия,
>именно по этому названию (в примере это `my_test`) происходит работа с атрибутом.


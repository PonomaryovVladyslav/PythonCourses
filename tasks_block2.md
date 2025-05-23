
# Задачи второго блока

Во всех задачах реализуй соответствующие классы, соблюдай правила ООП.  

---

## 1. 🏦 Класс `BankAccount`

Создай класс `BankAccount` с приватным атрибутом баланса.

### Требования:
- Метод `deposit(amount)` — пополнение счёта.
- Метод `withdraw(amount)` — снятие со счёта (не снимать больше, чем есть).
- Метод `get_balance()` — возвращает текущий баланс.

---

## 2. 💡 Умное устройство с множественным наследованием

Создай два класса:
- `Speaker` с методом `play_music()`
- `Lamp` с методом `turn_on_light()`

Создай класс `SmartDevice`, который наследует оба и добавляет метод `activate()` — включает музыку и свет.

---

## 3. 🛒 Классы `Product`, `Item`, `ShoppingCart`

- `Product`: название, цена, вес.
- `Item`: содержит `Product` и количество.
- `ShoppingCart`: список объектов `Item`.

### Обязательные методы и поведение:

#### ➕ Добавление товара (`add_item(product, quantity)`):
- Если товар **уже есть** в корзине (сравнение по названию), нужно **увеличить количество** в существующем `Item`.
- Если такого товара ещё **нет**, создать новый `Item` и добавить его в корзину.
- При добавлении **отрицательного количества** — выбросить `ValueError`.

#### ➖ Удаление товара (`remove_item(product)`):
- Удаляет `Item`, содержащий `Product`, из корзины.
- Если товар **не найден**, вывести сообщение:  
  `Продукт '<название>' не найден в корзине.`

#### 📊 Другие методы:
- `get_total_price()` — общая стоимость всех товаров.
- `get_total_weight()` — общий вес всех товаров.
- `__len__()` — количество разных товаров (`Item`).
- `__str__()` — красивый вывод содержимого корзины.

---

## 4. 🧱 Усложнение корзины

Добавь в `ShoppingCart`:

- Метод обновления количества товара.
- Проверки на отрицательные значения цены, веса, количества.
- Поддержку сложения корзин (`+`) — складываются количества совпадающих товаров.
- Сортировку по:
  - цене (если одинаково — по весу, потом по названию),
  - весу,
  - названию.
- Поддержку `in` и индексированного доступа (`[]`).

---

## 5. 📇 Класс `Contact` и `AddressBook` с миксином

- `Contact`: имя, телефон, e-mail
- `AddressBook`: список контактов, метод `add_contact`

### Миксин:
Добавь `SaveToFileMixin` с методом `save_to_file(filename)`, который сохраняет текстовое представление объекта в файл.

### Применение:
- `Contact` и `AddressBook` должны использовать этот миксин.

---

## 6. 🛠️ Усложнение адресной книги

Добавь:

- Проверку на дублирование по email (удалять старый при совпадении).
- Удаление по имени.
- Поиск контактов по имени.

---

## 7. 🃏 Колода карт для игры в "Дурака"

Реализуй:

- `Card`: ранг (`6–A`) и масть (`♠ ♥ ♦ ♣`)
- `Deck`: 36 карт

### Возможности:
- Перетасовать
- Вытянуть карту
- Показать козырь (последняя карта)
- Метод `beats(other, trump_suit)` — побеждает ли карта другую по правилам «дурака»

---

## 8. 🌡️ Класс `Temperature`

- Хранит температуру в Цельсиях.
- `@classmethod`:
  - `from_fahrenheit(cls, f)`
  - `from_kelvin(cls, k)`
- `@property`:
  - `fahrenheit`
  - `kelvin`

---

## 9. 🧱 Паттерн Factory Method

Создай абстрактный класс `Shape` и классы-наследники:
- `Circle`, `Rectangle`, `Square`

Создай `ShapeFactory` с методом `create_shape(type: str)` для создания фигур.

---

## 10. 🧠 Паттерн Strategy: сортировка товаров

- Класс `Product`: название, цена, вес
- Разные стратегии сортировки:
  - по цене
  - по алфавиту
  - по весу

Реализуй отдельные классы-стратегии и класс `ProductSorter`, который принимает стратегию и сортирует список.

---

## ✅ Тесты

К каждой задаче необходимо написать модульные тесты с использованием стандартного модуля `unittest`.


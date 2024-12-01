1. Напишите програму которая находит все простые числа в диапазоне от 2 до 1000.
2. Напишите программу, пользователь вводи строку, а вы создаете словарь, где ключи — это символы строки, а значения —
   количество их вхождений.
3. Создайте два словаря и объедините их в один.
4. Напишите программу, которая удаляет ключ из словаря по введённому пользователем значению ключа.
5. Напишите программу, которая подсчитывает количество уникальных слов в предложении и сохраняет их в словаре.
6. Напишите программу, которая принимает список слов и возвращает словарь, где ключи — это длины слов, а значения —
   списки слов данной длины. ["bla", "test", "two"] -> {3: ["bla", "two"], 4: ["test"]}
7. Создайте программу, которая удаляет все элементы из словаря, ключи которых начинаются с определённого символа.
8. Создайте список словарей с данными о трёх книгах: автор, название, год издания. Напишите программу, которая выводит
   книгу с
   самым ранним годом издания.
9. Есть список словарей, где ключи это имена людей, а значение это рост, возраст и вес. Пользователь задает по какому
   параметру он хочет найти самого-самого. Вывести имя на экран
10. Создайте словарь, который хранит информацию о магазинах и их товарах. Напишите программу для поиска самого дешёвого
    товара среди всех магазинов.
11. Создайте словарь, где ключи — названия стран, а значения — вложенные словари с информацией о населении и площади.
    Напишите программу для вывода самой маленькой страны по площади.
12. Напишите программу, которая принимает строку и выводит все уникальные символы, использованные в этой строке.
13. Напишите программу, которая находит все уникальные слова в тексте и выводит их отсортированными по алфавиту.
14. Создайте множество с элементами от 1 до 10 и удалите из него чётные числа.
15. Напишите программу, которая определяет, содержатся ли все элементы одного множества в другом множестве.
16. Создайте кортеж с числами и найдите минимальное, максимальное и среднее значение.
17. Напишите программу, которая принимает кортеж и выводит его элементы в обратном порядке.
18. Напишите программу, которая принимает кортеж строк и выводит кортеж, где все строки перевёрнуты.
19. Создайте кортеж из чисел и напишите программу для нахождения всех пар чисел, сумма которых равна заданному числу. (
    1,2,3,4,5), число 5, все пары это [(1,4), (2,3)]
20. Напишите программу, которая принимает кортеж чисел и возвращает новый кортеж, состоящий только из чётных чисел.
21. Создайте кортеж имён и напишите программу, которая выводит самое длинное имя.
22. Напишите программу, которая принимает кортеж чисел и возвращает кортеж, содержащий только уникальные элементы.
23. Напишите программу, которая преобразует список кортежей состоящих из двух строк в словарь, где первый элемент
    каждого кортежа становится ключом, а второй — значением.
24. Создайте словарь с множествами в качестве значений и найдите пересечение всех множеств.
25. Создайте кортеж, содержащий множества, и напишите программу для нахождения объединения всех множеств в кортеже.
26. Напишите программу, которая преобразует строку в множество и возвращает кортеж, содержащий длину этого множества и
    количество гласных в нём.
27. Создайте два словаря, в которых ключи — это числа, а значения — множества. Напишите программу для нахождения
    объединения всех множеств с одинаковыми ключами.
28. Напишите программу, которая принимает словарь с множествами и кортежами в качестве значений и выводит на экран все
    уникальные элементы из этих множеств и кортежей.

Две сложные задачки:


На вход приходит список словарей, с одинаковыми ключами, и список строк, который содержит ключи из этих же словарей. Нужно получить список словарей, для которых значени указанных ключей будут уникальными.
    
        Если:
       list_of_dicts = [
           {
           "name": "Vlad",
           "age": 30,
           "city": "Prague"
           },
           {
           "name": "Stas",
           "age": 30,
           "city": "Prague"
           },
           {
           "name": "Vlad",
           "age": 25,
           "city": "Prague"
           }, {
           "name": "Vlad",
           "age": 30,
           "city": "Berlin"
           }
      ]

      И:

      list_of_keys = ["name", "age"]

      То:    

       result = [
           {
           "name": "Vlad",
           "age": 30,
           "city": "Prague"
           },
           {
           "name": "Stas",
           "age": 30,
           "city": "Prague"
           },
           {
           "name": "Vlad",
           "age": 25,
           "city": "Prague"
           }
      ]
    
      Если ключи:

      list_of_keys = ["age", "city"]

      То:

      result = [
           {
           "name": "Vlad",
           "age": 30,
           "city": "Prague"
           },
           {
           "name": "Vlad",
           "age": 25,
           "city": "Prague"
           }, {
           "name": "Vlad",
           "age": 30,
           "city": "Berlin"
           }
      ]
    
      Если ключи:

      list_of_keys = ["name", "city"]

      то:

      result = [
          {
          "name": "Vlad",
          "age": 30,
          "city": "Prague"
          },
          {
          "name": "Stas",
          "age": 30,
          "city": "Prague"
          },
          {
          "name": "Vlad",
          "age": 30,
          "city": "Berlin"
          }
      ]



Банкомат. Нужно вычислить какими купюрами будет выдана сумма в банкомате, если есть условие, сумма должна быть выдана минимальными купюрами, но не более чем 10 купюр одного номинала.
   
    Допустим существуют купюры [1, 2, 5, 10, 20, 50, 100, 200, 500]
    
    Пользователь вводит 16

        You need: 
        banknote 1, 10 times
        banknote 2, 3 times

    Пользователь вводит 123 
      
        You need: 
        banknote 1, 10 times
        banknote 2, 9 times
        banknote 5, 9 times
        banknote 10, 5 times

    Пользователь вводит 1234 

        You need: 
        banknote 1, 9 times
        banknote 2, 10 times
        banknote 5, 9 times
        banknote 10, 10 times
        banknote 20, 8 times
        banknote 50, 10 times
        banknote 100, 4 times
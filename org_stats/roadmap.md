# Итерация 1

Основные силы были направлены на реализацию функциональности, связанной с генерацией БД.

## Функциональность
- Представление дерева генерации БД в формате json; парсинг дерева генерации для его дальнейшего использования при генерации БД
- Генерация БД на основе файла с деревом генерации
- Формирование описания БД на естественном языке
- Определение сида генерации БД
- Формирование дампа сгенерированной БД

## Покрытие тестами
- Класс генератора случайных чисел, используемого при генерации БД  
- Класс дерева правил генерации БД
- Класс генератора БД

# Итерация 2

## План на итерацию 2
- Генерация SELECT-запросов
- Вычисление правильного результата запроса
- Словестное описание запросов
- Исправление багов, обнаруженных за первую итерацию

## Реализованная за итерацию 2 функциональность
- Сохранение результатов работы из docker-контейнера
- Генерация простых SELECT-запросов (без ключевых слов)
- Вычисление правильного результата запроса
- Словестное описание запросов (с поддержкой ключевых слов WHERE и ORDER BY)
- Переработан формат файла с деревом генерации в целям добавления поддержки связей между таблицами

## Покрытие тестами
Был исправлен баг с выполенением тестов, теперь они являются повторяемыми (была добавлена поддержка передачи сида в тесты).

# Итерация 3

## План на итерацию 3
- Генерация таблиц со связями (1:1, 1:n, m:n)
- Генерация запросов c ключевыми словами WHERE и ORDER BY
- Формирование словесного описания задания
- Вывод в терминал и файл

## Реализованная за итерацию 3 функциональность
- решена проблема с сохранением результатов из докер-контейнера (через volume)
- генерация таблиц со связями (1:1, 1:n, m:n)
- составление словесного описания задания (метод)
- вывод в PDF (метод)

## Покрытие тестами
В процессе исправление бага с локальным запуском тестов

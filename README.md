# mse_db_gen_tasks

## Запуск Docker:
```
  docker build -t gr3pr1/mse .
```
```
  docker run gr3pr1/mse
```
## Запуск приложения (CLI):
Запуск генератора со случайным зерном
```commandline
  python3 ./run_gen.py
```
Запуск генератора с заданным зерном
```commandline
  python3 ./run_gen.py [-s, --seed] SEED (число вместо SEED) 
```
Вывод подсказки
```commandline
  python3 ./run_gen.py [-h, --help]
```

## Запуск Unit-тестов:
Вызвать подсказку (-h необязательно)
```commandline
    bash tests.sh -h
```
Запуск всех тестов 
```commandline
    bash tests.sh run_all
```
Запуск тестов генератора последовательности случайных чисел
```commandline
    bash tests.sh run_seq_gen_tests
```
Запуск тестов генератора баз данных
```commandline
    bash tests.sh run_db_tests
```

## Файл дерева генерации базы данных:
```
Дерево описывается в формате JSON.
Каждый узел дерева - это таблица, в которой можно создать поля и от которой можно перейти к другим соответствующим таблицам.
```

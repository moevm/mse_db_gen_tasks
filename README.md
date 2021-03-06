# mse_db_gen_tasks

## Установка зависимостей

Для корректной работы приложения (_если оно запускается не в docker-контейнере_) необходимо установить зависимости, указанные в `requirements.txt`, чтобы это сделать 
используйте команду:

```commandline
pip install -r requirements.txt
```

## Use cases
Данное приложение можно использовать в случае, если пользователю необходимо сгенерировать базу данных с случайными структурой и наполнением таблиц, а также последующим сохранением структуры базы данных в `.json` файл и генерацией дампа базы данных.

## Запуск с помощью docker-compose
Для того, чтобы запусить программу с помощью docker-compose сначала используйте команду `docker-compose build`. После чего вы сможете использовать приложение с помощью следующей команды:
```commandline
docker-compose run --entrypoint="CMD" db_gen
```
Где CMD -- любая команда из перечня доступных, например: `python3 ./run_gen.py gen_select_request`. Реузльтаты выполнения команд будут созранены в папку `results`
## Запуск приложения без docker-compose:
1. Запуск генератора с заданным зерном
   >Результат выполнения данной команды аналогичен результату выполнения команды, указанной выше, но в этом случае будет использован указанный сид для генерации таблицы.
```commandline
python3 ./run_gen.py gen_with_seed [-s, --seed] SEED (число вместо SEED) [-d, --dump]  PATH (path - строка пути к файлу, если путь не указывать, то будет запуск без дампа)
```
2. Запуск генератора со случайным зерном
    >В результате выполнения данной команды будет сгенерирован файл с указанным названием, в котором будет представлен обычный дамп базы данных.
```commandline
python3 ./run_gen.py gen_with_random_seed [-d, --dump]  PATH (path - строка пути к файлу, если путь не указывать, то будет запуск без дампа)
```
3. Генерация запроса
```commandline
python3 ./run_gen.py gen_select_request [-w] True/False [-o] True/False (default - False)
```
4. Вывод подсказки
   >В результате выполнения данной команды будет выведена подсказка.
```commandline
python3 ./run_gen.py (название команды) [--help]
```
## Запуск Unit-тестов:
Вызвать подсказку (-h необязательно)
```commandline
bash tests.sh -h
```
Запуск всех тестов 
```commandline
bash tests.sh run_all [seed]|NULL
```
Запуск тестов генератора последовательности случайных чисел
```commandline
bash tests.sh run_seq_gen_tests [seed]|NULL
```
Запуск тестов генератора баз данных
```commandline
bash tests.sh run_db_tests [seed]|NULL
```

## Пример работы
https://youtu.be/guJ0jzxemVc &ndash; демонстрация генерации дерева базы данных.

https://youtu.be/KGXc-MHRHDM &ndash; демонстрация дампа базы данных.

## Файл дерева генерации базы данных:
Дерево описывается в формате JSON.
Каждый узел исходящий от root - это таблица, каждый узел исходящий от таблицы - поле таблицы.
Каждый узел содержит в себе следующие поля: название узла, тип и опционально содержит ссылку на поле другой таблицы.
Ссылки показывают, какие поля таблиц являются внешними ключами и с какими ключами они связаны.

JSON на внешнем уровне в ключах содержит названия таблиц. У каждой таблицы имеются ключевые поля.
fields - содержит пары в которых ключ - название поля таблицы, значение - тип данных.
foreign - содержит информацию о том, какие поля являются внешними ключами и с какими полями другой таблицы они связаны.

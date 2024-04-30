# Приложение "YaCut - укоротитель ссылок"

## Описание:

Учебный проект по изучению фреймворка [Flask](https://flask.palletsprojects.com).

Приложение позволяет создавать для веб-сайтов короткие ссылки в формате 
```http://localhost/<short-id>```. 
```<short-id>``` возможно задать свой или сгенерировать автоматически.

Созданные короткие ссылки сохраняются в базе данных.

## Использование:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:AleksandrPU/yacut.git
```

```
cd yacut
```

Создать и активировать виртуальное окружение:

```
python3.9 -m venv venv
```

**ВНИМАНИЕ!** Необходимо использовать Python версии 3.9.

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Переименовать файл ```env.example``` в файл ```.env```.

```
mv env.example .env
```

Задать секретный ключ ```SECRET_KEY``` в файле ```.env```.
Значение ```SECRET_KEY``` можно сгенерировать командой:

```
python -c 'import secrets; print(secrets.token_hex())'
```

Запустить проект:

```
flask run
```

По умолчанию приложение запустится по адресу [http://localhost:5000](http://localhost:5000).

## Автор:

Проект создан Паутовым Александром на основе репозитория 
[yandex-praktikum/yacut](https://github.com/yandex-praktikum/yacut).
# qa_guru_python_9_11_Selene_UI_project
# Проект по тестированию сайта интернет-магазина Литрес
> <a target="_blank" href="https://www.litres.ru/">Ссылка на Интернет-магазин</a>

#### Список проверок, реализованных в автотестах
- [x] Проверка авторизации с валидными и не валидными данными
- [x] Провека добавления и удаления товара из корзины
- [x] Провека добавления и удаления товара из избранного
- [x] Проверка наличия на главной странице каталога

### Структура проекта

### Проект реализован с использованием
Python Pytest PyCharm Selenoid Selene Jenkins Allure Report Telegram 

<img src="/design/python-original.svg" alt="Image 1" width="45" height="45"><img src="/design/pytest-original.svg" alt="Image 2" width="45" height="45"><img src="/design/PyCharm_Icon.svg" alt="Image 3" width="45" height="45"><img src="/design/selenoid.png" alt="Image 4" width="45" height="45"><img src="/design/jenkins-original.svg" alt="Image 5" width="45" height="45">
<img src="/design/allure.png" alt="Image 6" width="45" height="45"><img src="/design/telegram.svg" alt="Image 7" width="45" height="45">

# Запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/C09_Gavrilenko_Sergey_15_unit/">Ссылка на проект в Jenkins</a>

### Для запуска автотестов в Jenkins
#### 1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/C09_Gavrilenko_Sergey_15_unit/">проект</a>

![This is an image](/design/screens/Jenkins_main.png)

#### 2. Выбрать пункт **Собрать с параметрами**
#### 3. В случае необходимости изменить параметры, выбрав значения из выпадающих списков
#### 4. Нажать **Собрать**
#### 5. Результат запуска сборки можно посмотреть в отчёте Allure

![This is an image](/design/screens/allure_report.png)

### Локальный запуск автотестов
1. Клонируйте репозиторий на свой локальный компьютер при помощи git clone
2. Создайте и активируйте виртуальное окружение
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```
3. Установите зависимости с помощью pip
  ```bash
  pip install -r requirements.txt
  ```
4. Для запусков тестов локально используйте команду 
  ```bash
  pytest -sv
  ```
5. Для запусков тестов удаленно используйте команду 
  ```bash
  environment='remote' pytest -sv
  ```

Получение отчёта allure:
```bash
allure serve allure-results
``` 

### Пример видеозаписи прохождения теста
![This is an image](/design/screens/test_gif.gif)

### Настроено автоматическое оповещение о результатах сборки Jenkins в Telegram-бот
![This is an image](/design/screens/bot.png)
# Проект по тестированию сервиса мужских аксессуаров, украшений ручной работы, косметики и других подарков для мужчин.

----
> Магазин мужских подарков, аксессуаров и украшений

> [Сайт BORODA.LAND](https://boroda.land/)

![](https://github.com/matygullinruslan/qa_guru_python_9_11_Selene_UI_project/blob/main/assets/site_land.png)
----

## Список проверок, реализованных в автотестах:

### UI автотесты:

- [x] Проверка авторизации с валидными и не валидными данными
- [x] Регистрация пользователя на сайте 
- [x] Провека добавления и удаления товара из корзины
- [x] Провека добавления и удаления товара из избранного
- [x] Проверка поиска товара с помощью поисковой строки
- [x] Проверка выбора товара на главной странице каталога

----

### Проект реализован с использованием:

<p  align="left">
<code><img width="5%" title="python" src="https://github.com/matygullinruslan/qa_guru_python_9_11_Selene_UI_project/blob/main/assets/python.png"></code>
<code><img width="5%" title="selene" src="https://github.com/matygullinruslan/qa_guru_python_9_11_Selene_UI_project/blob/main/assets/selene.png"></code>
<code><img width="5%" title="selenium" src="https://github.com/matygullinruslan/qa_guru_python_9_11_Selene_UI_project/blob/main/assets/selenium.png"></code>
<code><img width="5%" title="pytest" src="https://github.com/matygullinruslan/qa_guru_python_9_11_Selene_UI_project/blob/main/assets/pytest.png"></code>
<code><img width="5%" title="selenoid" src="https://github.com/matygullinruslan/qa_guru_python_9_11_Selene_UI_project/blob/main/assets/selenoid.png"></code>
<code><img width="5%" title="jenkins" src="https://github.com/matygullinruslan/qa_guru_python_9_11_Selene_UI_project/blob/main/assets/jenkins.png"></code>
<code><img width="5%" title="allure" src="https://github.com/matygullinruslan/qa_guru_python_9_11_Selene_UI_project/blob/main/assets/allure_report.png"></code>
<code><img width="5%" title="alluretestops" src="https://github.com/matygullinruslan/qa_guru_python_9_11_Selene_UI_project/blob/main/assets/allure_testops.png"></code>
<code><img width="5%" title="github" src="https://github.com/matygullinruslan/qa_guru_python_9_11_Selene_UI_project/blob/main/assets/github.png"></code>  
<code><img width="5%" title="telegram" src="https://github.com/matygullinruslan/qa_guru_python_9_11_Selene_UI_project/blob/main/assets/telegram.png"></code>   
<code><img width="5%" title="pycharm" src="https://github.com/matygullinruslan/qa_guru_python_9_11_Selene_UI_project/blob/main/assets/pycharml.png"></code>  


> Для полноценного прохождения всех тестов должно быть  зарегистрировано два аккаунта. Данные
> которых необходимо указать в файле
`.env`
>
Для написания UI-тестов используется фреймворк `Selene`, современная «обёртка» вокруг `Selenium WebDriver`
Библиотека модульного тестирования: `PyTest`  
`Jenkins` выполняет удаленный запуск тестов в графическом интерфейсе. Установки дополнительных приложений на компьютер
пользователя не требуется.  
`Selenoid` запускает браузер с тестами в контейнерах `Docker` (и записывает видео)  
Фреймворк `Allure Report` собирает графический отчет о прохождении тестов  
После завершения тестов `Telegram Bot` отправляет в `Telegram` краткий вариант `Allure Report`

----

### Локальный запуск

Необходимо создать файл `.env` и заполнить его актуальными тестовыми параметрами.

1) Скачать проект и открыть в IDE
2) Для локального запуска необходимо выполнить команду в терминале:

```commandline
pytest
```

3) Выполнить запрос на формирование отчета  
   note: команда для Windows

```commandline
allure serve
```

Результат: откроется страница с отчетом Allure Report

----

### <img width="3%" title="Jenkins" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg"> Удаленный запуск автотестов выполняется на сервере Jenkins

> <a target="_blank" href="https://jenkins.autotests.cloud/job/qa_guru_python_9_11_Selene_UI_project/">Ссылка на проект в
> Jenkins</a>

----


#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/C10_MDN782007_autodoc_test_project/">проект</a>
2. Выбрать пункт `Build with Parameters`
3. Выбрать браузер
4. Выбрать версию браузера
4. Указать комментарий для уведомления в Телеграмм
5. Нажать кнопку `Build`
6. Результат запуска сборки можно посмотреть в отчёте Allure



----

### <img width="3%" title="Allure report" src="https://github.com/matygullinruslan/qa_guru_python_9_11_Selene_UI_project/blob/main/assets/allure_report.png"> Allure отчет

![image](assets/Allure_Report_test.png)
Отчет позволяет получить детальную информацию по все шагам тестов, включая скриншоты и log - файлы


### <img width="3%" title="Allure report" src="https://github.com/matygullinruslan/qa_guru_python_9_11_Selene_UI_project/blob/main/assets/authorization.gif"> Видео прохождения теста:

Видеозапись каждого теста генерируется с помощью `Selenoid` после успешного запуска контейнера c тестами в `Docker`.

![image](assets/test_example.gif)

### <img width="3%" title="Allure report" src="assets/tg.png"> Получение уведомлений о прохождении тестов в Telegram

После завершения сборки специальный Telegram-бот отправляет сообщение с отчетом.  








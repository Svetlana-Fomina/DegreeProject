# README
## Инструкция 
1. Установить и запустить `Pycharm` на компьютере
2. В консоли с помощью команды pip установить следующие пакеты: `pip install requests`, `pip install pytest`. 
3. Запуск актуального [стенда], запись его пути в файл configuration.py. 
4. Переход к документации [API], запись пути в файл configuration.py. 
5. Изучение раздела [Orders - Создание заказа]
6. Изучение раздела [Orders - Получить заказ по его номеру]
7. Производим запрос на создание нового заказа с помощью функции `def post_new_order` в файле sender_stand_request.py 
8. Производим запрос на получение трек-номера для заказа с помощью функции `def get_track_number_of_order` в файле create_orders_test.py и сохраняем номер трека созданного заказа
9. Производим запрос на получение заказа по трек-номеру с помощью функции `def test_create_and_track_order` в файле create_orders_test.py 
10. Производим запрос на получение информации о заказе с помощью функции `def get_order_info(track_number)` в файле sender_stand_request.py 
10. Проверить, что код ответа равен 200 с помощью оператора `assert`


### Что важно учесть

- Всего понадобится 6 файлов: configuration.py, data.py, sender_stand_request.py, create_orders_test.py, README.md, .gitignore. 
- В  файле _configuration.py_ указать url-стенда, api на создание заказа и п олучение  заказа по его номеру
- В файле _sender_stand_request.py_ указать функции создания нового заказа и получение информации о заказе
- В файле _data.py_ указать тела POST-запросов
- В файле _create_orders_test.py _ написать чек-лист
- Каждый тест должен быть в отдельной функции с префиксом `test`. 

   [стенда]: <https://47525ced-5beb-4179-8c88-3c8f3ff3dec6.serverhub.praktikum-services.ru>
   [API]: <https://47525ced-5beb-4179-8c88-3c8f3ff3dec6.serverhub.praktikum-services.ru/docs/>
   [Orders - Создание заказа]: <https://47525ced-5beb-4179-8c88-3c8f3ff3dec6.serverhub.praktikum-services.ru/docs/#api-Orders-CreateOrder>
    [Orders - Получить заказ по его номеру]: <https://47525ced-5beb-4179-8c88-3c8f3ff3dec6.serverhub.praktikum-services.ru/docs/#api-Orders-GetOrderByTrackNumber>
   [Main.Kits]: <https://47525ced-5beb-4179-8c88-3c8f3ff3dec6.serverhub.praktikum-services.ru/docs/#api-Main.Kits-CreateKit>

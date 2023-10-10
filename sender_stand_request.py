import requests
import configuration
import data

def post_new_order():                                                                   # запрос на создание нового заказа
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
           json=data.order_body)


def get_order_info(track_number):                                                       # запрос на получение информации о заказе
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK,
           params={"t": track_number})

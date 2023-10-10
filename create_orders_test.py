import pytest
import sender_stand_request


def get_track_number_of_order():
    track_number = sender_stand_request.post_new_order()                # запрос на получение трек-номера заказа
    return track_number.json()["track"]

def test_create_and_track_order():
    track_number = get_track_number_of_order()                          # запрос на получение заказа по трек-номеру
    get_response = sender_stand_request.get_order_info(track_number) 
    assert get_response.status_code == 200                              # проверка, что ответ возвращается с кодом статуса 200

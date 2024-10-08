import functions as func


# 1. GET.
def test_get_booking_ids():
    response = func.get_all_bookings()
    assert response.status_code == 200, "Код статуса не равен 200"
    return response


# 2. POST.
def test_create_booking():
    booking_info = {
        "firstname": "Tulka",
        "lastname": "Grande",
        "totalprice": 123,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-10-02",
            "checkout": "2024-10-03"
        },
        "additionalneeds": "Breakfast"
    }
# Создание бронирования
    response = func.create_booking(booking_info)
# Получение id букинга из json ответа
    response_post_json = response.json()
    booking_id = (response_post_json.get("bookingid"))

    response_get = func.get_booking_by_id(booking_id)
    response_get_json = response_get.json()

    assert response_get_json.get("firstname") == "Tulka"
    assert response_get_json.get("lastname") == "Grande"


# 3. PATCH
def test_create_and_patch_booking():
    # Создание бронирования, получение booking_id
    booking_info = {
        "firstname": "Tulka",
        "lastname": "Grande",
        "totalprice": 123,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-10-02",
            "checkout": "2024-10-03"
        },
        "additionalneeds": "Breakfast"
    }
    response = func.create_booking(booking_info)
    booking_id = response.json()["bookingid"]

    # Изменение "firstname" и "lastname" и применением токена аутентификации
    headers = {
        'Cookie': f'token={func.create_token("admin", "password123")}'
    }
    new_data = {
        "firstname": "Tutulka",
        "lastname": "Pequeno"
    }
    func.patch_booking(new_data, headers, booking_id)

    # Получение информации о бронировании
    patched_booking = (func.get_booking_by_id(booking_id))
    response_get_json = patched_booking.json()

    assert response_get_json.get("firstname") == "Tutulka"
    assert response_get_json.get("lastname") == "Pequeno"


# 4. DELETE.
def test_create_and_delete_booking():
    # Создание бронирования, получение booking_id
    booking_info = {
        "firstname": "Tulka",
        "lastname": "Grande",
        "totalprice": 123,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-10-02",
            "checkout": "2024-10-03"
        },
        "additionalneeds": "Breakfast"
    }
    response = func.create_booking(booking_info)
    booking_id = response.json()["bookingid"]

    headers = {
        'Cookie': f'token={func.create_token("admin", "password123")}'
    }
    func.delete_booking_by_id(booking_id, headers)
    response_get = func.get_booking_by_id(booking_id)

    assert response_get.status_code == 200, "Статус код не равен 404"


# 1. Калькулятор.

calc = func.Calculator()
calc.add(1, 3)
calc.div(2, 10)
calc.mul(100, 12.2)
print(calc.show_operations())
calc.clear_history()

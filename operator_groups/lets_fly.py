from collections import OrderedDict


def get_lets_fly_groups():
    return OrderedDict({
        "Наши ошибки": OrderedDict({
            "package_is_expired": [
                "package is expired",
            ],
            "empty_routes_after_cast": [
                "error getting routes: empty routes after cast",
            ],
            "route_not_found_in_cache": [
                "error finding route in cache: route not found",
            ],
            "proxy_connection_refused": [
                "proxyconnect tcp: dial tcp",
            ],
        }),
        "Неизвестно чьи ошибки": OrderedDict({
            "connection_error": [
                "error in ReadAll: unexpected EOF",
            ],
        }),
        "Ошибки ТО Lets Fly": OrderedDict({
            "timeout": [
                "context cancelled (timeout)",
            ],
            "booking_closed_for_dates": [
                "Бронирование на выбранные даты закрыто",
            ],
            "invalid_supplier_response": [
                "invalid result structure: invalid claim document: only one set of hotel data expected",
            ],
            "internal_server_error": [
                "Внутренняя ошибка сервера приложений",
            ],
            "no_flights": [
                "Рейсы не найдены",
            ],
            "bad_gateway_response": [
                "unexpected content type: text/html, status: 502",
                "request failed with status code 502",
            ],
            "required_service_missing": [
                "Не передана входящая в пакет обязательная для бронирования услуга",
            ],
            "offer_not_actual": [
                "Предложение больше не действительно",
            ],
            "price_not_found": [
                "Не найдена цена",
            ],
            "transport_booking_failed": [
                "Невозможно забронировать транспорт",
            ],
            "supplier_response_500": [
                "unexpected content type: text/html; charset=utf-8, status: 500",
            ],
        }),
    })

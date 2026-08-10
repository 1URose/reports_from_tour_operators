from collections import OrderedDict


def get_space_travel_groups():
    return OrderedDict({
        "Наши ошибки": OrderedDict({
            "package_is_expired": [
                "package is expired",
            ],
            "empty_routes_after_cast": [
                "error getting routes: empty routes after cast",
            ],
            "empty_transports_after_pick": [
                "empty transports after pick",
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
        "Ошибки ТО SpaceTravel": OrderedDict({
            "timeout": [
                "context cancelled (timeout)",
            ],
            "bad_gateway_response": [
                "unexpected content type: text/html, status: 502",
                "unexpected content type: text/html;charset=utf-8, status: 502",
                "request failed with status code 502",
            ],
            "internal_server_error": [
                "Внутренняя ошибка сервера приложений",
            ],
            "offer_not_actual": [
                "Предложение больше не действительно",
            ],
            "invalid_supplier_response": [
                "invalid result structure: invalid claim document: only one set of hotel data expected",
            ],
            "no_flights": [
                "Рейсы не найдены",
            ],
            "price_not_found": [
                "Не найдена цена",
            ],
            "supplier_busy": [
                "Сервер занят. Пожалуйста, повторите попытку позже.",
            ],
            "supplier_dns_error": [
                "Could not resolve host: andr.space-travel.ru",
            ],
            "transport_booking_failed": [
                "Невозможно забронировать транспорт",
            ],
            "supplier_response_500": [
                "unexpected content type: text/html; charset=utf-8, status: 500",
            ],
        }),
    })

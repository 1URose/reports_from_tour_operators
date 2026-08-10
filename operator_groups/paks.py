from collections import OrderedDict


def get_paks_groups():
    return OrderedDict({
        "Наши ошибки": OrderedDict({
            "package_is_expired": [
                "package is expired",
            ],
            "empty_routes_after_cast": [
                "error getting routes: empty routes after cast",
            ],
            "package_not_found": [
                "error building domain package: package not found",
            ],
            "tour_dropped_by_rules": [
                "error applying rules to tour: tour dropped by rules",
            ],
            "proxy_connection_refused": [
                "proxyconnect tcp: dial tcp",
            ],
        }),
        "Неизвестно чьи ошибки": OrderedDict({

        }),
        "Ошибки ТО Paks": OrderedDict({
            "timeout": [
                "context cancelled (timeout)",
                "Превышено время ожидания ответа от туроператора",
            ],
            "internal_server_error": [
                "Внутренняя ошибка сервера приложений",
            ],
            "bad_gateway_response": [
                "unexpected content type: text/html, status: 502",
                "request failed with status code 502",
            ],
            "route_not_found_in_tour": [
                "error replacing route: route with id",
            ],
            "offer_expired": [
                "Предложение больше не действительно",
            ],
            "supplier_connection_error": [
                "Failed to connect to robot.paks.ru",
                "Could not resolve host: robot.paks.ru",
            ],
            "price_not_found": [
                "причина (Не найдена цена)",
            ],
            "search_data_expired": [
                "Данные поиска устарели. Сделайте новый поиск.",
            ],
            "required_service_missing": [
                "Не передана входящая в пакет обязательная для бронирования услуга",
            ],
        }),
    })

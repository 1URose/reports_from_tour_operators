from collections import OrderedDict


def get_russ_express_groups():
    return OrderedDict({
        "Наши ошибки": OrderedDict({
            "package_is_expired": [
                "package is expired",
            ],
            "empty_routes_after_cast": [
                "error getting routes: empty routes after cast",
            ],
            "proxy_connection_refused": [
                "proxyconnect tcp: dial tcp",
            ],
        }),
        "Неизвестно чьи ошибки": OrderedDict({
        }),
        "Ошибки ТО RussExpress": OrderedDict({
            "supplier_ssl_error": [
                "OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to online.r-express.ru:443",
            ],
            "supplier_internal_server_error": [
                "500 Internal Server Error",
                "Внутренняя ошибка сервера приложений",
            ],
            "supplier_bad_gateway": [
                "502 Bad Gateway",
                "unexpected content type: text/html, status: 502",
                "request failed with status code 502",
            ],
            "currency_catalog_error": [
                "Предложение не действительно: debug: get currency catalog",
            ],
            "offer_not_actual": [
                "Предложение больше не действительно",
            ],
            "invalid_tariff_attributes": [
                "error parsing transport luggage: empty tariff attributes",
            ],
            "supplier_connection_reset": [
                "Recv failure: Connection reset by peer",
            ],
            "empty_supplier_response": [
                "Empty reply from server",
            ],
            "accommodation_mismatch": [
                "People does not fit accommodation",
            ],
            "no_flights": [
                "Рейсы не найдены",
            ],
            "insurance_pattern_error": [
                "Cant get pattern_insure",
            ],
            "price_not_found": [
                "Не найдена цена",
            ],
            "global_offer_mismatch": [
                "Глобальное СПО не подходит для расчета",
            ],
            "supplier_timeout": [
                "context cancelled (timeout)",
                "Превышено время ожидания ответа от туроператора",
            ],
        }),
    })

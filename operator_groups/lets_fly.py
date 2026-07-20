from collections import OrderedDict


def get_lets_fly_groups():
    return OrderedDict({
        "Наши ошибки": OrderedDict({
            "package_expired": [
                "package is expired",
                "tour expired",
            ],
            "rules_drop": [
                "tour dropped by rules",
                "error applying rules to tour",
            ],
            "route_cache_miss": [
                "error finding route in cache",
                "route not found in cache",
            ],
            "operator_mismatch": [
                "package and route have different operators",
            ],
            "empty_routes": [
                "empty routes after cast",
                "failed to cast routes: empty result routes",
            ],
            "rate_error": [
                "no rate",
                "failed to get rate",
                "unknown currency",
            ],
            "db_connection": [
                "error getting package by id: query failed: invalid connection",
                "query failed: dial tcp",
                "Lost connection to MySQL server",
                "connect: connection refused",
            ],
            "cache_write": [
                "failed to insert routes",
                "failed to reset fresh routes IDs",
                "error writing to cache",
                "READONLY You can't write against a read only replica",
            ],
        }),
        "Неизвестно чьи ошибки": OrderedDict({
            "timeout": [
                "context deadline exceeded",
                "context cancelled",
                "context canceled",
                "Client.Timeout exceeded while awaiting headers",
                "i/o timeout",
                "TLS handshake timeout",
            ],
            "transport": [
                "connection reset by peer",
                "connection refused",
                "connection timed out",
                "no route to host",
                "unexpected EOF",
                "EOF",
            ],
            "bad_payload": [
                "invalid character '<' looking for beginning of value",
                "json unmarshal error",
                "xml unmarshal error",
                "expected element type",
                "unexpected end of JSON input",
            ],
            "empty_response": [
                "empty body response",
                "empty booking response",
                "empty prebook response",
                "api response error: None",
            ],
        }),
        "Ошибки ТО Lets Fly": OrderedDict({
            "no_available_flights": [
                "No flights",
                "no flights",
                "no suitable flights found",
                "no seats",
                "Нет мест на рейсе",
                "рейсы отсутствуют",
                "По указанным параметрам рейсы отсутствуют",
            ],
            "no_availability": [
                "no availability",
                "No availability",
                "Нет доступных мест",
                "Нет мест",
                "мест нет",
            ],
            "offer_expired": [
                "offer not found",
                "similar offer not found",
                "Предложение более недоступно",
                "Предложение недоступно",
                "Поиск устарел",
                "Параметры поиска устарели",
            ],
            "price_or_fare_changed": [
                "price has changed",
                "price changed",
                "fare expired",
                "tariff expired",
                "Стоимость тура изменилась",
                "цена изменилась",
                "тариф изменился",
            ],
            "hotel_or_room_stop": [
                "hotel has unavailable status",
                "room rate has expired",
                "room is not available",
                "stop sale",
                "отель в стопе",
                "номер в стопе",
            ],
            "booking_not_created": [
                "booking already in progress",
                "booking not created",
                "failed to create_booking",
                "failed to prebook",
                "prebook have failed status",
                "Невозможно создать бронирование",
            ],
            "authorization": [
                "Unauthorized",
                "Пользователь не авторизован",
                "authorization failed",
                "Session expired",
                "Invalid Authorization",
            ],
            "tourist_validation": [
                "invalid tourist",
                "tourist name",
                "empty full name",
                "invalid phone",
                "empty email",
            ],
            "document_validation": [
                "document info is duplicated",
                "document number is invalid",
                "invalid document number",
                "document expires before end of travel",
                "birth certificate cannot be used after age",
            ],
            "supplier_5xx": [
                "Внутренняя ошибка сервера",
                "Internal server error",
                "request failed with status code 500",
                "request failed with status code 502",
                "request failed with status code 503",
                "Service Unavailable",
            ],
        }),
    })

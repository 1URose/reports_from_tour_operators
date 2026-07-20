from collections import OrderedDict


def get_space_travel_groups():
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
            "invalid_response": [
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
        "Ошибки ТО SpaceTravel": OrderedDict({
            "fare_expired": [
                "fare expired",
                "tariff expired",
                "тариф устарел",
                "тариф изменился",
                "price has changed",
                "price changed",
            ],
            "no_seats": [
                "no seats",
                "No flights",
                "no flights",
                "No availability",
                "Нет мест",
                "Нет мест на рейсе",
                "рейсы отсутствуют",
            ],
            "offer_not_actual": [
                "offer not found",
                "similar offer not found",
                "Предложение более недоступно",
                "Предложение недоступно",
                "Поиск устарел",
                "Параметры поиска устарели",
            ],
            "pnr_or_booking_not_created": [
                "PNR",
                "pnr",
                "booking not created",
                "Невозможно создать бронирование",
                "Не удалось создать бронирование",
            ],
            "ticketing_limit": [
                "time limit",
                "ticketing time limit",
                "Истек таймлимит",
                "срок выписки истек",
            ],
            "gds_or_supplier_error": [
                "GDS",
                "Amadeus",
                "Sabre",
                "Galileo",
                "supplier response error",
                "supplier error",
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

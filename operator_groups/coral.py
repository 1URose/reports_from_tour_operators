from collections import OrderedDict


def get_coral_groups():
    return OrderedDict({
        "Наши ошибки": OrderedDict({
            "package_is_expired": [
                "package is expired",
                "tour expired",
            ],
            "tour_dropped_by_rules": [
                "tour dropped by rules",
                "error applying rules to tour",
            ],
            "route_not_found_in_cache": [
                "error finding route in cache",
                "route not found in cache",
            ],
            "package_route_operator_mismatch": [
                "package and route have different operators",
            ],
            "empty_route_after_cast": [
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
            "cache_write_error": [
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
            "connection_error": [
                "connection reset by peer",
                "connection refused",
                "connection timed out",
                "no route to host",
                "unexpected EOF",
                "EOF",
            ],
            "invalid_response_format": [
                "invalid character '<' looking for beginning of value",
                "json unmarshal error",
                "xml unmarshal error",
                "expected element type",
                "unexpected end of JSON input",
            ],
            "empty_supplier_response": [
                "empty body response",
                "empty booking response",
                "empty prebook response",
                "api response error: None",
            ],
        }),
        "Ошибки ТО Coral": OrderedDict({
            "no_availability": [
                "no availability",
                "No availability",
                "Нет доступных мест",
                "Нет мест",
                "мест нет",
                "не подтвердил наличие мест",
            ],
            "no_flights": [
                "No flights",
                "no flights",
                "По указанным параметрам рейсы отсутствуют",
                "no suitable flights found",
                "не получили подтверждение о наличии свободных мест на этом перелёте",
            ],
            "offer_not_actual": [
                "Внимание! Предложение более недоступно",
                "Предложение более недоступно",
                "Предложение недоступно",
                "Поиск устарел",
                "Параметры поиска устарели",
                "Результаты поиска устарели",
                "offer not found",
                "similar offer not found",
            ],
            "price_changed": [
                "price has changed",
                "price changed",
                "Стоимость тура изменилась",
                "цена изменилась",
                "изменение стоимости",
            ],
            "hotel_or_room_stop": [
                "hotel has unavailable status",
                "This room rate has expired",
                "room rate has expired",
                "room is not available",
                "hotel is stop sale",
                "stop sale",
            ],
            "auth_or_session": [
                "Unauthorized",
                "Пользователь не авторизован",
                "authorization failed",
                "Invalid Authorization",
                "Session expired",
                "Full authentication is required",
            ],
            "tourist_validation": [
                "tourist name has test format",
                "tourist name must be in latin",
                "tourist name must be in cyrillic",
                "invalid tourist",
                "empty full name",
            ],
            "document_validation": [
                "document info is duplicated",
                "document number is invalid",
                "invalid document number",
                "birth certificate cannot be used after age",
                "document expires before end of travel",
            ],
            "internal_supplier_error": [
                "Внутренняя ошибка сервера",
                "Внутренняя ошибка сервера приложений",
                "Internal server error",
                "request failed with status code 500",
                "request failed with status code 502",
                "request failed with status code 503",
                "Service Unavailable",
            ],
            "booking_failed": [
                "failed to create_booking",
                "failed to prebook",
                "prebook have failed status",
                "prebook have expired ttl",
                "booking already in progress",
            ],
        }),
    })

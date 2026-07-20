from collections import OrderedDict


def get_paks_groups():
    return OrderedDict({
        "Наши ошибки": OrderedDict({
            "package_expired": [
                "package is expired",
                "tour expired",
            ],
            "tour_dropped_by_rules": [
                "tour dropped by rules",
                "error applying rules to tour",
            ],
            "route_cache_error": [
                "error finding route in cache",
                "route not found in cache",
            ],
            "operator_mismatch": [
                "package and route have different operators",
            ],
            "empty_cast_result": [
                "empty routes after cast",
                "failed to cast routes: empty result routes",
            ],
            "rate_not_found": [
                "no rate",
                "failed to get rate",
                "unknown currency",
            ],
            "db_error": [
                "error getting package by id: query failed: invalid connection",
                "query failed: dial tcp",
                "Lost connection to MySQL server",
                "connect: connection refused",
            ],
            "cache_write_failure": [
                "failed to insert routes",
                "failed to reset fresh routes IDs",
                "error writing to cache",
                "READONLY You can't write against a read only replica",
            ],
        }),
        "Неизвестно чьи ошибки": OrderedDict({
            "request_timeout": [
                "context deadline exceeded",
                "context cancelled",
                "context canceled",
                "Client.Timeout exceeded while awaiting headers",
                "i/o timeout",
                "TLS handshake timeout",
            ],
            "transport_failure": [
                "connection reset by peer",
                "connection refused",
                "connection timed out",
                "no route to host",
                "unexpected EOF",
                "EOF",
            ],
            "invalid_payload": [
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
        "Ошибки ТО Paks": OrderedDict({
            "tour_not_found": [
                "tour not found",
                "Тур не найден",
                "заявка не найдена",
                "offer not found",
                "similar offer not found",
            ],
            "tour_not_actual": [
                "tour is not actual",
                "Тур не актуален",
                "Предложение более недоступно",
                "Предложение недоступно",
                "Поиск устарел",
                "Параметры поиска устарели",
            ],
            "no_rooms_or_quota": [
                "no availability",
                "Нет доступных мест",
                "Нет мест",
                "мест нет",
                "quota is not available",
                "квота мест закончилась",
            ],
            "no_flight_seats": [
                "No flights",
                "no flights",
                "no seats",
                "Нет мест на рейсе",
                "рейсы отсутствуют",
                "не получили подтверждение о наличии свободных мест на этом перелёте",
            ],
            "price_changed": [
                "price has changed",
                "price changed",
                "Стоимость тура изменилась",
                "цена изменилась",
            ],
            "stop_sale": [
                "stop sale",
                "room rate has expired",
                "hotel has unavailable status",
                "room is not available",
                "отель остановлен",
                "номер остановлен",
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
            "authorization": [
                "Unauthorized",
                "Пользователь не авторизован",
                "authorization failed",
                "Session expired",
            ],
            "supplier_error": [
                "Внутренняя ошибка сервера",
                "Internal server error",
                "request failed with status code 500",
                "request failed with status code 502",
                "request failed with status code 503",
                "Service Unavailable",
            ],
            "booking_failed": [
                "booking already in progress",
                "failed to create_booking",
                "failed to prebook",
                "prebook have failed status",
                "Невозможно создать заявку",
                "Не удалось создать заявку",
            ],
        }),
    })

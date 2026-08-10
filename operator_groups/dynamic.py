from collections import OrderedDict


def get_dynamic_groups():
    return OrderedDict({
        # PG
        "PG": OrderedDict({
            "Случилось переполнение числового поля": [
                "pq: numeric field overflow",
            ],
            "INSERT_in_read-only_transaction": [
                "pq: cannot execute INSERT in a read-only transaction",
            ],
            "duplicate key value violates unique constraint": [
                "idx_bookings_digest",
                "order_credentials_pkey"
            ],
            "unexpected_message": [
                "pq: unexpected message",
            ],
            "pq_invalid byte sequence":[
                "pq: invalid byte sequence for encoding \"UTF8\"",
            ],
            "Ошибка соединения": [
                "dial tcp",
                "connect: connection refused",
                "error getting package by id: query failed: invalid connection",
            ],
        }),

        # Internal Errors
        "Internal Errors": OrderedDict({
            "unknown country ID: 255" : [
                "failed to get native country: unknown ID: 255"
            ],
            "route_not_found": [
                "route not found",
            ],
            "request_id_not_found": [
                "request_id not found",
            ],
            "Бронирование уже в процессе": [
                "booking already in progress",
            ],
            "negative_charge": [
                "negative route charge in tour",
            ],
            "failed_to_parse_baggage_description": [
                "failed to parse baggage description",
            ],
            "acm_tour_empty_component_id": [
                "failed to actualize acm tour: empty component id",
            ],
            "route_empty_component": [
                "empty component_id in route component",
                "err check prebook: error casting booking: empty components",
            ],
            "route not found in tour": [
                "not found in tour"
            ],
            "tour expired": [
                "while calling concretize: while actualizing tour: tour expired"
            ],
            "Сменился класс перелета": [
                "error validating segments class: segment class mismatch: expected economy, got business",
            ],
            "Ошибка парсинга даты": [
                "error parsing in 02.01.2006 format: parsing time \"29.02.2030\": day out of range"
            ],
        }),

        # Invalid Params
        "Invalid Params": OrderedDict({
            "Невалидный номер телефона": [
                "failed to create new booking: invalid phone number",
                "empty phone",
                "invalid phone",
            ],
            "invalid_date": [
                "invalid birthday, it should be",
            ],
            "unspecified_err": [
                "invalid params",
            ],
            "Невалидное имя": [
                "invalid tourist first_name",
                "tourist name must be in latin",
                "tourist name has invalid symbols",
                "tourist name is too short",
                "empty full name",
                "empty name",
                "tourist name must be in cyrillic",
            ],
            "Невалидная фамилия": [
                "empty surname"
            ],
            "Невалидный документ": [
                "document info is duplicated",
                "document number is invalid",
                "invalid document number",
                "one or more tourists got the same documents info",
                "empty passport number",
                "non-expired passport required",
                "birthday certificate or international passport required",
                "dynamics response error: by LT: document has invalid number: invalid length",
            ],
            "Невалидная почта": [
                "validate client params err: empty email"
            ],
            "Невалидный id национальности": [
                "validate tourist params err: empty nationality ID"
            ],
        }),

        # Unsuccessful Prebook
        "Unsuccessful Prebook": OrderedDict({
            "booking management is not available": [
                "booking management is not available for this booking",
            ],
            "invalid syntax": [
                "parsing \"AX\": invalid syntax",
            ],
            "unexpected end of JSON input": [
                "unexpected end of JSON input",
            ],
            "document expires before end of travel": [
                "prebook error: by LT: document expires before end of travel",
            ],
            "birth certificate cannot be used": [
              "birth certificate cannot be used after age",
            ],
            "no route to host": [
                "prebook error: by LT: no route to host",
            ],
            "fail_to_find_similar_component": [
                "failed to find similar component",
                "offer not found",
                "failed to get offer by",
                "accommodation offer not found",
            ],
            "no_similar_route_offer_found": [
                "no similar route offer found",
                "no similar one way flight offer found",
                "no offers found for route actualization",
                "while selecting and concretizing route: dynamics response error: by LT: no similar route offer found",
                "while selecting and concretizing route: dynamics response error: by LT: no similar one way flight offer found",
            ],
            "no_similar_order_found": [
                "similar order not found",
                "failed to lock booking with similar order: booking is locked",
            ],

            "all_offers_filtered_by_rules": [
                "all offers filtered by rules",
            ],
            "perepoisk": [
                "request failed with supplier error: code 1167",
                "dynamics response error: by LT: Перепоиск не нашел рекомендаций. Пожалуйста, повторите поиск, PID",
                "dynamics response error: by LT: Внимание! Предложение более недоступно, необходимо повторить поиск",
                "dynamics response error: by LT: Перепоиск не дал результатов. Пожалуйста, создайте бронирование повторно, PID",
                "dynamics response error: by LT: Перепоиск не нашел рекомендаций. Пожалуйста, повторите поиск, PID",
                "dynamics response error: by LT: Exceeded number of requests. Contact your supervisor., PID",
                "dynamics response error: by LT: Результаты поиска устарели, пожалуйста, повторите поиск. Code - 0",
                "dynamics response error: by LT: Параметры поиска устарели, пожалуйста, повторите поиск. Code - 0",
                "dynamics response error: by LT: Поиск устарел, попробуйте произвести его ещё раз!",
            ],
            "failed to call prebook": [
                "failed to call prebook",
            ],
            "create new prebook invalid customer": [
                "empty customer last name",
            ],
            "empty response": [
                "empty prebook response",
                "empty body response",
            ],
            "dupl": [
                "one of the tourists is bound to the booked component in other active booking",
            ],
            "unspecified confirmation option": [
                "unspecified confirmation option",
            ],
            "full sold": [
                "request failed with supplier error: code 1029",
            ],
            "currency": [
                "error validating src currency",
                "error validating conversion rate: error validating from currency: unknown currency:",
            ],
            "no suitable flights found in actualization answer": [
                "no suitable flights found in actualization answer",
            ],
            "all flights are unsupported": [
                "all flights are unsupported",
            ],
            "no flights according to the specified parameters": [
                "По указанным параметрам рейсы отсутствуют",
                "no flights at research",
            ],
            "null reference exception": [
                "Object reference not set to an instance of an object.",
            ],
            "500": [
                "Внутренняя ошибка сервера приложений",
                "Service is not available",
                "code = Unavailable desc = error reading from server",
                "An error occurred while sending the request",
                "response unsuccessful with code: 500",
                "request failed with status code 500",
                "by LT: Неизвестная ошибка(Ошибка работы с базой данных)",
                "by LT: E0500, message: Предложение недоступно"
            ],
            "502": [
                "response unsuccessful with code: 502",
                "request failed with status code 502",
                "502 Bad Gateway"
            ],
            "503": [
                "status: 503",
                "Сервер перегружен. Пожалуйста, повторите запрос",
                "dynamics response error: by LT: request failed with status code 503",
            ],
            "no_error_debug": [
                "NO_ERROR, debug data",
            ],
            "typecode_en": [
                "TypeCode",
            ],
            "token_not_from_search": [
                "токен получен не из search, источник select Code - 0",
            ],
            "test_data": [
                "tourist name has test format",
            ],
            "invalid_json_in_response": [
                "invalid character '<' looking for beginning of value",
                "json unmarshal error: invalid character '<' looking for beginning of value",
                "error decoding prebook resp: json unmarshal error",
            ],
            "tour_expired": [
                "by LT: Что-то пошло не так",
                "не найдены или срок действия истек",
                "by LT: This room rate has expired!, status",
                "by LT: 8546: Предложение не актуально!",
            ],
            "retrieving detail error": [
                "retrieving detail error",
            ],
            "Неправильно определил кол-во взрослых и детей": [
                "by LT: found -"
            ],
            "build airline id  failed": [
                "build airline id  failed",
            ],
            "forward and backward flights must have the same number of adults": [
                "forward and backward flights must have the same number of adults"
            ],
            "error in XML document": [
                "dynamics response error: by LT: There is an error in XML document",
            ],
            "no suitable routes found in actualization answer": [
                "no suitable routes found in actualization answer",
                "dynamics response error: by LT: Остутствуют результаты в ответе актуализации",
            ],
            "No offers available": [
                "dynamics response error: by LT: No offers available| Code - 0",
            ],
            "Предложение больше не действительно": [
                "Предложение больше не действительно",
            ],
            "Слишком много запросов" : [
                "dynamics response error: by LT: Слишком много запросов. type",
            ],
            "Maximum simultanous connections" : [
                "by LT: 15 error: Maximum simultanous connections",
            ],
            "empty components": [
                "fail to prebook acm tour: error casting booking: empty components",
            ],
        }),

        # Dynamic Errors
        "Dynamic Errors": OrderedDict({
            "failed_count": [
                "STATUS_FAILED",
                "STATUS_CANCELED",
                "prebook have failed status",
                "Response status code does not indicate success",
                "i/o timeout",
                "Не удалось дождаться ответа от поставщика"
            ],
            "component not available": [
                "component not available",
            ],
            "deadlock detected": [
                "while calling prebook: prebook error: by LT: pq: deadlock detected",
            ],
            "error create booking" : [
                "error create booking: empty booking response",
            ],
            "tour is not available for booking": [
                "tour is not available for booking",
            ],
            "no routes found": [
                "no routes found",
            ],
            "empty booking response": [
                "err check prebook: empty booking response",
            ],
            "Запрашиваемые рейсы неактуальны": [
                "Запрашиваемые рейсы для OfferId"
            ],
            "fail get routes": [
                "ERR Unknown subcommand or wrong number of arguments for",
            ],
            "mismatch tourists": [
                "the number of adults and children in the component does not match the tourists data",
                "kids ages mismatch"
            ],
            "failed_load_component": [
                "failed to load component by id",
            ],
            "different_organizations": [
                "different organizations in bundle",
            ],
            "unknown organization": [
                "by LT: invalid organization: unknown organization",
            ],
            "error getting component from cache": [
                "error getting component from cache",
            ],
            "timeout": [
                "context deadline exceeded",
                "couldn&#39;t actualize component",
                "last connection error: connection error:",
                "broninit call failed",
                "error from waitgroup",
                "context canceled",
                "connection reset by peer",
                "Connection timed out",
                "EOF",
                "prebook have expired ttl",
                "Превышено время ожидания ответа от туроператора",
                "proxyconnect tcp: net/http: TLS handshake timeout",
                "net/http: TLS handshake timeout",
            ],
            "Internal Server Error" : [
                "dynamics response error: by LT: Система не может подтвердить класс бронирования. Пожалуйста, выберите другой перелёт, PID",
                "dynamics response error: by LT: Сервис временно недоступен. Пожалуйста, повторите запрос через несколько минут, PID",
                "dynamics response error: by LT: Не удалось обработать запрос. Передайте PID этого ответа нашему саппорту., PID",
                "dynamics response error: by LT: Неизвестная ошибка(Сервер занят. Пожалуйста, повторите попытку позже.)",
                "by LT: Бронирование остановлено по причине: Internal Server Error",
                "dynamics response error: by LT: Неизвестная ошибка(Ошибка работы с базой данных)",
                'by LT: //meta.online-express.ru/api/v2/accommodations/search?checkInDate=2026-06-01&checkOutDate=2026-06-18&currency=RUB&hotelId=224669&rooms%5B0%5D%5Badults%5D=2&rooms%5B0%5D%5Bchildren%5D=0": Service Unavailable',
                "dynamics response error: by LT: expected element type <HotelPricingResponse2> but have <html>",
                'dynamics response error: by LT: short_rus="2 места", rus="2 места", short_eng="", eng=""',
                "dynamics response error: by LT: expected element type <tours> but have <html>",
                "dynamics response error: by LT: expected element type <Envelope> but have <html>",
                "dynamics response error: by LT: code = Unavailable desc = upstream connect error or disconnect/reset before headers. reset reason",
                "dynamics response error: by LT: Разрыв соединения с системой бронирования. Если Вы пытались выписать или аннулировать билет, то необходимо обратиться в колл-центр для проверки статуса бронирования. Code - 0",
                "by LT: failed to get place supplier credentials from server: credentials not found",
                "dynamics response error: by LT: SoapServer->handle()",
                "dynamics response error: by LT: Внутренняя ошибка сервера, обратитесь к туроператору",
            ],
            "no_available_rates": [
                "dynamics response error: by LT: response error",
                "dynamics response error: by LT: minimum retail price is empty for offer",
                "dynamics response error: by LT: status - error, error - no_available_rates, debug - , status",
            ],
            "response error" : [
                "dynamics response error: by LT: response error"
            ],
            "no accommodations found": [
                "dynamics response error: by LT: no accommodations found in actualization search by hotel"
            ],
            "no active actual routes": [
                "dynamics response error: by LT: no active actual routes found with force method"
            ],
            "Не удалось подтвержить наличии свободных мест на перелет" : [
                "dynamics response error: by LT: К сожалению, мы не получили подтверждение о наличии свободных мест на этом перелёте."
            ],
            "bundle ID mismatch": [
                "while calling create booking: create booking error: by LT:", # Временная замена, так как не можем нормально распарсить  {"booking":null,"request_info":{"code":0,"error":{"cause":{"cause":null,"code":500,"detalization":{"critical":false,"http_status":0,"supplier_code":0},"message":"failed to create booking in meta middleware: failed to create booking in validation middleware: error finding or creating booking: handler failed to find or create booking: failed to find or create booking in logging middleware: failed to build booking: failed to load bundles: bundle ID mismatch: expected 01|230402Ic5vomOK::8eOnl9RT7O|310401toU9_O9q::MtLNoUW3::zEIsJwo9ff|090404B1JLvMZd::IgrXaK55yO, got 01|230402Ic5vomOK::8eOnl9RT7O|310401toU9_O9q::MtLNoUW3::j4dGgSsmLf|090404B1JLvMZd::IgrXaK55yO","type":"ERROR_TYPE_INTERNAL"},"code":500,"detalization":{"critical":false,"http_status":0,"supplier_code":0},"message":"Internal server error (from middleware)","type":"ERROR_TYPE_INTERNAL"},"request_id":"2a22ebef-f6fb-4b5a-a98c-8502a8c76574","warnings":[]}}
                "failed to create_booking: response failed: dynamics response error: by LT",
            ],
        }),
    })

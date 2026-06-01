import os
import csv
from collections import defaultdict, OrderedDict
from typing import Dict, Tuple, List
import html


# ====================== УТИЛИТЫ ======================
def normalize(s: str) -> str:
    return html.unescape((s or "").strip()).casefold()


def find_bucket_and_key(
    error_groups: "OrderedDict[str, OrderedDict[str, List[str]]]",
    text_norm: str
) -> Tuple[str, str]:
    for group_name, group_map in error_groups.items():
        for short_key, patterns in group_map.items():
            for p in patterns:
                if normalize(p) in text_norm:
                    return group_name, short_key
    return None, None


def read_csv_rows(path: str) -> List[Tuple[str, int]]:
    """
    Читает CSV и возвращает [(text, count), ...].
    Первая строка файла ВСЕГДА игнорируется (считаем её заголовком).
    Ожидается: первая колонка — текст ошибки, вторая — количество (или пусто -> 1).
    """
    rows: List[Tuple[str, int]] = []
    with open(path, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        # пропускаем заголовок без условий
        next(reader, None)

        for row in reader:
            if not row:
                continue
            text = (row[0] or "").strip()
            if not text:
                continue
            try:
                count = int(row[1])
            except Exception:
                count = 1
            rows.append((text, count))
    return rows


# ====================== ОСНОВНАЯ ЛОГИКА ======================
def process_errors(
    error_groups: "OrderedDict[str, OrderedDict[str, List[str]]]",
    rows: List[Tuple[str, int]]
):
    """
    Возвращает:
      counters[group][short_key] = count,
      unclassified[label] = count,
      group_totals[group] = total_in_group,
      overall_total
    """
    counters: Dict[str, defaultdict] = {g: defaultdict(int) for g in error_groups.keys()}
    unclassified: defaultdict = defaultdict(int)

    for text, count in rows:
        g, k = find_bucket_and_key(error_groups, normalize(text))
        if g is None:
            if ": " in text:
                normalized_tail = ": ".join(text.split(": ")[-3:])
            else:
                normalized_tail = text
            label = "Ошибка искусственная: " + normalized_tail
            unclassified[label] += count
        else:
            counters[g][k] += count

    group_totals = OrderedDict()
    for group_name in error_groups.keys():
        group_totals[group_name] = sum(counters[group_name].values())
    if unclassified:
        group_totals["UNCLASSIFIED"] = sum(unclassified.values())

    overall_total = sum(group_totals.values())
    return counters, unclassified, group_totals, overall_total


def _merged_group_totals_for_summary(group_totals: "OrderedDict[str, int]") -> "OrderedDict[str, int]":
    """
    Для блока 'СВОД ПО ГРУППАМ' объединяем:
      'Unsuccessful Prebook' + 'Dynamic Errors' -> 'Prebook + Dynamic Errors'
    Остальные группы выводим как есть и в исходном порядке.
    """
    prebook_key = "Unsuccessful Prebook"
    dynamic_key = "Dynamic Errors"
    merged_label = "Prebook Errors"

    pre = group_totals.get(prebook_key, 0)
    dyn = group_totals.get(dynamic_key, 0)
    merged_value = pre + dyn

    out = OrderedDict()
    merged_done = False

    for k, v in group_totals.items():
        if k == prebook_key or k == dynamic_key:
            if not merged_done:
                out[merged_label] = merged_value
                merged_done = True
            continue
        out[k] = v

    return out


def print_detailed_tables(counters, unclassified, group_totals, overall_total):
    for group_name, group_counts in counters.items():
        if not group_counts:
            continue
        print(group_name)
        for key, value in sorted(group_counts.items(), key=lambda x: (-x[1], x[0])):
            # print(f"- {key} - {value} шт")
            print(f"{key}\t{value}")
        print()

    if unclassified:
        print("=== UNCLASSIFIED ===")
        for key, value in sorted(unclassified.items(), key=lambda x: (-x[1], x[0])):
            print(f"- {key} - {value} шт")
        print()

    print("==== СВОД ПО ГРУППАМ ====")
    merged_totals = _merged_group_totals_for_summary(group_totals)

    for g, v in merged_totals.items():
        part = (v / overall_total * 100) if overall_total else 0.0
        print(f"- {g}: {v} шт ({part:.1f}%)")

    print(f"ИТОГО: {overall_total} шт\n")


# ====================== ПРОФИЛИ ГРУПП ======================
def get_pegast_tez_groups():
    return OrderedDict({
        "Наши ошибки ": OrderedDict({
            "package not found into db": [
                "error building domain package: package not found",
            ],
            "proxy server misbehaving": [
                "dial tcp: lookup px-n.internal.lvtv.me. on 10.96.0.10:53: server misbehaving",
            ],
            "failed to reset fresh routes IDs": [
                "failed to reset fresh routes IDs: failed to reset fresh routes IDs: READONLY You can't write against a read only replica."
            ],
            "error storing concretization tour price to cache": [
                "error storing concretization tour price to cache: error saving data to redis: READONLY You can't write against a read only replica."
            ],
            "Deadlock found when trying to get lock" : [
                "failed to update package: Error 1213 (40001): Deadlock found when trying to get lock; try restarting transaction",
            ],
            "failed to get rate from db": [
                "de = Internal desc = failed to get rate from db: Error 2013 (HY000): Lost connection to MySQL server during query",
            ],
            "denied by rate-limiter": [# Общая
                "request denied by rate-limier",
            ],
            "write to read-only MySQL server": [ # Общая
                "Error 1290 (HY000): The MySQL server is running with the --read-only option so it cannot execute this statement",
            ],
            "package is expired": [ # Общая
                "package is expired",
            ],
            "no present match": [ # Общая
                "failed to get extra kupala sri lanka: no present match",
                "failed to get extra nevylet kupala china 3000: no present match",
                "failed to get extra gelios vietnam: no present match",
                "failed to get extra gelios georgia ski: no present match",
                "failed to get extra kupala vietnam: no present match",
                "failed to get extra matching: no present match",
            ],
            "tour dropped by rules": [ # Общая
                "tour dropped by rules",
            ],
            "error finding route in cache": [ # Общая
                "error finding route in cache",
            ],
            "failed to get rate": [
                "no rate",
            ],
            "different origin and return places": [
                "different origin and return places",
            ],
            "package and route have different operators": [
                "package and route have different operators",
            ],
            "error writing to cache":[ # Общая
                "failed to insert routes: server selection error: server selection timeout, current topology: { Type: ReplicaSetNoPrimary",
                "failed to insert routes: (InterruptedDueToReplStateChange) operation was interrupted",
                "failed to insert routes: (NotWritablePrimary) not primary",
                "failed to reset fresh routes IDs: EOF",
                "error writing to cache: error in routes: failed to reset fresh routes IDs: failed to reset fresh routes IDs: dial tcp 62.84.125.225:6380: i/o timeout",
                "failed to update duplicates created_at: failed to perform bulk write operation: must provide at least one element in input slice",
            ],

            "hotel has unavailable status": [
                "hotel has unavailable status",
            ],
            "invalid flight number": [
                "invalid flight number",
            ],
            "no children to pick from": [
                "no children to pick from",
            ],

            "sql: no rows in result set": [
              "query failed: sql: no rows in result set",
            ],


            "response unsuccessful with code: 404": [
                "response unsuccessful with code: 404",
            ],
            "Требуется авторизация:": [
                "Full authentication is required to access this resource",
            ],
            "failed to get \"actualization:tez:flight-rules\" from redis" : [
                "failed to get \"actualization:tez:flight-rules\" string: redis: nil",
            ],
            "Ошибка с соединением": [
                "connect: no route to host",
                "failed to update package: invalid connection",
                "failed to select client good state orders: invalid connection",
                "failed to get rate from db: invalid connection",
                "error getting package by id: query failed: invalid connection",
                "rpc error: code = Unavailable desc = upstream connect error or disconnect/reset before headers. reset reason: connection timeout"
            ],
        }),
        "Неизвестно чьи ошибки": OrderedDict({
            "TLS handshake timeout": [
                "proxyconnect tcp: net/http: TLS handshake timeout",
                "net/http: TLS handshake timeout",
            ],
            "empty routes after cast": [
                "empty routes after cast",
            ],

            "failed to cast routes: empty result routes": [
                "failed to cast routes: empty result routes",
            ],
            "route not found in operator flights": [
                "route not found in operator flights"
            ],
            "NOREPLICAS Not enough good replicas to write":[
                "NOREPLICAS Not enough good replicas to write"
            ],
            "failed to insert routes to cache": [
                "failed to insert routes: (InterruptedDueToReplStateChange) operation was interrupted",
                "failed to insert routes: (NotWritablePrimary) not primary",
                "failed to insert routes: (NotWritablePrimary) Not primary so we cannot begin or continue a transaction",
            ],
            "unexpected EOF": [
                "packageBookingCreation failed: response unsuccessful with err Post \"https://api-ext.pegasys.pegast.com/PackageBookingCreation.svc\": unexpected EOF"
            ]
        }),
        "Ошибки ТО": OrderedDict({
            "FULL_PAID_FLAG": [ #TEZTOUR
                "response unsuccessful with code: Произошла ошибка в вычислении FULL_PAID_FLAG.",
            ],
            "Не найдена авиакомпания": [
                "response unsuccessful with code: Не найдена авиакомпания (carrier=C6)."  #TEZTOUR
            ],
            "invalid_xml_in_response": [
                "response build_order decode unsuccessful with err xml unmarshal error",
                "response decode unsuccessful with err xml unmarshal error: xml: (*api.AuthorizeResponse).UnmarshalXML did not consume entire <html> element",
            ],

            "failed to cast routes: empty result routes": [
                "failed to cast routes: empty result routes",
            ],
            "ParametersNotValid": [ #PEGAST
                "fail in construct booking: api response error: ParametersNotValid"
            ],
            "PackageInactiveBookingPeriod": [ #PEGAST
              "fail in construct booking: api response error: PackageInactiveBookingPeriod"
            ],
            "failed to verify certificate": [
                "failed to verify certificate: x509: certificate has expired or is not yet valid",
            ],
            "context canceled": [
                "context deadline exceeded",
                "connection timed out",
                "connection refused",
                "connection reset by peer",
                "context cancelled",
                "context canceled",
                "i/o timeout",
                "Error 9001 (HY000): Max connect timeout reached while reaching hostgroup"

            ],
            "InvalidBooking": [
                "fail in get insurance: api response error: InvalidBooking"
            ],
            "CannotFindEnoughResponsibleAdultsForAllInfants": [
                "fail in construct booking: api response error: CannotFindEnoughResponsibleAdultsForAllInfants",
            ],
            "...ORA-06512: at line 1": [
                "ORA-06512",
            ],
            "get empty flight pairs arr after parse": [
                "err parse regular flights: get empty flight pairs arr after parse",
            ],
            "internal server error": [
                "code 502",
                "response unsuccessful with code: 500",
                "Произошла системная ошибка: null",
                "response unsuccessful with code: 502",
                "The server sent HTTP status code 503",
                "response unsuccessful: code 503",
                "response unsuccessful with code: systemError",
                "The server sent HTTP status code 503: Service Unavailable",
                "response unsuccessful with err Post \"https://api-ext.pegasys.pegast.com/PackageBookingCreation.svc\": Service Unavailable",
                "response unsuccessful with code: 503",
                "response unsuccessful with code: Произошла системная ошибка: Session/EntityManager is closed",
                "response unsuccessful with code: Nemo currency is null!",
                "Client received SOAP Fault from server: Cannot access a disposed object." #TEZTOUR
            ],
            "code=[0]": [ #TEZTOUR
                "response unsuccessful with code: code=[0], [Error from supplier (No flights)]",
                "response unsuccessful with code: code=[0, 0], [Error from supplier (Too many requests), Error from supplier (No flights)]",
                "response unsuccessful with code: code=[0], [Error from supplier (Сервис временно недоступен. Повторите попытку через 60 секунд.)]",
                "response unsuccessful with code: code=[0], [Error from supplier (Invalid Country Code )]",
                "response unsuccessful with code: code=[0], [Error from supplier (Invalid Authorization )]",
                "response unsuccessful with code: code=[0], [Error from supplier (Internal service error. Please contact support.)]",
                "response unsuccessful with code: code=[0], [Error from supplier (Unknown supplier error)]",
                "response unsuccessful with code: code=[0], [Error from supplier (Unknown accel aero error)]",
                "response unsuccessful with code: code=[0], [Error from supplier (Внутренняя ошибка сервиса. Обратитесь в службу технической поддержки",
                "response unsuccessful with code: code=[0], [Error from supplier (Внутренняя ошибка сервера",
                "response unsuccessful with code: code=[0], [Error from supplier (No availability)]",
                "response unsuccessful with code: code=[0], [Error from supplier (Too many requests)]",
                "response unsuccessful with code: code=[0, 0], [Error from supplier (Too many requests), Error from supplier (Unknown accel aero error)]",
                "response unsuccessful with code: code=[0], [Error from supplier (Invalid Place of Destination Code )]",
                "response unsuccessful with code: code=[0], [Error from supplier (Search limit has been reached)]",
                "response unsuccessful with code: code=[0], [Error from supplier ( )]",
                "response unsuccessful with code: code=[0, 0], [Error from supplier (Internal service error. Please contact support.), Error from supplier ( )]",
                "response unsuccessful with code: code=[0], [Error from supplier (Invalid Place of Departure Code )]",
                "response unsuccessful with code: code=[0], [Error from supplier (No flights)]",
                "response unsuccessful with code: code=[0, 0], [Error from supplier (No flights), Error from supplier (Too many requests)]",
                "response unsuccessful with code: code=[0, 0], [Error from supplier (No flights), Error from supplier (Unknown accel aero error)]",
                "response unsuccessful with code: code=[0, 0], [Error from supplier (Unknown accel aero error), Error from supplier (No flights)]",
                "response unsuccessful with code: code=[0, 0], [Error from supplier (Unknown accel aero error), Error from supplier (Too many requests)]",
                "response unsuccessful with code: code=[0], [Error from supplier (XID 14988EA2A80 - HTTP: host ek-os-servicebagency.prod.proscloud.com on port 443 - socket connect failed -5990)]",
            ],
            "code=[1000]" : [ #TEZTOUR
                "response unsuccessful with code: code=[1000], [Infants count can not be more than adult count]",
            ],
            "code=[1002]": [ #TEZTOUR
                "response unsuccessful with code: code=[1002], [Error while contacting the supplier. (42|Application|Too many opened conversations. Please close them and try again.)]",
                "response unsuccessful with code: code=[1002], [An unexpected error occurred, please contact technical support.]",
                "response unsuccessful with code: code=[1002], [No response from supplier]",
                "response unsuccessful with code: code=[1002], [The given key 'SEG6_' was not present in the dictionary.]",
            ],
            "code=[1030]": [ #TEZTOUR
                "response unsuccessful with code: code=[1030], [Received an unexpected EOF or 0 bytes from the transport stream.]",
                "response unsuccessful with code: code=[1030], [The response ended prematurely. (ResponseEnded)]",
                "response unsuccessful with code: code=[1030], [Authentication failed, see inner exception.]",
                "response unsuccessful with code: code=[1030], [Unable to read data from the transport connection: An existing connection was forcibly closed by the remote host..]",
                "response unsuccessful with code: code=[1030], [Unable to read data from the transport connection: Удаленный хост принудительно разорвал существующее подключение..]",
                "response unsuccessful with code: code=[1030], [A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond.]",
                "response unsuccessful with code: code=[1030], [Invalid not empty response. Status description: Bad Gateway]",
                "response unsuccessful with code: code=[1030], [Invalid not empty response. Status description: Internal Server Error]",
                "response unsuccessful with code: code=[1030], [Invalid not empty response. Status description: Request Time-out]",
            ],
            "code=[0, 1002]": [ #TEZTOUR
                "response unsuccessful with code: code=[0, 1002], [Error from supplier (No flights), No response from supplier]",
                "response unsuccessful with code: code=[0, 1002], [Error from supplier (No availability), No response from supplier]",
                "response unsuccessful with code: code=[1002, 0], [An unexpected error occurred, please contact technical support., Error from supplier (Unknown supplier error)]",
                "response unsuccessful with code: code=[1002, 0], [No response from supplier, Error from supplier (No flights)]",
                "response unsuccessful with code: code=[1002, 0], [No response from supplier, Error from supplier (Unknown accel aero error)]",
                "response unsuccessful with code: code=[0, 1002], [Error from supplier (Unknown accel aero error), No response from supplier]",
            ],
            "code=[0, 1030]": [ #TEZTOUR
                "code=[0, 1030], [Error from supplier (Internal service error. Please contact support.)",
                "response unsuccessful with code: code=[1030], [Unable to read data from the transport connection: An existing connection was forcibly closed by the remote host..]",
                "response unsuccessful with code: code=[1030], [Unable to read data from the transport connection: Удаленный хост принудительно разорвал существующее подключение..]",
            ],
            "code=[1014]" : [ #TEZTOUR
                "response unsuccessful with code: code=[1014], [Error from supplier (JOURNEY SERVER: System problem (check OID))]",
            ],
            "Не найден пользователь (ID=null)": [
                "response unsuccessful with code: Не найден пользователь (ID=null).",
            ],
            "response unsuccessful airport": [
                "response unsuccessful with code: Не найден аэропорт (id=null).",
            ],
            "Unauthorized": [
                "response unsuccessful with code: Unauthorized",
                "request failed with supplier error: Пользователь не авторизован"
            ],
            "SystemTemporarilyUnavailable": [ #PEGAST
                "SystemTemporarilyUnavailable"
            ],
            "RequestFailedUnexpectedly": [ #PEGAST
                "RequestFailedUnexpectedly"
            ],
            "BookingCannotBeConstructed": [ #PEGAST
                "BookingCannotBeConstructed"
            ],
            "PackageSpoNotActual": [ #PEGAST
                "PackageSpoNotActual"
            ],
            "PackageSpoInactiveBookingPeriod": [ #PEGAST
                "PackageSpoInactiveBookingPeriod",
            ],
            "MaxBookingDateTimeExpired": [ #PEGAST
                "MaxBookingDateTimeExpired",
            ],
            "concretized route has changed id": [
                "concretized route has changed id",
            ],

            "Пустой ответ": [
                "api response error: None",
                "error CollectAllFlights tour: %!w(<nil>)"
            ],
            "empty optional routes": [
                "empty optional routes"
            ],
            "empty round trip flight services": [
                "empty round trip flight services",
            ],
            "response build_order unsuccessful with err Post": [
                "response build_order unsuccessful with err Post",
            ],
            "response search_flights unsuccessful with err Post": [
                "response search_flights unsuccessful with err Post",
            ],
            "Residences not found in a special offer": [
                "response unsuccessful with code: Residences not found in a special offer"
            ],
            "error convert full price, empty field price in calc_resp": [
                "err calculate fuel charge for flights: convert full price from calculate data err: parse  to amount failed: strconv.ParseFloat:",
            ],
            "failed to cast insurances, insurance field price is empty": [
                "failed to cast insurances: parse insurance price err: parse  to amount failed: strconv.ParseFloat:",
            ],
        }),
    })


def get_dynamic_groups():
    return OrderedDict({
        # PG
        "PG": OrderedDict({
            "Случилось переполнение числового поля": [
                "pq: numeric field overflow",
            ],
            "pg_INSERT_in_read-only_transaction": [
                "pq: cannot execute INSERT in a read-only transaction",
            ],
            "duplicate key value violates unique constraint": [
                "idx_bookings_digest",
                "order_credentials_pkey"
            ],
            "pg_unexpected_message": [
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
            "route_empty_component_id": [
                "empty component_id in route component",
            ],
            "route not found in tour": [
                "not found in tour"
            ],
            "tour expired": [
                "while calling concretize: while actualizing tour: tour expired"
            ],

        }),

        # Invalid Params
        "Invalid Params": OrderedDict({
            "Невалидный номер телефона": [
                "failed to create new booking: invalid phone number",
                "empty phone",
                "invalid phone",
                "invalid length",
            ],
            "invalid_params_invalid_date": [
                "invalid birthday, it should be",
            ],
            "invalid_params_unspecified_err": [
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
                "non-expired passport required"
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
                "while selecting and concretizing route: tour expired: by LT: no similar route offer found",
                "while selecting and concretizing route: tour expired: by LT: no similar one way flight offer found",
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
                "tour expired: by LT: Перепоиск не нашел рекомендаций. Пожалуйста, повторите поиск, PID",
                "tour expired: by LT: Внимание! Предложение более недоступно, необходимо повторить поиск",
                "tour expired: by LT: Перепоиск не дал результатов. Пожалуйста, создайте бронирование повторно, PID"
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
                "request failed with status code 500"

            ],
            "502": [
                "response unsuccessful with code: 502",
                "request failed with status code 502",
                "502 Bad Gateway"
            ],
            "503": [
                "status: 503",
                "Сервер перегружен. Пожалуйста, повторите запрос"
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
                "не найдены или срок действия истек"
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
                "tour expired: by LT: There is an error in XML document",
            ],
            "no suitable routes found in actualization answer": [
                "no suitable routes found in actualization answer"
            ],
            "Предложение больше не действительно": [
                "Предложение больше не действительно",
            ],
            "Слишком много запросов" : [
                "tour expired: by LT: Слишком много запросов. type",
            ],
            "Maximum simultanous connections" : [
                "by LT: 15 error: Maximum simultanous connections",
            ],

            "tour expired": [
                # "while calling concretize: while actualizing tour: tour expired",
            #     "while actualizing tour: tour expired",
            #     "while changing route: tour expired",
            #     "by LT: One or more errors occurred. (Error from supplier)",
            #     "by LT: 176242988882209831 Code - 0",
            #     "Произошла ошибка при выполнении запроса актуализации",
            #     "while selecting and concretizing route: tour expired",
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
                "by LT: Бронирование остановлено по причине: Internal Server Error",
                "tour expired: by LT: Неизвестная ошибка(Ошибка работы с базой данных)",
                'by LT: //meta.online-express.ru/api/v2/accommodations/search?checkInDate=2026-06-01&checkOutDate=2026-06-18&currency=RUB&hotelId=224669&rooms%5B0%5D%5Badults%5D=2&rooms%5B0%5D%5Bchildren%5D=0": Service Unavailable',
                "tour expired: by LT: expected element type <HotelPricingResponse2> but have <html>",
                'tour expired: by LT: short_rus="2 места", rus="2 места", short_eng="", eng=""',
            ],
            "response error" : [
                "tour expired: by LT: response error"
            ],
            "no accommodations found": [
                "tour expired: by LT: no accommodations found in actualization search by hotel"
            ],
            "no active actual routes": [
                "tour expired: by LT: no active actual routes found with force method"
            ],
            "Не удалось подтвержить наличии свободных мест на перелет" : [
                "tour expired: by LT: К сожалению, мы не получили подтверждение о наличии свободных мест на этом перелёте."
            ],
            "bundle ID mismatch": [
                "while calling create booking: create booking error: by LT:", # Временная замена, так как не можем нормально распарсить  {"booking":null,"request_info":{"code":0,"error":{"cause":{"cause":null,"code":500,"detalization":{"critical":false,"http_status":0,"supplier_code":0},"message":"failed to create booking in meta middleware: failed to create booking in validation middleware: error finding or creating booking: handler failed to find or create booking: failed to find or create booking in logging middleware: failed to build booking: failed to load bundles: bundle ID mismatch: expected 01|230402Ic5vomOK::8eOnl9RT7O|310401toU9_O9q::MtLNoUW3::zEIsJwo9ff|090404B1JLvMZd::IgrXaK55yO, got 01|230402Ic5vomOK::8eOnl9RT7O|310401toU9_O9q::MtLNoUW3::j4dGgSsmLf|090404B1JLvMZd::IgrXaK55yO","type":"ERROR_TYPE_INTERNAL"},"code":500,"detalization":{"critical":false,"http_status":0,"supplier_code":0},"message":"Internal server error (from middleware)","type":"ERROR_TYPE_INTERNAL"},"request_id":"2a22ebef-f6fb-4b5a-a98c-8502a8c76574","warnings":[]}}
            ],
        }),
    })


# ====================== CLI ======================
def main():
    print("Кого считаем?\n  1 — Пегас/ТезТур\n  2 — Динамика")
    while True:
        choice = input("Введи 1 или 2: ").strip()
        if choice in ("1", "2"):
            break
        print("Некорректный ввод. Введи 1 или 2.")

    error_groups = get_pegast_tez_groups() if choice == "1" else get_dynamic_groups()

    default_path = "Edit visualization.csv"
    user_path = input(f"Путь к CSV [{default_path}]: ").strip() or default_path
    if not os.path.exists(user_path):
        raise FileNotFoundError(f"Файл не найден: {user_path}")

    print("------------------------------------------")

    rows = read_csv_rows(user_path)

    # raw_total = sum(count for _, count in rows)
    # print(f"Всего записей по данным CSV: {raw_total}")

    counters, unclassified, group_totals, overall_total = process_errors(error_groups, rows)
    print_detailed_tables(counters, unclassified, group_totals, overall_total)


if __name__ == "__main__":
    main()

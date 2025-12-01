# errors_report_csv.py  — CSV only, no charts, merged summary for Prebook+Dynamic
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
                # вставляем объединённую строку на месте первой встреченной из двух
                out[merged_label] = merged_value
                merged_done = True
            # вторую из них пропускаем
            continue
        out[k] = v

    # если обеих не было, ничего не меняем; если была только одна — она уже стала merged_label с тем же значением
    return out


def print_detailed_tables(counters, unclassified, group_totals, overall_total):
    # Детали по группам (без локальных "Всего: ...")
    for group_name, group_counts in counters.items():
        if not group_counts:
            continue
        print(group_name)
        for key, value in sorted(group_counts.items(), key=lambda x: (-x[1], x[0])):
            print(f"- {key} - {value} шт")
            # print(f"{key}\t{value}")
        print()

    if unclassified:
        print("=== UNCLASSIFIED ===")
        for key, value in sorted(unclassified.items(), key=lambda x: (-x[1], x[0])):
            print(f"- {key} - {value} шт")
        print()

    # Свод по группам — с объединением Prebook+Dynamic
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
            "package is expired": [
                "package is expired",
            ],
            "no present match": [
                "failed to get extra kupala sri lanka: no present match",
                "failed to get extra nevylet kupala china 3000: no present match",
            ],
            "tour dropped by rules": [
                "tour dropped by rules",
            ],
            "error finding route in cache": [
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

            "hotel has unavailable status": [
                "hotel has unavailable status",
            ],
            "invalid flight number": [
                "invalid flight number",
            ],
            "no children to pick from": [
                "no children to pick from",
            ],
            "response unsuccessful with code: 404": [
                "response unsuccessful with code: 404",
            ],
            "Требуется авторизация:": [
                "Full authentication is required to access this resource",
            ],
            "failed to get \"actualization:tez:flight-rules\" from redis" : [
                "failed to get \"actualization:tez:flight-rules\" string: redis: nil",
            ]
        }),
        "Неизвестно чьи ошибки": OrderedDict({
            "empty routes after cast": [
                "empty routes after cast",
            ],
            "Ошибка с соединением": [
                "connect: no route to host",
                "failed to update package: invalid connection",
                "failed to select client good state orders: invalid connection",
            ],
            "failed to cast routes: empty result routes": [
                "failed to cast routes: empty result routes",
            ],
            "route not found in operator flights": [
                "route not found in operator flights"
            ],
            "NOREPLICAS Not enough good replicas to write":[
                "NOREPLICAS Not enough good replicas to write"
            ]

        }),
        "Ошибки ТО": OrderedDict({
            "context canceled": [
                "context deadline exceeded",
                "connection timed out",
                "connection refused",
                "connection reset by peer",
                "context cancelled",
                "i/o timeout",
                "Error 9001 (HY000): Max connect timeout reached while reaching hostgroup"

            ],
            "InvalidBooking": [
                "fail in get insurance: api response error: InvalidBooking"
            ],
            "Too many requests": [
                "Error from supplier (Too many requests)",
            ],
            "...ORA-06512: at line 1": [
                "ORA-06512",
            ],
            "err parse regular flights: get empty flight pairs arr after parse": [
                "err parse regular flights: get empty flight pairs arr after parse",
            ],
            "internal server error": [
                "code 502",
                "response unsuccessful with code: 500",
                "response unsuccessful with code: 502",
                "The server sent HTTP status code 503",
                "response unsuccessful: code 503",
                "response unsuccessful with code: code=[0], [Error from supplier (Internal service error. Please contact support.)]",
                "response unsuccessful with code: code=[0], [Error from supplier (Unknown supplier error)]",
                "response unsuccessful with code: code=[0], [Error from supplier (Unknown accel aero error)]",
                "response unsuccessful with code: code=[0], [Error from supplier (Внутренняя ошибка сервиса. Обратитесь в службу технической поддержки",
                "response unsuccessful with code: code=[0], [Error from supplier (Внутренняя ошибка сервера",
                "response unsuccessful with code: systemError",
                "code=[0, 1030], [Error from supplier (Internal service error. Please contact support.)",
                "response unsuccessful with code: Произошла системная ошибка:"
            ],
            "SystemTemporarilyUnavailable": [
                "SystemTemporarilyUnavailable"
            ],
            "RequestFailedUnexpectedly": [
                "RequestFailedUnexpectedly"
            ],
            "BookingCannotBeConstructed": [
                "BookingCannotBeConstructed"
            ],
            "PackageSpoNotActual": [
                "PackageSpoNotActual"
            ],
            "PackageSpoInactiveBookingPeriod": [
                "PackageSpoInactiveBookingPeriod",
            ],
            "MaxBookingDateTimeExpired": [
                "MaxBookingDateTimeExpired",
            ],
            "concretized route has changed id": [
                "concretized route has changed id",
            ],
            "code=[1002]": [
                "code=[1002",
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
            "response unsuccessful airport": [
                "response unsuccessful with code: Не найден аэропорт (id=null).",
            ],
            "Unauthorized": [
                "response unsuccessful with code: Unauthorized",
                "request failed with supplier error: Пользователь не авторизован"
            ],
            "code=[1030]": [
                "code=[1030",
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
            "parse to amount failed": [
                "convert full price from calculate data err: parse  to amount failed",
                "failed to parse price: parse  to amount failed",
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
            "Дублирование значений": [
                "idx_bookings_digest",
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
            ],
            "Невалидная почта": [
                "validate client params err: empty email"
            ]
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
            "tour expired": [
                "while actualizing tour: tour expired",
                "while changing route: tour expired",
                "by LT: One or more errors occurred. (Error from supplier)",
                "by LT: 176242988882209831 Code - 0",
                "Произошла ошибка при выполнении запроса актуализации",
                "while selecting and concretizing route: tour expired",
            ],
            "birth certificate cannot be used": [
              "birth certificate cannot be used after age",
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
                "Перепоиск не нашел рекомендаций",
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
            "all flights unsupported": [
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
            "tour is not available for booking": [
                "tour is not available for booking",
            ],
            "no routes found": [
                "no routes found",
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
    counters, unclassified, group_totals, overall_total = process_errors(error_groups, rows)

    print_detailed_tables(counters, unclassified, group_totals, overall_total)


if __name__ == "__main__":
    main()

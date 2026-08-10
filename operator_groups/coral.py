from collections import OrderedDict


def get_coral_groups():
    return OrderedDict({
        "Наши ошибки": OrderedDict({
            "package_is_expired": [
                "package is expired",
            ],
            "route_not_found_in_cache": [
                "error finding route in cache: route not found",
            ],
            "user_pool_exhausted": [
                "error selecting not blocked user: no users not in block",
            ],
            "package_not_found": [
                "error building domain package: package not found",
            ],
            "country_matcher_upstream_failure": [
                "failed to get match for country: failed to get map by key matcher:data:2:place_countries: upstream failure",
            ],
        }),
        "Неизвестно чьи ошибки": OrderedDict({
            "connection_error": [
                "error in ReadAll: unexpected EOF",
            ],
            "http2_goaway": [
                "http2: server sent GOAWAY and closed the connection",
            ],
            "flight_selection_bad_request": [
                "failed to select flight: response unsuccessful with code: 400",
            ],
        }),
        "Ошибки ТО Coral": OrderedDict({
            "timeout": [
                "context cancelled (timeout)",
            ],
            "tour_not_found": [
                "failed to search: tour not found",
            ],
            "wrong_auth_response": [
                "wrong auth response code",
            ],
            "no_available_flights": [
                "no available flights",
            ],
            "invalid_supplier_response": [
                "unexpected end of JSON input",
            ],
            "requested_route_not_found": [
                "requested route not found in supplier response",
            ],
        }),
    })

from collections import OrderedDict


def get_sunmar_groups():
    return OrderedDict({
        "Наши ошибки": OrderedDict({
            "package_is_expired": [
                "package is expired",
            ],
            "tour_dropped_by_rules": [
                "error applying rules to tour: tour dropped by rules",
            ],
            "route_not_found_in_cache": [
                "error finding route in cache: route not found",
            ],
            "package_not_found": [
                "error building domain package: package not found",
            ],
            "proxy_connection_refused": [
                "proxyconnect tcp: dial tcp",
            ],
        }),
        "Неизвестно чьи ошибки": OrderedDict({
            "connection_error": [
                "error in ReadAll: unexpected EOF",
            ],
            "http2_goaway": [
                "http2: server sent GOAWAY and closed the connection",
            ],
            "invalid_supplier_response": [
                "json: cannot unmarshal object into Go value of type []*api.BookingInfo",
            ],
        }),
        "Ошибки ТО Sunmar": OrderedDict({
            "timeout": [
                "context cancelled (timeout)",
            ],
            "tour_not_found": [
                "failed to search: tour not found",
            ],
            "no_available_flights": [
                "no available flights",
            ],
            "flight_selection_bad_request": [
                "failed to select flight: response unsuccessful with code: 400",
            ],
            "requested_route_not_found": [
                "requested route not found in supplier response",
            ],
        }),
    })

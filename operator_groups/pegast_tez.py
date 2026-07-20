from collections import OrderedDict


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
            "Нет активной учетной записи" :[
                "api response error: ApiUserNotActive",
            ],
            "FULL_PAID_FLAG": [ #TEZTOUR
                "response unsuccessful with code: Произошла ошибка в вычислении FULL_PAID_FLAG.",
            ],
            "Не найдена авиакомпания": [
                "response unsuccessful with code: Не найдена авиакомпания (carrier=C6)."  #TEZTOUR
            ],
            "invalid_xml_in_response": [
                "response build_order decode unsuccessful with err xml unmarshal error",
                "response decode unsuccessful with err xml unmarshal error: xml: (*api.AuthorizeResponse).UnmarshalXML did not consume entire <html> element",
                "xml unmarshal error: xml: (*api.AuthorizeResponse).UnmarshalXML did not consume entire <html> element"
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
                "response unsuccessful with code: code=[1030, 0], [Authentication failed, see inner exception., Error from supplier (No flights)]",
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

import datetime
import socket

RESPONSE = """HTTP/1.1 200 OK
Content-Length: 20
Content-Type: text/html
Date: %s

<h1>hello world</h1>"""

WEEKDAY = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
MONTH = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]


def format_date(dt):
    weekday = WEEKDAY[dt.weekday()]
    month = MONTH[dt.month - 1]
    return "%s, %02d %s %04d %02d:%02d:%02d GMT" % (
        weekday,
        dt.day,
        month,
        dt.year,
        dt.hour,
        dt.minute,
        dt.second,
    )


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("127.0.0.1", 8080))
    server_socket.listen()
    print("Listening on http://127.0.0.1:8080")
    client_socket, addr = server_socket.accept()
    client_socket.sendall(
        (RESPONSE % (format_date(datetime.datetime.utcnow())))
        .replace("\n", "\r\n")
        .encode()
    )
    client_socket.close()

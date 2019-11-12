import socket
import ssl
from html_parser import MyHTMLParser


def send_request(method="GET", protocol_version="HTTP/1.1", url="", port=443, params=None):
    if port == 443:
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        context.verify_mode = ssl.CERT_REQUIRED
        context.check_hostname = True
        context.load_default_certs()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock = context.wrap_socket(sock, server_hostname=url)
    else:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if params:
        parsed_params = ""
        for k, v in params.items():
            parsed_params += f"{k}={v}"
    else:
        parsed_params = ""

    request = f"{method} / {protocol_version}\nHost: {url}{parsed_params}\n\n"
    print(request)
    sock.connect((url, port))
    sock.send(request.encode())

    return sock


def print_socket_content(sock):
    result = sock.recv(4096)
    while len(result) > 0:
        print(result)
        result = sock.recv(4096)


if __name__ == "__main__":
    sock = send_request(url="yandex.ru", port=443)
    print_socket_content(sock)
    sock.close()


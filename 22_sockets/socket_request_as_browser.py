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


def get_socket_content(sock):
    socket_content = sock.recv(4096)
    while True:
        socket_content += sock.recv(4096)
        if "</html>" in str(socket_content):
            break
    return socket_content


if __name__ == "__main__":
    sock = send_request(url="yandex.ru", port=443)
    socket_content = get_socket_content(sock)
    print(socket_content)
    sock.close()
    # parser = MyHTMLParser()
    # parser.feed(str(result))
    # выводить на экран список:
    # тегов и их названия, текст,
    # самый частовстречающийся тег,
    # список ссылок и картинок на странице


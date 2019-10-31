import paramiko
import requests
import time

host = '0.0.0.0'
user = 'root'
secret = 'root'
port = 32772


def test_ssh_connection():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=secret, port=port)
    client.exec_command('echo "Hello, world." > test.html')
    client.exec_command('python3 -m http.server 8888')
    time.sleep(5)  # ожидаем поднятия http.server
    r = requests.get(url="http://localhost:8888/test.html")
    assert r.ok is True
    assert r.text == "Hello, world.\n"
    client.close()

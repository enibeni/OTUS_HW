import paramiko
import ftplib


host = '0.0.0.0'
user = 'root'
secret = 'root'
port = 32772


def ssh_connection():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=user, password=secret, port=port)
    stdin, stdout, stderr = client.exec_command('dpkg -s vsftpd')
    package_install_status = (stdout.read() + stderr.read()).decode("utf-8")
    if not 'Status: install ok installed' in package_install_status:
        print("im here !")
        client.exec_command('apt-get update')
        stdin, stdout, stderr = client.exec_command('apt-get -y install vsftpd')
        package_install_status = (stdout.read() + stderr.read()).decode("utf-8")
        print(package_install_status)

    # upload config
    # create ftp user
    # service vsftpd start
    # stdin, stdout, stderr = client.exec_command('service vsftpd start')
    # package_install_status = (stdout.read() + stderr.read()).decode("utf-8")
    # print(package_install_status)


    client.close()


if __name__ == '__main__':
    ssh_connection()



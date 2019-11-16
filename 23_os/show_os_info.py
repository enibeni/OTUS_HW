import os
import sys
import subprocess


def show_network_interfaces():
    network_interaces = os.listdir('/sys/class/net/')
    for interface in network_interaces:
        print(interface)


def show_default_gateway():
    subprocess.Popen(('ip', 'route'), stdout=subprocess.PIPE)
    output = str(subprocess.check_output(('ip', 'route')))
    print(str(output).split('\\n')[0])


def show_cpu_info():
    command = "lscpu"
    info = str(subprocess.check_output(command, shell=True)).strip()
    for line in info.split('\\n'):
        print(line)


def show_processes():
    command = "ps -aux"
    info = str(subprocess.check_output(command, shell=True)).strip()
    for line in info.split('\\n'):
        print(line)


def show_network_interfaces_statistics():
    command = "ifconfig"
    info = str(subprocess.check_output(command, shell=True)).strip()
    for line in info.split('\\n'):
        print(line)


def show_service_status(service):
    os.system(f'service {service} status')


def show_port_usage(port):
    os.system(f'netstat -tulpn | grep :{port}')


def show_package_version(package):
    os.system(f'apt list {package}')


def show_directory_contents(path_to_dir):
    os.system(f'ls -la {path_to_dir}')


def show_current_directory_content():
    os.system(f'ls -la')


def show_kernel_version():
    os.system(f'uname -r')


def show_os_version():
    os.system(f'cat /etc/os-release')


def print_help():
    print("""
    Please, enter an option:
    (1) - show_network_interfaces
    (2) - show_default_gateway
    (3) - show_cpu_info
    (4) - show_processes
    (5) - show_network_interfaces_statistics
    (6) - show_service_status
    (7) - show_port_usage
    (8) - show_package_version
    (9) - show_directory_contents
    (10) - show_current_directory_content
    (11) - show_kernel_version
    (12) - show_kernel_version
    """)


if __name__ == '__main__':
    print_help()
    user_input = int(input())

    if user_input == 1:
        show_network_interfaces()
    elif user_input == 2:
        show_default_gateway()
    elif user_input == 3:
        show_cpu_info()
    elif user_input == 4:
        show_processes()
    elif user_input == 5:
        show_network_interfaces_statistics()
    elif user_input == 6:
        print("enter service name")
        service = input()
        show_service_status(service)
    elif user_input == 7:
        print("enter port")
        port = input()
        show_port_usage(port)
    elif user_input == 8:
        print("enter package")
        package = input()
        show_package_version(package)
    elif user_input == 9:
        print("enter path to directory")
        path = input()
        show_directory_contents(path)
    elif user_input == 10:
        show_current_directory_content()
    elif user_input == 11:
        show_kernel_version()
    elif user_input == 12:
        show_os_version()
    else:
        sys.exit("wrong input, bye!")


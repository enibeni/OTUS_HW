import argparse
import re
import os
import sys
import json
from collections import defaultdict, OrderedDict


def get_requests_count(file):
    requests_count = 0
    for line in file:
        regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        if re.search(regex, line):
            requests_count += 1
    return requests_count


def get_requests_type_count(file):
    type_count = defaultdict(int)
    for line in file:
        regex = r"\"(POST|GET|PUT|DELETE|HEAD)"
        match = re.search(regex, line)
        if match:
            type_count[match.group(0)] += 1
    return type_count


def get_top_request_ip_addresses(file, count_to_show=10):
    requests_ip = defaultdict(int)
    for line in file:
        regex = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        match = re.search(regex, line)
        if match:
            requests_ip[match.group(0)] += 1
    sorted_ip = sorted(
        requests_ip.items(),
        key=lambda kv: kv[1],
        reverse=True
    )[:count_to_show]
    return OrderedDict(sorted_ip)


def get_top_errors(file, error_type=4, count_to_show=10):
    errors = defaultdict(int)
    for line in file:
        regex = r"\s" + str(error_type) + r"\d{2}\s"
        if re.search(regex, line):
            regex = r"(POST|GET|PUT|DELETE|HEAD) (.+\") (\d{3})"
            match = re.search(regex, line)
            request = match.group(0) if match else "request is not parsed"
            errors[request] += 1
    sorted_errors = sorted(
        errors.items(),
        key=lambda kv: kv[1],
        reverse=True
    )[:count_to_show]
    return OrderedDict(sorted_errors)


def get_input_args():
    """
    :return: list of args
    """
    parser = argparse.ArgumentParser(description="Process access.log")
    parser.add_argument(
        "-f",
        "--file",
        action="store",
        help="path to log file",
    )
    parser.add_argument(
        "-d",
        "--dir",
        action="store",
        help="path to the directory with logs",
    )
    args = parser.parse_args()
    return args


def save_json_report(report):
    with open("report.json", "w") as f:
        json.dump(report,  f, indent=4)


def load_logs_file(logs_filepath):
    if not os.path.exists(logs_filepath):
        return None
    with open(logs_filepath, "r", encoding="utf-8") as file:
        return file.readlines()


if __name__ == "__main__":
    args = get_input_args()
    report = defaultdict(dict)
    log_files = []

    if args.dir:
        files = os.listdir('.')
        log_files = [file for file in files if str(file).endswith(".log")]

    elif args.file:
        log_files.append(args.file)

    for file in log_files:
        log_file = load_logs_file(file)
        if log_file is None:
            sys.exit("File not found")

        requests_count = get_requests_count(log_file)
        report[file]["Total sum of requests"] = requests_count

        methods = get_requests_type_count(log_file)
        report[file]["Requests count by type"] = methods

        requests_ip = get_top_request_ip_addresses(log_file)
        report[file]["Top requests by ip"] = requests_ip

        client_errors = get_top_errors(log_file, error_type=4)
        report[file]["Top client errors requests"] = client_errors

        server_errors = get_top_errors(log_file, error_type=5)
        report[file]["Top server errors requests"] = server_errors

        save_json_report(report)

    print(json.dumps(report, indent=4))



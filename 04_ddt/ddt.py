import csv
import random


def read_csv_data():
    csv_file = open('data.csv', encoding='Windows-1251')
    file_data = list(csv.reader(csv_file))
    data_without_header = file_data[1:]
    fios = [x[0] for x in data_without_header]
    cities = [x[1] for x in data_without_header]
    return fios, cities


def generate_output_data(fios, cities):
    output_data = list(
        ((x, y, random.getrandbits(1), random.getrandbits(1), random.getrandbits(1))
         for x in fios for y in cities)
    )
    return output_data


def write_data_to_file(data):
    with open('data.txt', 'w') as f:
        for line in data:
            f.write('{}\n'.format('\t'.join(map(str, line))))


if __name__ == '__main__':
    fios, cities = read_csv_data()
    data = generate_output_data(fios, cities)
    write_data_to_file(data)

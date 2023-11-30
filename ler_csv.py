import csv
import os
from functools import reduce


def read_csv(filename):
    data_list = []

    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "./"))

    with open(os.path.join(data_dir, filename), 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data_list.append(row)

    return data_list


def find_intersection(lists):
    if not lists:
        return []

    restaurant_sets = [set(stream) for stream in lists]
    intersection = reduce(lambda set1, set2: set1.intersection(set2), restaurant_sets)
    return list(intersection)
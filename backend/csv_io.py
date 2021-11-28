import csv


def parse_cc_csv(csvfile):
    # returns list of dict
    items = []
    print('Reading File: ', csvfile)
    with open(csvfile, encoding="ISO-8859-1") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            # index 0 - date
            # index 1 - vendor
            # index 2 - price
            # index 3 - category ** if categorized
            items.append(
                {'date': row[0], 'vendor': row[1], 'price': row[2]})
    return items


def parse_chequing_csv(csvfile):
    # returns list of dict
    items = []
    print('Reading File: ', csvfile)
    with open(csvfile, encoding="ISO-8859-1") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            # index 0 - date
            # index 1 - vendor
            # index 2 - price
            # index 3 - category ** if categorized
            items.append(
                {'date': row[0], 'vendor': row[4], 'price': row[1]})
    return items


def parse_categorized_csv(csvfile):
    # returns list of dict
    items = []
    print('Reading File: ', csvfile)
    with open(csvfile, encoding="ISO-8859-1") as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            # index 0 - date
            # index 1 - vendor
            # index 2 - price
            # index 3 - category ** if categorized
            items.append(
                {'date': row[0], 'vendor': row[1], 'price': row[2], 'category': row[3]})
    return items


def write_csv(csvfile, dict_data, csv_columns):
    print('Writing File: ', csvfile)
    with open(csvfile, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)

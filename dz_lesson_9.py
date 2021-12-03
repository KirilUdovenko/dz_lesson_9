def read_file(filename):
    with open(filename, 'r') as file:
        return file.read().split('\n')


def get_domains(filename):
    lines = read_file(filename)
    lines = [line.replace(".", "") for line in lines]
    return lines


def get_names(filename):
    lines = read_file(filename)
    lines = [line.split("\t")[1] for line in lines]
    return lines


def str_to_date(some_str):
    months_dict = {'January': '01',
                   'February': '02',
                   'March': '03',
                   'April': '04',
                   'May': '05',
                   'June': '06',
                   'July': '07',
                   'August': '08',
                   'September': '09',
                   'October': '10',
                   'November': '11',
                   'December': '12'}
    parts = some_str.split()
    day, month, year = parts
    date = f"{day[:-2].zfill(2)}/{months_dict[month]}/{year}"
    return date


def get_dates(filename):
    lines = read_file(filename)
    lines = [line.split(" - ")[0] for line in lines if " - " in line]
    lines = [str_to_date(line) for line in lines]
    return lines


filename_domains = "domains.txt"
domains = get_domains(filename_domains)
print(domains)

filename_names = "names.txt"
names = get_names(filename_names)
print(names)

filename_dates = "author.txt"
dates = get_dates(filename_dates)
print(dates)

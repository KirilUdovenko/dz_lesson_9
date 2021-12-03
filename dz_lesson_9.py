class FileWorkerReplace:
    def __init__(self, filename_domains):
        self.filename_domains = filename_domains
        self.read_file()
        self.get_domains()

    def read_file(self):
        with open(self.filename_domains, 'r') as file:
            return file.read().split('n')

    def get_domains(self):
        lines = self.read_file()
        lines = [line.replace(".", "") for line in lines]
        return lines


filename_domains = "domains.txt"
file_worker_replace = FileWorkerReplace(filename_domains)
file_worker_replace.read_file()
file_worker_replace.get_domains()


class FileWorkerSort:
    def __init__(self, filename_names):
        self.filename_names = filename_names
        self.read_file()
        self.get_names()

    def read_file(self):
        with open(self.filename_names, 'r') as file:
            return file.read().split('n')

    def get_names(self):
        lines = self.read_file()
        lines = (line.split("\t")[1] for line in lines)
        return lines


filename_names = "names.txt"
file_worker_sort = FileWorkerSort(filename_names)
file_worker_sort.read_file()
file_worker_sort.get_names()


class DateRemake:
    def __init__(self, filename_dates):
        self.filename_dates = filename_dates
        self.read_file()
        self.get_dates()

    def read_file(self):
        with open(self.filename_dates, 'r') as file:
            return file.read().split('n')

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

    def get_dates(self):
        lines = self.read_file()
        lines = [line.split(" - ")[0] for line in lines if " - " in line]
        lines = [str_to_date(line) for line in lines]
        return lines


filename_dates = "author.txt"
date_remake = DateRemake(filename_dates)
date_remake.read_file()
date_remake.get_dates()

# dates = get_dates(filename_dates)
# print(dates)

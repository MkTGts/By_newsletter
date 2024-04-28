import csv
from datetime import datetime


class Importeds:
    def __init__(self, filename='file1') -> None:
        with open(filename, encoding='utf-8') as file:
            rows = csv.reader(file, delimiter=';')
            self.rows = list(rows)

    @staticmethod
    def clear_file(filename: str) -> None:
        f = open(filename, 'w')
        f.close()

    @classmethod
    # записывает маил и имя в файл и выводит кличество соответствующих
    def writer(cls, file_name: str, rows: list, key: str, col: int, count=0) -> int:
        with open(file_name, 'a', encoding='utf-8') as file:
            for row in rows:
                if row[col] == key:
                    count += 1
                    file.write(row[1] + ' - ' + row[2] + '\n')
        return count

    def status(self) -> int:  # статус (отправлено <-> ошибка)
        __class__.clear_file('status_ok.txt')
        return self.writer('status_ok.txt', self.rows, key='Отправлено', col=3)

    def is_read(self) -> int:  # прочитано или нет
        __class__.clear_file('read_ok.txt')
        return self.writer('read_ok.txt', self.rows, key='Да', col=5)

    def click(self) -> int:  # кликнуто по ссылке или нет
        __class__.clear_file('click_ok.txt')
        return self.writer('click_ok.txt', self.rows, key='Да', col=6)

    def unsub(self) -> int:  # если отписался
        __class__.clear_file('unsub.txt')
        return self.writer('unsub.txt', self.rows, key='Да', col=7)

    def is_dates(self) -> datetime:  # дата рассылки
        s = self.rows[1][4][:10]
        dates = datetime.strptime(s, '%d.%m.%Y')
        return dates

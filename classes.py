import csv
from datetime import datetime
import os


class Importeds:
    def __init__(self, filename='file1') -> None:
        with open(filename, encoding='utf-8') as file:
            rows = csv.reader(file, delimiter=';')
            self.rows = list(rows)

    @staticmethod
    def create_file_date(filename: str) -> datetime:
        """
        Статический метод возврщающий дату создания файла
        Эти данные будут использоваться для указания на какое время актуальна статистика
        Файл скачан и перенесен в папку, это и есть время создания файла
        """
        stat = os.stat(filename)
        ctime = stat.st_ctime
        return datetime.fromtimestamp(ctime)

    @classmethod
    def writer(cls, file_name: str, rows: list, key: str, col: int, count=0) -> int:
        """
        Шаблонный метод, принимает имя файла, список строк, которые будут обрабатываться,
        ключ по которому нужно будет искать и столбец в котором искать
        Записывает маил и имя в файл и выводит кличество соответствующих условиям
        """
        with open(file_name, 'w', encoding='utf-8') as file:
            for row in rows:
                if row[col] == key:
                    count += 1
                    file.write(row[1] + ';' + row[2] + '\n')
        return count

    def create_dir(self) -> str:  # создает папку с названием по дате рассылки
        dir_name = f'data/statistics/stat_as_{self.is_dates().strftime(
            '%d%m%y')}'  # достает название папки
        try:
            os.mkdir(dir_name)  # создает папку
        except FileExistsError:
            pass
        self.dir_name = dir_name
        return dir_name  # возвращает название папки

    def status(self) -> int:  # статус (отправлено <-> ошибка)
        path = f'{self.dir_name}/status_ok.txt'  # путь к файлу
        return self.writer(path, self.rows, key='Отправлено', col=3)

    def is_read(self) -> int:  # прочитано или нет
        path = f'{self.dir_name}/read_ok.txt'  # путь к файлу
        return self.writer(path, self.rows, key='Да', col=5)

    def click(self) -> int:  # кликнуто по ссылке или нет
        path = f'{self.dir_name}/click_ok.txt'  # путь к файлу
        return self.writer(path, self.rows, key='Да', col=6)

    def unsub(self) -> int:  # если отписался
        path = f'{self.dir_name}/unsub.txt'  # путь к файлу
        return self.writer(path, self.rows, key='Да', col=7)

    def is_dates(self) -> datetime:  # дата рассылки
        """
        Дата рассылки. В дальнейшем будет использоваться также как название рассылки
        """
        s = self.rows[1][4][:10]
        dates = datetime.strptime(s, '%d.%m.%Y')
        return dates

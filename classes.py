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
        """Шаблонный метод, принимает имя файла, список строк, которые будут обрабатываться,
        ключ по которому нужно будет искать и столбец в котором искать
        Записывает маил и имя в файл и выводит кличество соответствующих условиям"""
        __class__.errorss = []
        with open(file_name, 'w', encoding='utf-8') as file:
            for row in rows:
                if key and row[col] != key:  # если ключ не False и элемент в выбраном столбце не равен ключу, то пропускаем
                    continue
                else:  # если норм записываем
                    count += 1
                    file.write(row[1] + ';' + row[2] + '\n')
                    if key == 'С ошибками':
                        __class__.errorss.append(row[1])

        return count

    def create_dir(self) -> str:  # создает папку с названием по дате рассылки
        dir_name = f'data/statistics/stat_as_{self.is_dates().strftime(
            '%d%m%y')}'  # достает название папки
        try:
            os.mkdir(dir_name)  # создает папку
        except FileExistsError:
            pass
        self.dir_name = dir_name
        return dir_name  # возвращает название директории

    def status(self) -> int:  # статус (отправлено <-> ошибка)
        pat = f'{self.dir_name}/status_ok.txt'  # путь к файлу
        return self.writer(pat, self.rows, key='Отправлено', col=3)

    def is_read(self) -> int:  # прочитано или нет
        pat = f'{self.dir_name}/read_ok.txt'  # путь к файлу
        return self.writer(pat, self.rows, key='Да', col=5)

    def click(self) -> int:  # кликнуто по ссылке или нет
        pat = f'{self.dir_name}/click_ok.txt'  # путь к файлу
        return self.writer(pat, self.rows, key='Да', col=6)

    def unsub(self) -> int:  # если отписался
        pat = f'{self.dir_name}/unsub.txt'  # путь к файлу
        return self.writer(pat, self.rows, key='Да', col=7)
    
    def all_addr(self) -> int:  # все адреса которые участвовали в рассылке
        pat = f'{self.dir_name}/all_addr.txt'  # путь к файлу
        self.all_ad = self.writer(pat, self.rows, key=False, col=1)
        return self.all_ad

    def err_adr(self) -> int:  # с ошибкой
        self.pat = f'{self.dir_name}/err_addr.txt'
        return self.writer(self.pat, self.rows, key='С ошибками', col=3)
    



    def is_dates(self) -> datetime:  # дата рассылки
        """
        Дата рассылки. В дальнейшем будет использоваться также как название рассылки
        """
        s = self.rows[1][4][:10]
        dates = datetime.strptime(s, '%d.%m.%Y')
        return dates
    
    def domains(self) -> dict:  # записывает статистику используемых доменов
        '''Собирает статистику по количеству используемых доменов почтовых адресов
        Список рассматриваемых доменов записывается здесь внутри 
        Данные берет из csv файла'''
        domains_dict = {}  # под словарь доменов
        for mail in self.rows[1:]:  # идет по файлу рассылки
            mail = mail[1]  # выбирает из только адреса
            se = mail.index('@')  # находит индекс символа @
            mail = mail[se+1:]
            domains_dict[mail] = domains_dict.get(mail, 0) + 1
        lst1 = sorted(domains_dict, key=lambda x: domains_dict[x], reverse=True)  # сортирует по убыванию тмпользования адресов
        with open('data/statistics/domain_stat.txt', 'w', encoding='utf-8') as file: # открыввает файл для записи статистики доменов
            wrtr = [f'адресов с доменом {j} - {domains_dict[j]}шт. это {round((domains_dict[j] * 100) / self.all_ad, 2)}%.\n' for j in lst1]  
            file.writelines(wrtr)  # записывает 

        return domains_dict  # возвращает словарь статистики доменов
    
    def names_stat(self):
        names_dict = {}  # словарь под имена
        for i in self.rows[1:]:  # итерация по данным из файла
            name = i[2]  # выберает только имя
            names_dict[name] = names_dict.get(name, 0) + 1  # плюсует имя к словарю

        s = sorted(names_dict, key=lambda x: names_dict[x], reverse=True)  # сортирует по убыванию

        with open('data/statistics/names_stat.txt', 'w', encoding='utf-8') as file:  # запись в файл
            wrtr = [f'Имя {j} встречается {names_dict[j]} раз, это {round((names_dict[j] * 100) / self.all_ad, 2)}%.\n' for j in s]
            file.writelines(wrtr)
        
        return names_dict
    
        

        







            





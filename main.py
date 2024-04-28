from classes import Importeds
from funcs import *


file_name_imported = 'file1.csv'

data = Importeds(file_name_imported)

delivered = data.status()  # кол-во доставленных
read = data.is_read()  # кол-во прочитанных
click = data.click()  # кол-во кликов
unsub = data.unsub()  # кол-во отисавшихся
dates_unsub = data.is_dates()  # дата рассылки
dates_relevant = Importeds.create_file_date(
    file_name_imported)  # дата на которую данные актуальны


# название файла в который записались данные
fn = write_to_stat(delivered, read, click, unsub, dates_unsub, dates_relevant)
print(f'Данные записаны в файл {fn}')
s = input()

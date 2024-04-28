from classes import Importeds
from funcs import *


data = Importeds('file1.csv')

delivered = data.status()  # кол-во доставленных
read = data.is_read()  # кол-во прочитанных
click = data.click()  # кол-во кликов
unsub = data.unsub()  # кол-во отисавшихся
dates = data.is_dates()  # дата рассылки

# print(delivered, read, click, unsub, dates, sep='\n')
# print(write_to_stat(delivered, read, click, unsub, dates))
# название файла в который записались данные
fn = write_to_stat(delivered, read, click, unsub, dates)
print(f'Данные записаны в файл {fn}')
s = input()

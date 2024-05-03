from classes import Importeds
from funcs import *


file_name_imported = 'data/imported/file1.csv'

data = Importeds(file_name_imported)

path = data.create_dir()  # название директории в data
delivered = data.status()  # кол-во доставленных
read = data.is_read()  # кол-во прочитанных
click = data.click()  # кол-во кликов
unsub = data.unsub()  # кол-во отgисавшихся
dates_unsub = data.is_dates()  # дата рассылки
all_ad = data.all_addr()  #все адреса
err = data.err_adr()  # адреса с ошибками
dates_relevant = Importeds.create_file_date(
    file_name_imported)  # дата на которую данные актуальны


# название файла в который записались данные
fn = write_to_stat(delivered, read, click, unsub,
                   dates_unsub, dates_relevant, path, all_ad, err)

genral_stat(dates_unsub, dates_relevant, delivered, read, click, unsub, all_ad, err)

print(f'Данные записаны в файл {fn}')
s = input()

data.names_stat()
data.domains()

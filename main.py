from classes import Importeds
from funcs import *


file_name_imported = 'data/imported/file1.csv'  # входной файл

data = Importeds(file_name_imported)

# при вызове этих методов также происходит запись в соответсвующий файл, в папке по дате рассылки
path = data.create_dir()  # название директории в data
delivered = data.status()  # кол-во доставленных
read = data.is_read()  # кол-во прочитанных
click = data.click()  # кол-во кликов
unsub = data.unsub()  # кол-во отписавшихся
dates_unsub = data.is_dates()  # дата рассылки
all_ad = data.all_addr()  # все адреса
err = data.err_adr()  # адреса с ошибками
dates_relevant = Importeds.create_file_date(
    file_name_imported)  # дата на которую данные актуальны
errorss = Importeds.errorss  # список адресов с ошибкой при отправлении



# название файла в который записались данные
fn = write_to_stat(delivered, read, click, unsub,
                   dates_unsub, dates_relevant, path, all_ad, err)  # запись в файлы статистики


genral_stat(dates_unsub, dates_relevant, delivered, read, click, unsub, all_ad, err)  # запись в общий файл статистики

print(f'Данные записаны в файл {fn}')  # принтует куда записали

s = input()

data.names_stat()  # метод записывает статистику имен пользователей по кол-ву
data.domains()  # метод записывает статистику используемых доменов по кол-ву


print(rev_addrs(fn))  # функция записывает релевантные адреса для след рассылки

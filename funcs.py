from datetime import datetime
import json
import csv



def write_to_stat(delivered: int, read: int, click: int, unsub: int, dates_unsub: datetime, dates_relevant: datetime, path: str, all_ad: int, err: int) -> str:
    """
    Функиця записывает собранную статистику по рассылке в файл и возвращает название файла в который записала стат.
    Принимает(в очередности подачи): кол-во доставленных; прочитанны; кликов(переходов); отписавшихся;
    актуальную дата(т.е. когда файл был загружен с Битрикса); дату рассылки(является также именем рассылки); 
    дату релевантноти рассилки; директория внутри data куда сохраняются данные по этой расслке.
    """
    filename = path + '/stat_' + str(dates_unsub.day).zfill(2) + \
        str(dates_unsub.month).zfill(2) + \
        str(dates_unsub.year)[2:] + '.txt'  # генерация названия файла
    
    

    with open(filename, 'w', encoding='utf-8') as file:
        dr = dates_relevant.strftime('%H:%M %d.%m.%Y')
        file.write(f'Рассылка от {dates_unsub.strftime('%d.%m.%Y')}.\n')
        file.write(f'Статистика актуальна на {dr}.\n\n')
        file.write(f'Всего было отправлено {all_ad} писем.\n')
        file.write(f'Было успешно доставлено {delivered} - {percent(delivered, all_ad)}% писем.\n')
        file.write(f'Возникла ошибка при отправлении {err} - {percent(err, all_ad)}% писем.\n')
        file.write(f'Из них прочитано было {read} - {percent(read, delivered)}% писем.\n')
        file.write(f'По ссылке перешли {click} - {percent(click, delivered)}% человек.\n')
        file.write(f'После этой рассылки, отписались {unsub} - {percent(unsub, delivered)}% человек.\n\n')

    return filename  # возвращает название файла


def genral_stat(dates_unsub: datetime, dates_relevant: datetime, delivered: int, read: int, click: int, unsub: int, all_ad: int, err: int) -> None:
    columns = ['Дата рассылки', 'Дата проверки','Всего отправлено', 'Успешно доставлено', 'Ошибка при отправлении', 
               'Прочитано', 'Переходов', 'Отписок']  # загаловок
    data = [dates_unsub.strftime(
        # текущие данные
        '%d.%m.%Y'), dates_relevant.strftime('%d.%m.%Y %H:%M'), all_ad, delivered, err, read, click, unsub]

    # открываем файл для записи текущих данных
    with open('data/statistics/general_stat.csv', 'a+', encoding='cp1251', newline='') as file:
        # row = read_column()  # первая строка в файле для проверки, что заголовок есть в файле
        wrt = csv.writer(file, delimiter=';',
                         quoting=csv.QUOTE_STRINGS)  # под запись
        if read_column():
            wrt.writerow(columns)
        wrt.writerow(data)


def read_column() -> bool:  # функция возвращает первую строку и файла для проверки на пустоту
    with open('data/statistics/general_stat.csv', 'r', encoding='utf-8') as file:
        row = csv.reader(file)
        try:
            next(row)
            return False
        except:
            return True
        

def percent(num: int, full_num:int) -> int:
    '''Функция принимает общее число и отдельное число, для вычисления процента.
       Будет принимать общее кол-во отправлений и разносить по процентам каждую категорию.'''
    try:
        res = (num * 100) / full_num
        return round(res, 2)
    except ZeroDivisionError:
        pass


def rev_addrs(fn: str) -> None:
    '''Функиця записывает релевантные адреса для следующей рассылки, за исключением отписавшихся.'''
    res = []
    fn = fn.split('/')[:-1]
    full_addr_dir = '/'.join(fn) + '/all_addr.txt'  # преобразует путь к файлу где лежат все адреса
    error_addr_dir = '/'.join(fn) + '/unsub.txt'  # преобразует путь к файлу где лежат адреса с отписками

    with open(full_addr_dir, 'r', encoding='utf-8') as file:  # достает все адреса
        addr_ok = [i.strip() for i in file.readlines()]
 
    with open(error_addr_dir, 'r', encoding='utf-8') as  file1:  # достает адреса с ошибкой
        addr_err = [j.strip() for j in file1.readlines()]

    for i in addr_ok:  # итерация по всем адресам
        if i in addr_err:  # если адрес присутсвует в списке адрнесов с ошибками
            del addr_ok[addr_ok.index(i)]  # то этот адрес удаляется из списка

    with open('data/relev_addr.txt', 'w', encoding='utf-8') as file2:  # открывает файл с релевантными адресами
        for addr in addr_ok:
            file2.write(addr + '\n')  # записывает адрес не отписавшегося

    return f'Создан список релевантных адресов. Отписались {len(addr_err)}.'


    
    


    
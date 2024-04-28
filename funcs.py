from datetime import datetime
import os


def write_to_stat(delivered: int, read: int, click: int, unsub: int, dates_unsub: datetime, dates_relevant: datetime) -> str:
    """
    Функиця записывает собранную статистику по рассылке в файл и возвращает название файла в который стат записала
    Принимает(в очередности подачи): кол-во доставленных, прочитанных, кликов(переходов), отписавшихся,
    актуальную дата(т.е. когда файл был загружен с Битрикса), дату рассылки
    """
    filename = 'stat_' + str(dates_unsub.day).zfill(2) + \
        str(dates_unsub.month).zfill(2) + \
        str(dates_unsub.year)[2:] + '.txt'  # генерация названия файла

    with open(filename, 'w', encoding='utf-8') as file:
        dr = dates_relevant.strftime('%H:%M %d.%m.%Y')
        file.write(f'Рассылка от {dates_unsub.strftime('%d.%m.%Y')}.\n')
        file.write(f'Статистика актуальна на {dr}.\n\n')
        # file.write(f'Рассылка от {dates_unsub.strftime('%d.%m.%Y')}.\n')
        file.write(f'Было успешно доставлено {delivered} писем.\n')
        file.write(f'Из них прочитано было {read} писем.\n')
        file.write(f'По ссылке перешли {click} человек.\n')
        file.write(f'После этой рассылки, отписались {unsub} человек.\n\n')
    return filename  # возвращает название файла

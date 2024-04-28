from datetime import datetime


def write_to_stat(delivered: int, read: int, click: int, unsub: int, dates: datetime) -> str:
    filename = 'stat_' + str(dates.day).zfill(2) + \
        str(dates.month).zfill(2) + str(dates.year)[2:] + '.txt'

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f'Рассылка состоялась {dates.strftime('%d.%m.%Y')}\n\n')
        file.write(f'Было успешно доставлено {delivered} писем.\n')
        file.write(f'Из них прочитано было {read} писем.\n')
        file.write(f'По ссылке перешли {click} человек.\n')
        file.write(f'После этой рассылки, отписались {unsub} человек.\n\n')
    return filename

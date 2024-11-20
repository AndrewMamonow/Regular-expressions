from pprint import pprint
import csv
import re


if __name__ == '__main__':
    # читаем адресную книгу в формате CSV в список contacts_list
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    # pprint(contacts_list)

    # TODO 1: выполните пункты 1-3 ДЗ
    for index, personal in enumerate(contacts_list):
        personal = ' '.join(personal[:3]).split(' ')
        contacts_list[index][0] = personal[0]
        contacts_list[index][1] = personal[1]
        if personal[2] == '':
            contacts_list[index][2] = personal[3]
        else:
            contacts_list[index][2] = personal[2] 
        pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
        pattern_sub = r'+7(\2)-\3-\4-\5 \6\7'
        contacts_list[index][5] = re.sub(pattern, pattern_sub, contacts_list[index][5])
        first_name = contacts_list[index][0]
        last_name = contacts_list[index][1]
        for index_2, personal in enumerate(contacts_list):
            if personal[0] == first_name and personal[1] == last_name and index_2 != index:
                for n in range(2, 7):
                    if contacts_list[index_2][n] == '':
                        contacts_list[index_2][n] = contacts_list[index][n]
                contacts_list.pop(index)

    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)


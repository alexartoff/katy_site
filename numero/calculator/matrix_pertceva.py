#!/usr/bin/env python


from datetime import timedelta, datetime


def get_date():
    date = input("birth date (dd.mm.yyyy): ")
    parse_date = date.replace('.', '')
    return parse_date


def post_date(bday):
    parse_date = bday.replace('.', '')
    return parse_date


def calc_matrix(birth_date):
    birth_date_int = [int(item) for item in birth_date]
    result_list = birth_date_int
    first_number = sum(birth_date_int)
    # print(first_number)
    first_number_int = [int(item) for item in str(first_number)]
    second_number = sum(first_number_int)
    destiny_number = second_number if (second_number < 10 or second_number == 11) else sum([int(item) for item in str(second_number)])
    # print(second_number, destiny_number)
    third_number = abs(first_number - 2 * (birth_date_int[0] if birth_date_int[0] != 0 else birth_date_int[1]))
    # print(third_number)
    third_number_int = [int(item) for item in str(third_number)]
    fourth_number = sum(third_number_int)
    # print(fourth_number)
    result_list.append(first_number)
    result_list.append(second_number)
    result_list.append(third_number)
    result_list.append(fourth_number)
    result_str = '' #map(lambda ch: result_str + str(ch), result_list)
    for item in result_list:
        result_str += str(item)
    return result_str, destiny_number


def make_dict(lst, dn):
    key_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    number_dict = {'one': '', 'two': '', 'three': '', 'four': '', 'five': '', 'six': '', 'seven': '', 'eight': '', 'nine': ''}
    for key in number_dict.keys():
        val = ''
        for item in lst:
            if int(item) == key_dict[key]:
                val += item
        number_dict[key] = val #if val != '' else '0'
    number_dict_all = number_dict.copy()
    number_dict_all.update({
        'sudba': str(dn),
        'bit': str(len(number_dict_all['four'] + number_dict_all['five'] + number_dict_all['six'])),
        'cel': str(len(number_dict_all['one'] + number_dict_all['four'] + number_dict_all['seven'])),
        'semiya': str(len(number_dict_all['two'] + number_dict_all['five'] + number_dict_all['eight'])),
        'privichki': str(len(number_dict_all['three'] + number_dict_all['six'] + number_dict_all['nine'])),
        'temperament': str(len(number_dict_all['three'] + number_dict_all['five'] + number_dict_all['seven'])),
        })
    output = ''
    for key in number_dict_all.keys():
        if key == 'ЧИСЛО СУДЬБЫ':
            output += f"\nЧИСЛО СУДЬБЫ:{number_dict_all[key]} "
        elif isinstance(key, str):
            output += f"{key}:{number_dict_all[key]} "
        elif isinstance(key, int):
            output += f"{'-' if number_dict_all[key] == '' else number_dict_all[key]} / "
        number_dict_all[key] = "---" if number_dict_all[key] == "" else number_dict_all[key]
    return number_dict, number_dict_all, output


def find_date_via_matrix(start_date=(1960, 1, 1), end_date=(2020, 12, 31)):
    matrix_for_search = {1:'1111', 2:'22', 3:'33', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
    date = datetime(*start_date)
    while date < datetime(*end_date):
        # print(date.day, date.month, date.year)
        date_str = f'{date.day}{date.month}{date.year}'
        res, dn = calc_matrix(date_str)
        dct, _, output = make_dict(res, dn)
        if matrix_for_search == dct:
            print(date.day, date.month, date.year)
            print(output, "\n")
        date += timedelta(1)
        # print(date.day, date.month, date.year)


def main():
    res_str, dn = calc_matrix(get_date())
    _, _, output = make_dict(res_str, dn)
    print(output)
    # find_date_via_matrix()


if __name__ == "__main__":
    main()

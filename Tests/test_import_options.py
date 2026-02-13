''' these tests are not part of E2E flow in any way, it is to test import options available in the framework'''

from Utils.import_options_utils import read_json_data, read_excel_data, read_csv_data


def test_importing_from_json():
    result_json = read_json_data('./Testdata/test_data.json')
    print('email = ', result_json[0][0]["email"])
    print('name = ', result_json[0][0]["name"])
    print('subject = ', result_json[0][1]["subject"])


def test_importing_from_excel():
    result_exl = read_excel_data(file_path='./Testdata/testexcel.xlsx')
    print(result_exl)
    print('data=>', result_exl[1][1])

def test_importing_csv():
    result_csv = read_csv_data(file_path='./Testdata/filecsv.csv')
    print('animal name =>', result_csv[0][0])
    print('is is an animal? ',result_csv[0][1])


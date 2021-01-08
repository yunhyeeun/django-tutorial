import requests
import re
from bs4 import BeautifulSoup, SoupStrainer

# 국내 발생 현황
def print_overview():
    req = requests.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11')
    if req.status_code != 200:
        print (req.status_code)
    else:
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        titles = soup.select('div.caseTable > div > .ca_top')
        subtitles = soup.select('div.caseTable > div > ul.ca_body > li > dl > dt.ca_subtit')
        values = soup.select('div.caseTable > div > ul.ca_body > li > dl > dd.ca_value')
        result_total = {}
        for i, title in enumerate(titles):
            elem = dict()
            for j in range(2):
                elem[subtitles[2 * i + j].text] = str_to_num(values[2 * i + j].text)
            result_total[title.text] = elem

    print ("***국내발생동향***\n")
    print (result_total)

# 시도별 발생동향
def print_data_by_cities():
    req = requests.get('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13')
    if req.status_code != 200:
        print (req.status_code)
    else:
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        table_titles = soup.select('thead > tr > th')
        table_contents_string = soup.select('tbody > tr > th')
        table_contents_number = soup.select('tbody > tr > td')
        result_titles = []
        result_contents_string = []
        result_contents_number = []
        result_total = {}

        for title in table_titles:
            result_titles.append(title.text)
        for string in table_contents_string:
            result_contents_string.append(string.text)
        for number in table_contents_number:
            result_contents_number.append(str_to_num(number.text))
        result_titles = result_titles[3:]
        rowsize = len(result_titles)
        start = 0

        for i, city in enumerate(result_contents_string):
            start = len(result_titles) * i
            element = dict()
            for j, head in enumerate(result_titles):
                element[head] = result_contents_number[start + j]
            result_total[city] = element

    print ("***시도별 발생동향***\n")
    for item in result_total.items():
        print (item)

def str_to_num(str):
    str = str.replace(',', '')
    str = str.replace('\n', '')
    str = str.replace(' ', '')
    try:
        tmp = int(str)
        return tmp
    except ValueError:
        try:
            tmp = float(str)
            return tmp
        except ValueError:
            return str
        

print_overview()
# print_data_by_cities()

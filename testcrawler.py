import requests
import re
import urllib.request
import xmltodict
import json

from xml.etree import ElementTree
from bs4 import BeautifulSoup, SoupStrainer
from urllib import parse
from datetime import date

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
        

def print_overview_api():
    URL = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson'
    API_KEY = 'f%2Fhg6LYbdDJSpfbO591Mc6yKoWwuB5nf52tDezzb0jTKIX7Wx8GxAbhP3An8NOIJmGPad2WCDTZRa1%2FoRclNGA%3D%3D'
    API_KEY = parse.unquote(API_KEY)
    PAGENO = '1'
    NUM_ROWS = '10'
    START_DATE = '20200310',
    today = date.today()
    END_DATE = '{0:04d}{1:02d}{2:02d}'.format(int(today.year), int(today.month), int(today.day))
    params = {
        'ServiceKey' : API_KEY,
        # 'pageNo' : PAGENO,
        # 'numOfRows' : NUM_ROWS,
        # 'startCreateDt' : START_DATE,
        # 'endCreateDt' : END_DATE
    }
    
    request = requests.get(URL, params=params)
    raw_data = xmltodict.parse(request.text)
    json_data = json.loads(json.dumps(raw_data))
    body = json_data['response']['body']['items']['item']
    def parsing(word):
        if word =='seq':
            return '게시글번호'
        elif word == 'stateDt':
            return '기준일'
        elif word == 'stateTime':
            return '기준시간'
        elif word == 'decideCnt':
            return '확진자 수'
        elif word == 'clearCnt':
            return '격리해제 수'
        elif word == 'examCnt':
            return '검사진행 수'
        elif word == 'deathCnt':
            return '사망자 수'
        elif word == 'careCnt':
            return '치료중 환자 수'
        elif word == 'resutlNegCnt':
            return '결과 음성 수'
        elif word == 'accExamCnt':
            return '누적 검사 수'
        elif word == 'accExamCompCnt':
            return '누적 검사 완료 수'
        elif word == 'accDefRate':
            return '누적 환진률'
        elif word =='createDt':
            return '등록일시분초'
        elif word == 'updateDt':
            return '수정일시분초'
        else:
            return word
    
    print ("\n*** 국내 발생 현향 ***\n")

    for key, value in body.items():
        print ("{} : {}".format(parsing(key), value))
    
def print_data_by_cities_api():
    URL = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson'
    API_KEY = 'f%2Fhg6LYbdDJSpfbO591Mc6yKoWwuB5nf52tDezzb0jTKIX7Wx8GxAbhP3An8NOIJmGPad2WCDTZRa1%2FoRclNGA%3D%3D'
    API_KEY = parse.unquote(API_KEY)
    PAGENO = '1'
    NUM_ROWS = '10'
    START_DATE = '20200310',
    today = date.today()
    END_DATE = '{0:04d}{1:02d}{2:02d}'.format(int(today.year), int(today.month), int(today.day))
    params = {
        'ServiceKey' : API_KEY,
        # 'pageNo' : PAGENO,
        # 'numOfRows' : NUM_ROWS,
        # 'startCreateDt' : START_DATE,
        # 'endCreateDt' : END_DATE
    }
    
    request = requests.get(URL, params=params)
    raw_data = xmltodict.parse(request.text)
    json_data = json.loads(json.dumps(raw_data))
    body = json_data['response']['body']['items']['item']

    def parsing(word):
        if word == 'seq':
            return '게시글번호'
        elif word == 'createDt':
            return '등록일시분초'
        elif word == 'updateDt':
            return '수정일시분초'
        elif word == 'deathCnt':
            return '사망자 수'
        elif word == 'defCnt':
            return '확진자 수'
        elif word == 'gubun':
            return '시도명'
        elif word == 'gubunCn':
            return '시도명(중국)'
        elif word == 'gubunEn':
            return '시도명(영어)'
        elif word == 'incDec':
            return '전일대비 증감 수'
        elif word == 'isolClearCnt':
            return '격리 해제 수'
        elif word == 'isolIngCnt':
            return '격리중 환자 수'
        elif word == 'localOccCnt':
            return '지역 발생 수'
        elif word == 'overFlowCnt':
            return '해외 유입 수'
        elif word == 'qurRate':
            return '10만명 당 발생률'
        elif word == 'stdDay':
            return '기준일시'
        else:
            return word
    
    print ("\n*** 시도별 발생동향 ***\n")
    for city in body:
        for key, value in city.items():
            print ("{} : {}".format(parsing(key), value))
        print ("")

def test():
    # print_overview()
    # print_data_by_cities()
    print_overview_api()
    print_data_by_cities_api()


test()
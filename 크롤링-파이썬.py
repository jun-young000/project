#!/usr/bin/env python
# coding: utf-8

# ## 김영란법 이후로 JSON 만들기

# In[1]:


# -*-coding: utf-8
# 시장/ 부시장 직속 부서들만 먼저!
json_hierarchy = [
    {
        "div": "균형발전본부",
        "child": "균형발전정책과/도시활성화과/도심권사업과/동남권사업과/동북권사업과/서부권사업과/주거환경과/한옥정책과"
    },
    {
        "div" : "서울특별시장"
    },
    {
       "div": "경제정책실",
       "child": [
           {
               "div": "거점성장추친단",
               "child": "도시제조업거점반/산업거점조성반/산업거점활성화반"
           },
           {
               "div": "경제일자리기획관",
               "child": "경제정책과/도시농업과/일자리정책과/지역상생경제과/창업정책과/캠퍼스타운활성화과/투자창업과"
           },
           {
               "div": "신성장산업기획관",
               "child": "금융투자과/미디어콘텐츠산업과/전략산업기반과"
           }
       ]
    },
    {
        "div" : "1인가구특별대책추진단"
    },
    {
        "div" : "대변인",
        "child" : "언론담당관"
    },
    {
        "div": "감사위원회",
        "child": "공공감사담당관/조사담당관/안전담당관/감사담당관"
    },

   {
        "div": "남북협력추친단",
        "child": "개발협력담당관/남북협력담당관"
    },   
    {
        "div": "노동공정상생정책관",
        "child": "공정경제담당관/소상공인정책담당관"
    },    
    {
        "div": "시민감사옴부즈만위원회"
    },
    {
        "div": "공공개발기획단"
    },
    {
        "div": "서울혁신기획관",
        "child": "인권담당관/지역공동체담당관/청년정책담당관/갈등조정담당관/민관협력담당관"
    },
    {
        "div": "시민소통기획관",
        "child": "시민소통담당관/시민봉사담당관/도시브랜드담당관/신속행정담당관/뉴미디어담당관/국제교류담당관"
    },
    {
        "div": "행정1부시장"
    },
    {
        "div": "균형발전본부",
        "child": "균형발전정책과/도시활성화과/도심권사업과/동남권사업과/동북권사업과/서부권사업과/주거환경과/한옥정책과"
    },
    {
        "div": "여성가족정책실",
        "child": "가족담당관/보육담당관/아이돌봄당당관/양성평등정책담당관/여성권익담당관/여성정책담당관/외국인다문화담당관"
    },
    {
        "div": "민생사법경찰단"
    },
    {
        "div": "비상기획관",
        "child": "민방위담당관"
    },
    {
        "div": "정보기획관",
        "child": "통계데이터담당관/정보기획담당관/정보통신보안담당관/공간정보담당관/정보시스템담당관"
    },
    {
        "div": "일자리노동정책관",
        "child": "사회적경제담당관/노동정책담당관/일자리정책담당관"
    },
    {
        "div": "노동민생정책관",
        "child": "사회적경제담당관/노동정책담당관/공정경제담당관/소상공인정책담당관/제로페이담당관"
    },
    {
        "div": "도시계획국",
        "child": "도시계확과/도시관리과/도시빛정책과/시설계획과/전략계획과/토지관리과"
    },
    {
        "div": "행정2부시장"
    },
    {
        "div": "도시공간개선단"
    },
    {
        "div": "기술심사담당관"
    },
    {
        "div": "정무부시장"
    },
   {
       "div": "기획조정실",
       "child": [
           {
               "div": "국제교류담당관"
           },
           {
               "div": "정책기획관",
               "child": "남북협력담당관/대외협력담당관/법률지원담당관/법무담당관/조직담당관/평가담당관/평가협업담당관/협력상생담당관"
           },
           {
               "div": "해외도시협력담당관"
           },
           {
               "div": "재정기획관",
               "child": "예산담당관/시민참여예산과/공기업담당관/재정관리담당관/시민참여예산담당관/재정균형발전담당관"
           }
       ]
    },
    {
       "div": "경제진흥본부",
       "child": {
           "div": "창조경제기획관",
           "child": "도시농업과/경제정책과/민생경제과/문화융합경제과/디지털창업과/투자유치과/소상공인지원과"
       }
    },
    {
          "div": "복지본부",
          "child":"자활지원과/어르신복지과/희망복지지원과/복지정책과/장애인복지정책과/인생이모작지원과/장애인자립지원과"
       },
    
      {
          "div": "복지정책실",
          "child":[
            {
              "div": "복지기획관",
              "child": "복지정책과/어르신복지과/인생이모작지원과/자활지원과/자원지원과/장애인복지정책과/장애인자립지원과/지역돌롬복지과"
            },
            {
              "div": "복지정책과"
            },
            {
              "div": "어르신복지과",
            },
            {
              "div": "인생이모작지원과"
            },
            {
              "div": "자활지원과"
            },
            {
              "div": "장애인복지정책과"
            },
            {
              "div": "장애인자립지원과"
            },
            {
              "div": "지역돌봄복지과"
            },
          ]
       },
    

       {
          "div": "문화본부",
          "child":[
            {
              "div": "문화정책과"
            },
            {
              "div": "한양도성도감"
            },
            {
              "div": "문화시설추진단",
              "child": "문화시설과/박물관"
            },
            {
              "div": "역사문화재과"
            },
            {
              "div": "디자인정책과"
            },
            {
              "div": "문화예술과"
            }
          ]
       },
    {
       "div": "도시교통본부",
       "child": [
           {
               "div": "교통기획관",
               "child": "버스정책과/주차계획과/택시물류과"
           },
           {
               "div": "교통운영과"
           },
           {
               "div": "교통정보과"
           },
           {
               "div": "교통정책과"
           },
           {
               "div": "교통지도과"
           },
           {
               "div": "버스정책과"
           },
           {
               "div": "보행정책과"
           },
           {
               "div": "자전거정책과"
           },
           {
               "div": "주차계획과"
           },
           {
               "div": "택시물류과"
           }
           
       ]
    },
           {
       "div": "도시교통실",
       "child": 
       [
           {
               "div": "교통기획관",
               "child": "교통정책과/도시철도과/물류정책과/버스정책과/주차계획과/택시물류과"
           },
           {
               "div": "교통운영과"
           },
           {
               "div": "교통정보과"
           },
           {
               "div": "교통정책과"
           },
           {
               "div": "교통지도과"
           },
           {
               "div": "보행정책과"
           },
           {
               "div": "보행친화기획과",
               "child": "교통운영과/교통정보과/교통지도과/보행정책과/자전거정책과"              
           },
           {
               "div": "자전거정책과"
           }
       ]
    },     
       {
          "div": "기후환경본부",
          "child":"기후대기과/기후변화대응과/녹색에너지과/대기관리과/대기정책과/생활환경과/에너지시민협력과/자원순환과/차량공해저감과/환경시민협력과/환경정책과"
       },
       {
          "div": "행정국",
          "child":"인사과/인력개발과/정보공개정책과/총무과/자치행정과"
       },
       {
          "div": "재무국",
          "child": "38세금징수과/계약심사과/재무과/세무과/자산관리과/세제과"
       },
       {
         "div": "평생교육국",
         "child": "평생교육과/청소년정책과/교육정책과/친환경급식"
       },
       {
         "div": "관광체육국",
         "child": "관광산업과/관광정책과/올림픽추친과/전국체전기획과/체육정책과/체육진흥과"
       },
       {
         "div": "시민건강국",
         "child": "감염병관리과/감영병연구센터/건강증진과/동물보호과/보건의료정책과/생활보건과/식품안전과/식품정책과/질병관리과/코로나19대응지원과"
       },
       {
         "div": "안전총괄본부",
         "child":
        [
           {
             "div":"서울역일대종합발전기획단"
           },
           {
              "div":"안전총괄관",
              "child": "안전총괄과/시설안전과/도로관리과/교량안전과/도로시설과/도로계획과/보도환경개선과/상황대응과"
           }
        ]
       },
    
    {
        "div" : "도시재생본부",
        "child" : "공공개발센터/공공재생과/광화문광장추친단/도시활성화과/역사도심재생과/재생정책과/재생협력과/주거사업과/주거재생과/주거환경과"
    },
    
    {
        "div" : "도시재생실",
        "child" : "공공재생과/광화문광장추친단/도시활성화과/역사도심재생과/재생정책과/주거재생과/주거환경개선과/한옥건축자선과"
    },
        
    {
        "div" : "물순환안전국",
        "child" : "물순환정책과/물재생계획과/물재생시설과/하천관리과"
    },
    
    {
        "div" : "미래청년기획단"                
    },
            
    {
        "div" : "서울민주주의위원회",
        "child" : "서울시민주주의담당관/서울협치담당관/시민숙의예산담당관/지역공동체담당관"
      },
    
    {
        "div": "스마트도시정책관",
        "child": "공간정보담당관/빅데이터담당관/스마트도시담당관/정보시스템당당관/정보통신보안담당관"
    },              
    {
        "div": "시민협력국",
        "child":"갈등관리협치과/사회협력과/시민숙의예산과/시민참여과/지역공동체과"
    },
    {
        "div" : "인권담당관"
    },
    {
        "div": "주택건축국",
        "child":"건축기획과/공동주택과/임대주택과/주택정책과/한옥조성과"
    },
    
    {
       "div": "주택건축본부",
       "child": [
           {
               "div": "주거정비과",
               "child": "주거사업협력센터"
           },
           {
               "div": "건축기획과"
           },
           {
               "div": "공공주택과"
           },
           {
               "div": "공동주택과"
           },
           {
               "div": "주거사업과"
           },
           {
               "div": "주택공급과"
           },
           {
               "div": "주택정책과",      
           },
           {
               "div": "지역건축안전센터"
           }
       ]
    },     
    {
        "div": "주택건축실",
        "child":"공동주택지원과/재정비촉진사업과/전략사업과/주거정비과/주택정책과/주택정책지원센터/지역건축안전센터"
    },
    {
        "div": "지역발전본부",
        "child":"동남권계획과/동남권사업과/동남권사업단/동남권조성과/동북권사업과/동북권사업단/서남권사업과/서북권사업과"
    },
    {
        "div": "청년청"
    },
    {
        "div": "지역발전본부",
        "child":"동남권계획과/동남권사업과/동남권사업단/동남권조성과/동북권사업과/동북권사업단/서남권사업과/서북권사업과"
    },
    {
        "div": "푸른도시국",
        "child":"공원녹지정책과/공원조성과/산지방재과/서울로운영단/자연생태과/조경과"
    }
    ]


# ## JSON을 이용해 url 만들기

# In[2]:


from urllib import parse

# URL 추출
urls = [];
tail = '&dept%5B%5D='

# {} dict 
# [] list

def extract_value(data, origin_url):
    if(isinstance(data, list)):
        for single_list in data:
            extract_value(single_list, origin_url)
    elif(isinstance(data, dict)):
        #dict {} 일 경우
        if(len(data) == 1):
            if(origin_url != ''):
                origin_url = origin_url + tail
            div = data.get('div')
            url = origin_url + parse.quote(div)
            urls.append(url)
        else:
            div = data.get('div')
            child = data.get('child', 'empty')
            if origin_url != '':
                origin_url = origin_url + tail
            extract_value(child, origin_url + parse.quote(div))
    elif(isinstance(data, str)):
        divs = data.split('/')
        for single_div in divs:
            url = origin_url + tail + parse.quote(single_div)
            urls.append(url)

extract_value(json_hierarchy, "")


# ## 크롤링

# In[3]:


# 필요한 라이브러리 가져오기
from urllib import request
# !pip install html5lib
# import html5lib
# !pip install lxml
# import lxml
import pandas as pd
import numpy as np


# In[ ]:


import requests
from bs4 import BeautifulSoup
import re
import time

df = pd.DataFrame()
base_url_head = "https://opengov.seoul.go.kr/expense?dept%5B%5D=%EC%84%9C%EC%9A%B8%EC%8B%9C%EB%B3%B8%EC%B2%AD&dept%5B%5D="
url_2016 = "&year=2016&month="
url_2017 = "&year=2017&month="
url_2018 = "&year=2018&month="
url_2019 = "&year=2019&month="
url_2020 = "&year=2020&month="
url_2021 = "&year=2021&month="
column_div = "1소속부서"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

# urls돌면서 데이터 가져오기
for div in urls:
    div_url = (base_url_head + div)
    # unquote_div : url 첫부분 가져와서 
    unquote_div = parse.unquote(div)
    div_name = re.search('([가-힣]*)&de', unquote_div)
    if div_name is None:
        div_name = unquote_div
    else:
        div_name = div_name.group(1)

        
        
        
    for month in range(1,6): 
        url_month = div_url + url_2021 + str(month)
        res = requests.get(url_month,  headers=headers)
        time.sleep(2)
        soup = BeautifulSoup(res.content,'html.parser') 
        table = soup.find_all('table')
#         df_month = pd.read_html(str(table))
        

        try:
            df_month = pd.read_html(str(table))
#             df_month = pd.read_html(url_month)[1]
            # decode된 url의 첫 부분을 1소속부서 column에 넣어주기
            df['column_div'] = div_name
            df = df.append(df_month)
            print(url_month)
        except :
            print('err2021') 
            print(url_month)
            pass        
                
        
        
    for month in range(1,13): 
        url_month = div_url + url_2020 + str(month)
        res = requests.get(url_month,  headers=headers)
        time.sleep(2)
        soup = BeautifulSoup(res.content,'html.parser') 
        table = soup.find_all('table')
#         df_month = pd.read_html(str(table))
        

        try:
            df_month = pd.read_html(str(table))
#             df_month = pd.read_html(url_month)[1]
            # decode된 url의 첫 부분을 1소속부서 column에 넣어주기
            df['column_div'] = div_name
            df = df.append(df_month)
            print(url_month)
        except :
            print('err2020') 
            print(url_month)
            pass
  


    for month in range(1,13): 
        url_month = div_url + url_2019 + str(month)
        res = requests.get(url_month,  headers=headers)
        time.sleep(2)
        soup = BeautifulSoup(res.content,'html.parser') 
        table = soup.find_all('table')
#         df_month = pd.read_html(str(table))
        

        try:
            df_month = pd.read_html(str(table))
#             df_month = pd.read_html(url_month)[1]
            # decode된 url의 첫 부분을 1소속부서 column에 넣어주기
            df['column_div'] = div_name
            df = df.append(df_month)
            print(url_month)
        except :
            print('err2019') 
            print(url_month)
            pass
  



    for month in range(1,13): 
        url_month = div_url + url_2018 + str(month)
        res = requests.get(url_month,  headers=headers)
        time.sleep(2)
        soup = BeautifulSoup(res.content,'html.parser') 
        table = soup.find_all('table')
#         df_month = pd.read_html(str(table))
        

        try:
            df_month = pd.read_html(str(table))
#             df_month = pd.read_html(url_month)[1]
            # decode된 url의 첫 부분을 1소속부서 column에 넣어주기
            df['column_div'] = div_name
            df = df.append(df_month)
            print(url_month)
        except :
            print('err2018') 
            print(url_month)
            pass        
   


    for month in range(1,13): 
        url_month = div_url + url_2017 + str(month)
        res = requests.get(url_month,  headers=headers)
        time.sleep(2)
        soup = BeautifulSoup(res.content,'html.parser') 
        table = soup.find_all('table')
#         df_month = pd.read_html(str(table))
        

        try:
            df_month = pd.read_html(str(table))
#             df_month = pd.read_html(url_month)[1]
            # decode된 url의 첫 부분을 1소속부서 column에 넣어주기
            df['column_div'] = div_name
            df = df.append(df_month)
            print(url_month)
        except :
            print('err2017') 
            print(url_month)
            pass        
    
    
    
        
    for month in range(11,13): 
        url_month = div_url + url_2016 + str(month)
        res = requests.get(url_month,  headers=headers)
        time.sleep(2)
        soup = BeautifulSoup(res.content,'html.parser') 
        table = soup.find_all('table')
#         df_month = pd.read_html(str(table))
        

        try:
            df_month = pd.read_html(str(table))
#             df_month = pd.read_html(url_month)[1]
            # decode된 url의 첫 부분을 1소속부서 column에 넣어주기
            df['column_div'] = div_name
            df = df.append(df_month)
            print(url_month)
        except :
            print('err2016') 
            print(url_month)
            pass        
                
        
        
    
#     for month in range(1,13): 
#         url_month = div_url + url_2019 + str(month)
#         try:
#             df_month = pd.read_html(url_month)[1]
#             df_month = pd.read_html(url_month)[1]
#             # decode된 url의 첫 부분을 1소속부서 column에 넣어주기
#             df_month[column_div] = div_name
#             df = df.append(df_month)
#             print(url_month)
#         except IndexError:
#             print('err')
#             print(url_month)

    
#     for month in range(1,13): 
#         url_month = div_url + url_2018 + str(month)
#         try:
#             df_month = pd.read_html(url_month)[1]
#             # decode된 url의 첫 부분을 1소속부서 column에 넣어주기
#             df_month[column_div] = div_name
#             df = df.append(df_month)
#             print(url_month)
#         except IndexError:
#             print('err')
#             print(url_month)

    
#     for month in range(1,13): 
#         url_month = div_url + url_2017 + str(month)
#         try:
#             df_month = pd.read_html(url_month)[1]
#             # decode된 url의 첫 부분을 1소속부서 column에 넣어주기
#             df_month[column_div] = div_name
#             df = df.append(df_month)
#             print(url_month)
#         except IndexError:
#             print('err')
#             print(url_month)

        
#     for month in range(1,13): 
#         url_month = div_url + url_2016 + str(month)
#         try:
#             df_month = pd.read_html(url_month)[1]
#             # decode된 url의 첫 부분을 1소속부서 column에 넣어주기
#             df_month[column_div] = div_name
#             df = df.append(df_month)
#             print(url_month)
#         except IndexError:
#             print('err')
#             print(url_month)

    
# 왜 table로 안들어오지????왜오애ㅗ애왜왱


# In[ ]:


df['column_div'].unique()


# In[ ]:


df.describe()


# In[ ]:


df.info()


# In[ ]:


df.shape


# In[ ]:


df


# In[ ]:


df.head(2)


# In[ ]:


df.tail(2)


# In[ ]:


# 크롤링하는데 오래 걸리니 데이터를 파일로 저장해두자
from IPython.display import FileLink, FileLinks

df.to_csv("raw.csv", index=False)
# df_copy.to_excel('C:\workspace\djangoPrj\popular_restaurants_from_officials/seoul_dining_crawl.xlsx', index=False)

FileLinks('C:\\Users\Administrator\Desktop\coding\python\muticam\project')


# In[ ]:


df = pd.read_csv('raw.csv')
df.info()


# In[ ]:





# ## Tidy 1차 : column 분리하기

# In[ ]:


# 집행장소와 주소를 분리하자
df_copy = df.copy()
df_copy['집행지주소'] = df_copy['사용장소'].str.extract(r'\((.*)\)')
df_copy['집행지주소'] = df_copy['집행지주소'].replace(' ', '')
df_copy['집행지명'] = df_copy['사용장소'].str.extract(r'(.*)\(')
df_copy['집행지명'] = df_copy['집행지명'].replace(' ', '')
del df_copy['사용장소']


# In[ ]:


# 필요없는 Column 없애기
del df_copy['연번']
del df_copy['부서명']


# In[ ]:


# 집행일시를 년/월/일/시간으로 분리하자
df_copy['year'] = df_copy['사용일시'].str.extract(r'(20..)')
df_copy['month'] = df_copy['사용일시'].str.extract(r'-(\d\d)-')
df_copy['day'] = df_copy['사용일시'].str.extract(r'-(\d\d\s)')
df_copy['time'] = df_copy['사용일시'].str.extract(r'(\d?\d:\d?\d)')


# In[ ]:


del df_copy['사용일시']
df_copy.head(3)


# In[ ]:


df_copy['집행지명'] = df_copy['집행지명'].str.replace(' ', '')


# In[ ]:


df_copy = df_copy[df_copy['집행지명'].str.contains('파리바게[트뜨]') == False]


# In[ ]:


df_copy = df_copy[df_copy['집행지명'].str.contains('[카페|커피|스타벅스]') == False]
df_copy = df_copy[df_copy['집행지명'].str.contains('[온누리|상품권|시청|격려|우정사업|구매]') == False]
df_copy = df_copy[df_copy['집행지명'].str.contains('피자') == False]
df_copy = df_copy[df_copy['집행지명'].str.contains('구매') == False]
df_copy.info()


# In[ ]:


df_copy.to_csv('tidy_1.csv', index=False)


# In[ ]:


df = pd.read_csv('tidy_1.csv')
df.info()


# In[ ]:


# 참가자수 숫자로 변환하기# num에 널값이 많다 왜지?
people= df['사용자 및 인원'].str.extract(r'[\s|외|총|등]?(\d+)\s?[명|인]?')
df['num'] = people
df = df[df['num'].isnull() == False]
df['num'] = df['num'].astype(int)

df.info()


# In[ ]:


df['num'] = df['num'] + 1


# In[ ]:


df['cnt'] = 1
df


# In[ ]:


df.columns=['소속부서1','구분','집행목적',"집행금액","대상인원","결제방법","집행목적","집행지주소","집행지명","year","month","day","time","cnt","num"]


# In[ ]:


df.info()


# In[ ]:


df.to_csv('tidy_2.csv', index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





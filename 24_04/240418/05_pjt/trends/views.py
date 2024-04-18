from django.shortcuts import render, redirect
from .models import Keyword, Trend
from .forms import KeywordModelForm
from bs4 import BeautifulSoup
from selenium import webdriver
import re

import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64


# Create your views here.

# 키워드 저장 및 keyword.html 렌더링
def keyword(request):
    form = KeywordModelForm()
    keywords = Keyword.objects.all()
    # POST 요청에 포함된 데이터를 나타내는 딕셔너리 형태의 객체 = request.POST
    if request.method == 'POST':
        form = KeywordModelForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            form.save()
            # keyword 뷰 함수로 리디렉션하라는 뜻
            return redirect('trends:keyword')
    context = {
        'form': form,
        'keywords': keywords,
    }
    return render(request, 'trends/keyword.html', context)

def keyword_detail(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')

def crawling(request):
    keywords = Keyword.objects.all()
    for keyword in keywords:
        # Keyword 모델의 name 필드에 들어가는 값을 검색어로 입력
        url = f"https://www.google.com/search?q={keyword.name}"

        # 크롬 브라우저가 열림
        # 이 때, 동적인 내용들이 모두 채워짐
        driver = webdriver.Chrome()
        driver.get(url)
        # 열린 페이지 소스들을 받아온다.
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        # 각 게시물을 가져오자!
        # 공통적으로 div태그 + appbar class를 가져왔다.
        # 단일 검색을 할 경우엔 id 태그를, 여러 개 검색을 할 경우 클래스 태그를 가져오는 것이 좋다.
        # select() 메서드를 사용하면 CSS 선택자를 지정하여 
        # 문서에서 특정한 요소나 요소 그룹을 선택할 수 있다.
        # 이후 리스트로 반환한다.
        g_list = soup.select('div.appbar')
        for g in g_list:
            # re.sub() 함수는 python의 're' 모듈에서 제공하는 정규 표현식을 사용하여
            # 문자열을 다른 문자열로 치환하는 함수이다.
            # re = Regular Expression(정규 표현식)
            # re.sub(pattern, repl, string, count = 0, flags = 0) 함수의 인자는 다음과 같다.
            # pattern: 치환할 패턴을 나타내는 정규 표현식
            # repl: 대체할 문자열이나 함수
            # string: 대상 문자열
            # count: 선택적 매개변수로, 치환할 최대 개수를 나타낸다.
            # 기본값은 0이고, 0인 경우 모든 패턴이 치환된다.
            # flags: 선택적 매개변수로, 정규 표현식의 동작을 제어하는 플래그를 설정한다.
            # re.sub(r'[^0-9]', '', 'abc123def456') -> 문자열에 대해 숫자가 아닌 모든 문자를 제거하라는 뜻
            # BeautifulSoup에서는 CSS 선택자에서 요소의 태그명을 생략할 수 있다.
            # 따라서 div#result-stats == #result-stats
            # g.select_one('#result-stats').text.split('(')[0]
            # 뽑아낸 리스트에는 "검색결과 약 7,030,000개" (0.39초)"가 담길텐데
            # 앞의 결과 개수 숫자만 뽑고 싶어서 '('을 기준으로 나누어 그 앞에 것만 가져가는 것이다.
            result = re.sub(r'[^0-9]', '', g.select_one('#result-stats').text.split('(')[0])
            try:
                # filter() 메서드는 특정 조건을 가진 모든 객체를 검색할 수 있다.
                # 따라서 filter를 통해 검색한 필터링된 데이터 중에 
                # name필드가 keyword.name과 일치하는 데이터를 가져온다.
                data = Trend.objects.filter(search_period="all").get(name=keyword.name)
                data.result = int(result)
                data.save()
            except:
                # 없을 경우 새로 만든다.
                Trend.objects.create(name=keyword.name, result=int(result), search_period="all")
    trends = Trend.objects.all()
    context = {
        'trends': trends
    }
    return render(request, 'trends/crawling.html', context)

# 크롤링 수행 후 수행 결과 막대 그래프 생성 및 crawling_histogram.html 렌더링
def crawling_histogram(request):
    trends = Trend.objects.all()
    keyword_list = []
    result_list = []
    for trend in trends:
        if trend.search_period == "all":
            keyword_list.append(trend.name)
            result_list.append(trend.result)
    # import matplotlib.pyplot as plt
    # pyplot은 시각화 역할을 한다. -> 다양한 그래프 및 플롯 생성 가능
    # 이미 존재하는 그래프나 플롯을 초기화한다.
    plt.clf()
    # plt.bar() = 막대 그래프 생성
    # 주요 매개변수는 다음과 같다.
    # 'x': 막대 그래프의 x축에 표시할 데이터를 나타내는 리스트 또는 배열
    # 'height': 막대 그래프의 각 막대의 높이를 나타내는 리스트 또는 배열
    # 'width': 막대의 너비를 지정한다. 기본값은 0.8
    # 'color': 막대의 색상을 지정한다. 기본값은 파란색
    # 'label': 그래프의 범례에 표시될 레이블을 지정한다.
    plt.bar(x=keyword_list, height=result_list, label='Trends', color = 'green')
    # 제목 추가
    plt.title('Technology Trend Analysis')
    # x축 라벨링
    plt.xlabel('Keyword')
    # y축 라벨링
    plt.ylabel('Result')
    # 그래프에 범례를 추가한다.
    # 'label' 인자를 사용하여 plt.bar() 함수에 지정한 레이블을 사용한다.
    plt.legend()
    # 그리드를 추가한다. 이는 그래프의 배경에 격자 무늬를 추가한다.
    plt.grid()

    # 바이트 데이터를 저장하기 위한 버퍼를 생성
    # BytesIO() 클래스는 메모리 내 바이트 데이터를 다루기 위한 클래스, 이미지 데이터를 저장한다.
    buffer = BytesIO()
    # savefig() -> 그래프를 이미지로 저장하는 함수
    # 첫 번째 인자: 이미지를 저장할 파일 객체
    # format 매개변수를 통해 이미지의 형식을 지정한다.
    plt.savefig(buffer, format='png')
    # buffer에 저장된 바이트 데이터를 Base64로 인코딩하여 문자열로 변환한다.
    # Base64는 이진 데이터를 ASCII 문자로 변환하는 인코딩 방식 중 하나이며
    # 웹 페이지에서 이미지를 직접 표시할 수 있도록 한다.
    # base64 모듈을 사용해 이 작업을 수행하고, 인코딩된 문자열을 image_base64 변수로 저장
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    # 사용 완료된 buffer는 닫는다.
    buffer.close()
    context = {
        'chart_image': f'data:image/png;base64, {image_base64}',
    }
    return render(request, 'trends/crawling_histogram.html', context)

# 지난 1년을 기준으로 크롤링 수행 후 수행 결과 막대 그래프 생성 및 crawling_advanced.html 렌더링
def crawling_advanced(request):
    keywords = Keyword.objects.all()
    for keyword in keywords:
        url = f"https://www.google.com/search?q={keyword.name}&tbs=qdr:y"
        driver = webdriver.Chrome()
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        g_list = soup.select('div.appbar')
        # 지난 1년을 기준으로 크롤링을 수행해야 하므로 기간을 year로 잡았다.
        for g in g_list:
            result = re.sub(r'[^0-9]', '', g.select_one('#result-stats').text.split('(')[0])
            try:
                data = Trend.objects.filter(search_period='year').get(name=keyword.name)
                data.result = int(result)
                data.save()
            except:
                Trend.objects.create(name=keyword.name, result=int(result), search_period="year")
    
    trends = Trend.objects.all()
    keyword_list = []
    result_list = []
    for trend in trends:
        if trend.search_period == "year":
            keyword_list.append(trend.name)
            result_list.append(trend.result)
        
    plt.clf()
    plt.bar(x=keyword_list, height=result_list, label='Trends', color = 'yellowgreen')
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.legend()
    plt.grid()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    context = {
        'chart_image': f'data:image/png;base64, {image_base64}',
    }
    return render(request, 'trends/crawling_advanced.html', context)
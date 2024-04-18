# 05 PJT

###### 이번에는 특별히 문제가 기준이 아닌 파일 기준으로 README를 작성하고자 한다.

## forms.py
```python
class KeywordModelForm(forms.ModelForm):
    # form class의 설정을 담고 있다.
    # class Meta에 폼의 설정이나 동작에 영향을 주는 데이터를 모아둘 수 있다.
    class Meta:
        # 이 폼이 사용할 모델을 지정한다.
        # models.py의 Keyword 모델 사용
        model = Keyword
        # Keyword 모델 내에 있는 필드 중 사용할 필드를 적는다.
        # 튜플 형태로 필드 이름을 나열하고, 
        # 하나의 필드만 사용할 때에도 쉼표를 꼭 붙여주어야 한다.
        fields = ('name',)
        # widgets은 웹 어플리케이션에서 사용자가 입력한 데이터를 받을 수 있는 HTML 요소들을 의미한다.
        # Django에서는 폼의 필드를 어떻게 보여줄 지 결정하는 요소이다.
        widgets = {
            'name': TextInput
        }
        # 각 필드의 라벨을 지정한다.
        # forms.py를 이용해 label을 지정할 경우
        # 자동으로 키워드':', 옆에 콜론까지 붙여준다.
        # 즉 따로 콜론을 쓸 필요가 없다.(쓰면 2개 출력된다)
        labels = {
            'name': '키워드',
        }
```

### views.py

```python
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
```

```python
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
```

## 소감
 1. 크롤링 자체를 처음하기 때문에 크롤링에서는 크게 문제가 없었으나 
    result = re.sub(r'[^0-9]', '', g.select_one('#result-stats').text.split('(')[0])
    이 문장을 적어내지 못해서 상당한 시간을 사용하였다.
    특히 흔히 하던 split() 메서드를 사용해서 원하는 정보만을 뽑아내는 아이디어를 보고
    알고리즘에서 익혔던 것들을 잘 활용해야 한다는 것을 깨달았다.

 2. 얼마 차이도 없었는데 막대 그래프 만드는 과정을 까먹어서 
    하나씩 배운다는 생각으로 주석을 작성했다.
    이번 주 내내 본격적으로 주석을 작성하기 시작하면서 시간은 오래 걸리지만 장기 기억으로의 전환율이 비약적으로 상승한 것을 체감할 수 있었다.
    앞으로도 주석을 더 열심히 달 예정이다.

 3. buffer를 사용해서 이미지로 저장하는 과정은 계속 연습해야 할 듯 싶다.
    이상하게 문장이 직관적이라는 느낌을 못 받아서 잘 안 외워진다.

 4. 이번 주 내내 django 추가 연습을 진행했는데 확실히 작성 과정이 매끄러웠다.
    하지만 더욱 연습해야 할 듯...
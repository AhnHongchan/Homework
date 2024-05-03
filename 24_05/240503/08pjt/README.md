# 08pjt

## ver1

### 전역변수

```python
df = pd.read_csv('./data/test_data.csv', encoding='cp949')
data = df.to_dict('records')
```
- pandas를 사용해 csv 파일을 읽어온다
- cp949: 한글 인코딩을 나타내는 코드 페이지이다.
- csv 파일을 Dataframe으로 변환하는 과정
- records: 리스트 원소를 각각 하나의 레코드로 만들어 주기 위해 쓰는 옵션
- to_dict : DataFrame을 딕셔너리의 리스트로 변환해주는 메서드

### A

```python
def Dataset(request):
    return JsonResponse({'data': data},  json_dumps_params={'ensure_ascii': False})
```
- JSON 파일로 응답, 
- json_dumps_params={'ensure_ascii': False} : 유니코드 이스케이프를 방지하기 위한 옵션
-  한글이 정상적으로 유니코드 형태로 출력된다.

### B

```python
def null(request):
    df.fillna('Null', inplace=True)
    data2 = df.to_dict('records')
    return JsonResponse({'data': data2},  json_dumps_params={'ensure_ascii': False})
```
- pandas함수 중 결측값(NaN)을 다른 값으로 채워넣어주는 함수인 fillna 사용
- 문법 => dataframe형태의변수.fillna('다른 값', inplace=True)

### C

```python
def create_dataset(request):

    df_del = df.drop(df[df['나이'] == 'Null'].index)
    mean_age = df_del['나이'].mean()
    df_del['차이'] = abs(df_del['나이'] - mean_age)
    df_sorted = df_del.sort_values(by='차이')
    similar_age = df_sorted.head(10)
    new_df = pd.DataFrame(similar_age)
    del_df = new_df.drop(['차이'], axis=1)
    new_data = del_df.to_dict('records')

    return JsonResponse({'new_data': new_data}, json_dumps_params={'ensure_ascii': False})
```
0. 나이 값에 Null이 들어간 행을 전부 제거한 새로운 df를 만든다.
1. 평균 나이 구하기
2. 평균과의 차이 구하기
3. '차이'를 기준으로 정렬
4. 가장 비슷한 나이인 10개 행 추출
..ead 메서드를 사용하면 상위 행을 추출할 수 있음
5. 새로운 DataFrame 생성
6. 딕셔너리의 리스트로 변환

### D

```python
from locust import HttpUser, task, between

class SampleUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        print('test start')

    @task
    def create(self):
        self.client.get("test/create/")
```
- locust 테스트를 위한 locust_test.py의 코드 구성

### 결과 및 고찰

> csv파일을 view함수로 불러오는 과정에서 인코딩 관련한 에러가 발생해 pd.read_csv에 encoding='cp949'를 추가해 한글 관련된 인코딩 에러를 해소했다. B에서는 fillna라는 pandas함수를 사용하기 위해 제공된 자료를 활용했다. C함수를 만들 때는 평균나이를 구하는 알고리즘을 구현했지만 B함수를 실행한 후 C를 실행하면 Null이라는 스트링 값 때문에 에러가 발생해 Null이 채워진 항목을 제외하고 평균 나이를 구할 수 있도록 수정했다. D를 수행한 후 우리 조의 결과는 이용자수 100명, 동접자수 10명, 평균 RPS 48.6, 평균 응답시간 4ms 정도로, 다른 어떤 조의 알고리즘과 비교했을 때 RPS가 약 20 많이, 평균 응답시간 약 1992ms 빠르게 높은 성능으로 측정되었다.
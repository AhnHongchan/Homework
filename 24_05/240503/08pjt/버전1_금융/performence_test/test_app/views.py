from django.http import JsonResponse
from rest_framework.decorators import api_view
import random
import pandas as pd


array_length = 1000
random_range = 5000

# pandas를 사용해 csv 파일을 읽어온다
# cp949: 한글 인코딩을 나타내는 코드 페이지이다.
# csv 파일을 Dataframe으로 변환하는 과정
df = pd.read_csv('./data/test_data.csv', encoding='cp949')
# records: 리스트 원소를 각각 하나의 레코드로 만들어 주기 위해 쓰는 옵션
# to_dict : DataFrame을 딕셔너리의 리스트로 변환해주는 메서드
data = df.to_dict('records')


def Dataset(request):

    # JSON 파일로 응답, 
    # json_dumps_params={'ensure_ascii': False} : 유니코드 이스케이프를 방지하기 위한 옵션
    #  한글이 정상적으로 유니코드 형태로 출력된다.
    return JsonResponse({'data': data},  json_dumps_params={'ensure_ascii': False})

def null(request):

    # pandas함수 중 결측값(NaN)을 다른 값으로 채워넣어주는 함수인 fillna 사용
    # 문법 => dataframe형태의변수.fillna('다른 값', inplace=True)
    df.fillna('Null', inplace=True)
    data2 = df.to_dict('records')
    return JsonResponse({'data': data2},  json_dumps_params={'ensure_ascii': False})


def create_dataset(request):

    # 0. 나이 값에 Null이 들어간 행을 전부 제거한 새로운 df를 만든다.
    df_del = df.drop(df[df['나이'] == 'Null'].index)
    # 1. 평균 나이 구하기
    mean_age = df_del['나이'].mean()
    # 2. 평균과의 차이 구하기
    df_del['차이'] = abs(df_del['나이'] - mean_age)
    # 3. '차이'를 기준으로 정렬
    df_sorted = df_del.sort_values(by='차이')
    # 4. 가장 비슷한 나이인 10개 행 추출
    # .head 메서드를 사용하면 상위 행을 추출할 수 있음
    similar_age = df_sorted.head(10)
    # 5. 새로운 DataFrame 생성
    new_df = pd.DataFrame(similar_age)
    del_df = new_df.drop(['차이'], axis=1)
    # 6. 딕셔너리의 리스트로 변환
    new_data = del_df.to_dict('records')


    return JsonResponse({'new_data': new_data}, json_dumps_params={'ensure_ascii': False})
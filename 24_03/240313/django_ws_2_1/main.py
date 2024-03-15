import requests

API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttbhha04081429001'
params = {
    'ttbkey': API_KEY,
    'Version': '20131101',
    'MaxResults': 50,
    'start': 1,
    'output': 'js',
    'SearchTarget': 'Book',
    'QueryType': 'ItemNewSpecial'
}

response = requests.get(API_URL, params = params).json()

for item in response['item']:
    title = item['title']
    author = item['author']
    pub_date = item['pubDate']
    isbn = item['isbn']
    print("제목:", title)
    print("저자:", author)
    print("출간일:", pub_date)
    print("ISBN:", isbn)
    print()
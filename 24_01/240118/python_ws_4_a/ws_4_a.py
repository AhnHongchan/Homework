from conf.settings import NAME
from conf.settings import MAIN_URL
from utils.create_url import create_url
result = create_url(NAME, MAIN_URL)
print(result)
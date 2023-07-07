import requests
import re
import json
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

url = 'https://www.ting275.com/book/13325.html'
target_link = 'https://www.ting275.com/pc/index/getchapterurl/bookId/13325/chapterId/'

response = requests.get(url, headers=headers)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    elements = soup.select('ul.list-unstyled.text-center.play-list li a')


    #空字典
    data_list = []

    for element in elements:
        title = element.get('title')
        
        url = element.get('href')
        
        #去掉了 "/play/13325/" 和 ".html" 部分的字符串。
        new_url = re.sub(r"/play/13325/", "", url)
        
        # 加上最終請求的target_link
        new_url = target_link + new_url

        # 存入字典        
        data = {'title': title, 'url': new_url}
        data_list.append(data)


    # 将 data_list 列表存储为 JSON 文件
    with open('data.json', 'w') as file:
        json.dump(data_list, file)

else:
    print('请求失败，状态码:', response.status_code)

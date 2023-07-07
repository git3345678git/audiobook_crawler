import requests
import time
import random
import json

# 設置http header
headers = {
    'Cookie': '_gcl_au=1.1.964171729.1688182834; Hm_lvt_3fa0077fd7d807269fab93e71a0b26ab=1688182834,1688282633; __gads=ID=7ea084171b62478f-22eee0e576e2000b:T=1688182834:RT=1688282635:S=ALNI_MaPB2HI2MN-tAf0s5fCuv6cy-iDQQ; __gpi=UID=00000c8992c5f199:T=1688182834:RT=1688282635:S=ALNI_MZ7np7mR-XlDlXV4PqRooVXWvXv1g; Hm_lpvt_3fa0077fd7d807269fab93e71a0b26ab=1688282885',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://www.ting275.com/play/13325/5506984.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Te': 'trailers'
}

# 請求回json的m4a網址
def req_get_json(url, headers):
    response = requests.get(url, headers=headers)
    # 检查响应状态码
    if response.status_code == 200:
        # 响应成功
        data = response.json()
        # json 取 src
        src = data['src']

        #如果訪問過快會拿到
        #http://audio.cos.xmcdn.com/xxx.m4a
        if src.startswith('http'):
            return src
        
        # 星號做為分割
        decimals = src.split("*")
        # 全部hex轉為ascii 並加在一起
        download_link = "".join([chr(int(dec)) for dec in decimals])

        return download_link
    else:
        # 响应失败
        print('请求' + url + '失败:', response.status_code)

        
    

# 空字典
download_list = []

# 讀取文本所有url 並請求
with open('data.json', 'r') as file:
    json_data = file.read()

# 解析 JSON 字串
items = json.loads(json_data)

# 循環獲取 TITLE 跟 URL
for item in items:
    
    title = item.get("title", "")
    url = item.get("url", "")
    
    # 請求獲取m4a下載地址
    download_link = req_get_json(url, headers)
    # 存入字典
    data = {'title': title, 'url': download_link}
    download_list.append(data)


    #顯示進度
    print(title + "已存入")
    print(download_link + "已存入")

    
    # 生成一个0到5之间的随机数睡眠
    random_time = random.uniform(25, 35)
    time.sleep(random_time)



# 将 download_list 列表存储为 JSON 文件
with open('download_list.json', 'w') as file:
    json.dump(download_list, file)

import requests

url = 'https://qldt.ptit.edu.vn/api/auth/login'
payload = {
    'username': 'tai khoan qldt ',
    'password': 'mat khau qldt',
    'grant_type': 'password'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

r = requests.post(url, data=payload, headers=headers)
token = "Bearer " + r.json()['access_token']

data_url = 'https://qldt.ptit.edu.vn/api/sch/w-locdstkbtuanusertheohocky'
date_header = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Authorization': token,
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Cookie': '__zi=3000.SSZzejyD2CeYdgEpqWm8sIZ9eUVCGWR1QvMpxTDGHDDzXFUobL95bZ21yBwILGcJC8Mxl91N3PaqXx6s.1; _ga=GA1.3.649927060.1691975008; _ga_GXEC6VM3ZH=GS1.3.1696241093.1.1.1696241130.0.0.0; _gid=GA1.3.1341155159.1696550973; _ga_WF3VN29N2R=GS1.3.1696550974.29.0.1696550974.0.0.0; ASP.NET_SessionId=4pst5e4zv4udscqkv1fiieqf',
    'Host': 'qldt.ptit.edu.vn',
    'Idpc': '-6425855506493750551',
    'Origin': 'https://qldt.ptit.edu.vn',
    'Pragma': 'no-cache',
    'Referer': 'https://qldt.ptit.edu.vn/',
    'Sec-Ch-Ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

data_payload = {
    "filter": {
        "hoc_ky": 20231,
        "ten_hoc_ky": ""
    },
    "additional": {
        "paging": {
            "limit": 100,
            "page": 1
        },
        "ordering": [
            {
                "name": None,
                "order_type": None
            }
        ]
    }
}

k = requests.post(data_url, json=data_payload, headers=date_header)
for j in range(0,len(k.json()['data']['ds_tuan_tkb'])):
    print(k.json()['data']['ds_tuan_tkb'][j]['thong_tin_tuan'])
    for i in range(0,len(k.json()['data']['ds_tuan_tkb'][j]['ds_thoi_khoa_bieu'])):
        start = k.json()['data']['ds_tuan_tkb'][j]['ds_thoi_khoa_bieu'][i]['tiet_bat_dau']
        print("Thứ :",k.json()['data']['ds_tuan_tkb'][j]['ds_thoi_khoa_bieu'][i]['thu_kieu_so'])
        print(k.json()['data']['ds_tuan_tkb'][j]['ds_thoi_khoa_bieu'][i]['ten_mon'])

        print(k.json()['data']['ds_tiet_trong_ngay'][int(start-1)]['gio_bat_dau'],"-",k.json()['data']['ds_tiet_trong_ngay'][int(start-1)]['gio_ket_thuc'])



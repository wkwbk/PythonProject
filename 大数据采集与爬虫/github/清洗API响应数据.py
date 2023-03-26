import requests

search_content = "spider"
api_url = f"https://api.github.com/search/repositories?q={search_content}"
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69"}

req = requests.get(api_url, headers=ua)
print("状态码:", req.status_code)

req_dic = req.json()
print(f"与 {search_content} 有关的库总数:", req_dic["total_count"])
print("本次请求是否完整:", req_dic["incomplete_results"])

req_dic_items = req_dic["items"]
print("当前页面返回的项目数量:", len(req_dic_items))

req_dic_items_first = req_dic_items[0]
print("获取第一个项目的 ID:", req_dic_items_first["id"])
print("查看第一个项目中的内容数量:", len(req_dic_items_first))
print("获取第一个项目中的具体内容:", req_dic_items_first)
print("获取第一个项目作者的登录名:", req_dic_items_first["owner"]["login"])
print("获取第一个项目的全名:", req_dic_items_first["full_name"])
print("获取第一个项目的描述:", req_dic_items_first["description"])
print("获取第一个项目评分:", req_dic_items_first["score"])
print("获取第一个项目的地址:", req_dic_items_first["html_url"])

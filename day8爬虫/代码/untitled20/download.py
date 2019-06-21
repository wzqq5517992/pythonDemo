import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}

url = "https://cache.video.iqiyi.com/jp/dash?tvid=733060800&bid=300&vid=3d167e5f33e5533da70d7f5d118664db&src=01080031010000000000&vt=0&rs=1&uid=&ori=pcw&ps=0&tm=1561107043991&qd_v=1&k_uid=37972322d2d359b7f89e5f7a8f7905fd&pt=0&d=0&s=&lid=&cf=&ct=&authKey=49d229f9027c7ab3d03ddb2dea33525f&k_tag=1&ost=0&ppt=0&dfp=a0e16d8c84067e43818b5c6c647535c27975284b52daecec49981cd0a49abb9c00&locale=zh_cn&prio=%7B%22ff%22%3A%22f4v%22%2C%22code%22%3A2%7D&pck=&k_err_retries=0&k_ft1=143486267424772&k_ft4=4&k_ft5=1&bop=%7B%22version%22%3A%2210.0%22%2C%22dfp%22%3A%22a0e16d8c84067e43818b5c6c647535c27975284b52daecec49981cd0a49abb9c00%22%7D&callback=Qb536b2f991098f88111e148c41339e43&ut=0&vf=eb0ed1f447a8bced48155161781274dd"
rs = requests.get(url)
print(rs.text)
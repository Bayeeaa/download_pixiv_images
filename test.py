import requests
url = "https://api.bbmang.me/ranks?page=1&date=2023-09-07&mode=day&pageSize=30"
response = requests.get(url)
img_url = "https://acgpic.net/c/540x540_70/img-master"+response.json()["data"][0]['imageUrls'][0]['original'][32:-4]+"_master1200.jpg"
img = requests.get(img_url)
with open("./top1.jpg","wb") as f:
    f.write(img.content)



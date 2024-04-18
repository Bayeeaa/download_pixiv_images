import requests
import os
import datetime

day = datetime.date.today()
api_day = day-datetime.timedelta(days=3)

url = "https://api.bbmang.me/ranks?page=1&date="+str(api_day)+"&mode=day&pageSize=302"
response = requests.get(url)



path = 'C:/Users/yyn19/Desktop/code/download_imges/'+api_day  #为linux写法，方便以字符串方式拼接，参考的方法https://blog.csdn.net/weixin_45690176/article/details/106442608?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522169417769716800186570018%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=169417769716800186570018&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-106442608-null-null.142^v93^chatsearchT3_1&utm_term=SyntaxError%3A%20%28unicode%20error%29%20unicodeescape%20codec%20cant%20decode%20bytes%20in%20position%202-3%3A%20truncated%20%5CUXXXXXXXX%20escape&spm=1018.2226.3001.4187
if(os.path.exists(path)==False):  #判断是否存在该文件夹
    os.mkdir(path)  #创建该文件夹

for i in range(10):
    img_url = "https://acgpic.net/c/540x540_70/img-master"+response.json()["data"][i]['imageUrls'][0]['original'][32:-4]+"_master1200.jpg"  #注意json的使用，以及图片url的获取方法(拼接)
    img = requests.get(img_url)
    with open(path+"/top"+str(i+1)+".jpg","wb") as f:
        f.write(img.content)
    print("正在保存top"+str(i+1)+"中...")





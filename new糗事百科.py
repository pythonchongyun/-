import requests
from lxml import etree

url = requests.get("https://www.qiushibaike.com/text/")

r = etree.HTML(url.text)
userNames = r.xpath('//div[@class="author clearfix"]/a/h2/text()')
comments = r.xpath('//div[@class="content"]/span/text()')
userNama1 = []
for userName in userNames:
    userNama1.append(userName)
comment1 = []
for comment in comments:
    comment1.append(comment)
for i in range(len(userNama1)):
    print("%s:%s" % (userNama1[i], comment1[i]))



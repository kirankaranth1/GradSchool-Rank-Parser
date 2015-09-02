from __future__ import print_function
import re
import requests
from lxml import html
from StringIO import StringIO
import sys
import os
import json
import math

f=open("GradSchoolrankings.csv",'w')
for i in range(1,6):
    url="http://grad-schools.usnews.rankingsandreviews.com/best-graduate-schools/top-science-schools/computer-science-rankings/page+"+str(i)

    while True:
        try:
            page = requests.get(url)
        except requests.ConnectionError:
            continue
        break
    tree = html.parse(StringIO(page.text)).getroot()
    print("Parsing page "+str(i))
    for j in range(1,27):
        if j==4:
            continue
        univ_name_xpath=".//*[@id='article']/table/tbody/tr["+str(j)+"]/td[2]/a"
        univ_rank_xpath=".//*[@id='article']/table/tbody/tr["+str(j)+"]/td[1]/div/span"
        univ_rating_xpath=".//*[@id='article']/table/tbody/tr["+str(j)+"]/td[3]"
        #print(univ_name_xpath)
        #print(tree.xpath(univ_name_xpath)[0].text)
        print("Parsing line "+str(j))
        name=tree.xpath(univ_name_xpath)[0].text.encode('utf-8').strip(",")
        #rank=int(re.findall('\d+', str(tree.xpath(univ_rank_xpath)[0].text)))
        #rank=tree.xpath(univ_rank_xpath)[0].text
        rating=str(tree.xpath(univ_rating_xpath)[0].text).strip()
        
        print(name+","+rating,file=f)
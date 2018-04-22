import itchat
import numpy as np
import pandas as pd
from collections import defaultdict
import re
import jieba
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image
itchat.login()
friends = itchat.get_friends(update=True)
NickName = friends[0].NickName #获取自己的昵称
os.mkdir(NickName) #为自己创建一个文件夹

file = '/%s' %NickName #刚刚创建的那个文件夹的相对路径
cp = os.getcwd() #当前路径
path = os.path.join(cp+file) #刚刚创建的那个文件夹的绝对路径
os.chdir(path) #切换路径
number_of_friends = len(friends)
df_friends = pd.DataFrame(friends)
def get_count(Sequence):

    counts = defaultdict(int) #初始化一个字典

    for x in Sex:
        counts[x] += 1

    return counts
Sex = df_friends.Sex
Sex_count = get_count(Sex )
Sex_count = Sex.value_counts() #defaultdict(int, {0: 31, 1: 292, 2: 245})
Sex_count.plot(kind = 'bar')
Province = df_friends.Province

Province_count = Province.value_counts()

Province_count = Province_count[Province_count.index!=''] #有一些好友地理信息为空，过
City = df_friends.City #[(df_friends.Province=='北京') | (df_friends.Province=='四川')]

City_count = City.value_counts()

City_count = City_count[City_count.index!='']
file_name_all = NickName+'_basic_inf.txt'

write_file = open(file_name_all,'w')

write_file.write('你共有%d个好友,其中有%d个男生，%d个女生，%d未显示性别。\n\n' %(number_of_friends, Sex_count[1], Sex_count[2], Sex_count[0])+

                 '你的朋友主要来自省份：%s(%d)、%s(%d)、%s(%d)、%s(%d)和%s(%d)。\n\n' %(Province_count.index[0],Province_count[0],Province_count.index[1],Province_count[1],Province_count.index[2],Province_count[2],Province_count.index[3],Province_count[3],Province_count.index[4],Province_count[4])+
                 '主要来自这些城市：%s(%d)、%s(%d)、%s(%d)、%s(%d)、%s(%d)、%s(%d)、%s(%d)、%s(%d)、%s(%d)、%s(%d)和%s(%d)。'%(City_count.index[0],City_count[0],City_count.index[1],City_count[1],City_count.index[2],City_count[2],City_count.index[3],City_count[3],City_count.index[4],City_count[4],City_count.index[5],City_count[5],City_count.index[6],City_count[6],City_count.index[7],City_count[7],City_count.index[8],City_count[8],City_count.index[9],City_count[9],City_count.index[10],City_count[10]))

write_file.close()
Signatures = df_friends.Signature

regex1 = re.compile('<span.*?</span>') #匹配表情

regex2 = re.compile('\s{2,}')#匹配两个以上占位符。

Signatures = [regex2.sub(' ',regex1.sub('',signature,re.S)) for signature in Signatures] #用一个空格替换表情和多个空格。

Signatures = [signature for signature in Signatures if len(signature)>0] #去除
text = ' '.join(Signatures)

file_name = NickName+'_wechat_signatures.txt'

with open(file_name,'w',encoding='utf-8') as f:
    f.write(text)
    f.close()

wordlist = jieba.cut(text, cut_all=True)

word_space_split = ' '.join(wordlist)

coloring = np.array(Image.open("/Users/dream/Documents/GitHub/machinelearning/tensorflow_tutorial/Crawler-of-LinkedIn-master/wechat.png")) #词云的背景和颜色。这张图片在本地。

my_wordcloud = WordCloud(background_color="white", max_words=2000,
                         mask=coloring, max_font_size=60, random_state=42, scale=2,
                         font_path="/Users/dream/Documents/GitHub/machinelearning/tensorflow_tutorial/Crawler-of-LinkedIn-master/SourceHanSerifK-Light.otf").generate(word_space_split) #生成词云。font_path="C:\Windows\Fonts\msyhl.ttc"指定字体，有些字不能解析中文，这种情况下会出现乱码。


file_name_p = NickName+'.jpg'

my_wordcloud.to_file(file_name_p) #保存图片
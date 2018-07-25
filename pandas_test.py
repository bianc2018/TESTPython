#-* -coding:GBK -* -
#中文注释模板
import os
import pandas as pd
import requests
import seaborn as sns
import matplotlib.pyplot as plt 
from matplotlib.font_manager import FontProperties
#import statsmodels.api 
try:
    PATH = r'./'
    #r = requests.get('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
    #with open(PATH+'iris.data','w') as f:
    #    f.write(r.text)
    #os.chdir(PATH)
    df  = pd.read_csv(PATH+'iris.data',names = ['花萼长度','花萼宽度','花瓣长度','花瓣宽度','类别'])
    print(df.head())
    #print(df['sepal length'])
    #print(df.ix[:3,[x for x in df.columns if 'class' in x]])
    #print(df['class'].unique())
    #print(df[df['class']=='Iris-virginica'])
    #print(df.count())
    #print(df.describe(percentiles=[.20,.40,.80,.90,.95]))
    #print(df.corr())
#    plt.style.use("ggplot")
    #中文字体
    myfont=FontProperties(fname=r'C:\Windows\Fonts\simhei.ttf',size=14)
    sns.set(font=myfont.get_name())
    #g= sns.pairplot(df,hue="类别")
    #plt.show()
    #画散点图
    fig,ax = plt.subplots(figsize=(7,7))
    ax.scatter(df['花萼宽度'][:50],df['花萼长度'][:50])
    ax.set_ylabel("花萼长度")
    ax.set_xlabel("花萼宽度")
    ax.set_title('花萼（长*宽）',fontsize=14,y=1.02)
    plt.show()
except Exception as e:
    print("ERROR:"+str(e))
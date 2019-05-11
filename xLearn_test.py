#import xlearn as xl
from sklearn.model_selection import train_test_split

import jieba
import pandas as pd
pd.set_option('display.max_columns',1000)
pd.set_option('display.width',1000)

pd.set_option('display.max_colwidth',1000)
#停用词
stopwords=pd.read_csv('stopwords.txt',index_col=False,quoting=3,
                      names=['stopword'],encoding='utf-8')

stopwords=stopwords['stopword'].values
print(stopwords)

#加载语料
laogong_df=pd.read_csv('beilaogongda.csv',sep=',',encoding='utf-8')
laopo_df=pd.read_csv('beilaopoda.csv',sep=',',encoding='utf-8')
erzi_df=pd.read_csv('beierzida.csv',sep=',',encoding='utf-8')
nver_df=pd.read_csv('beinverda.csv',sep=',',encoding='utf-8')

#删除语料的nan行
laogong_df.dropna(inplace=True)
laopo_df.dropna(inplace=True)
erzi_df.dropna(inplace=True)
nver_df.dropna(inplace=True)

#转换
laogong=laogong_df.segment.values.tolist()
laopo=laopo_df.segment.values.tolist()
erzi=erzi_df.segment.values.tolist()
nver=nver_df.segment.values.tolist()





















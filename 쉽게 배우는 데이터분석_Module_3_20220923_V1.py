#!/usr/bin/env python
# coding: utf-8

# # 5.데이터 파악하기 

# ## 5-1 데이터를 파악할때 사용하는 명령어 다섯가지는 무엇인가요?

# In[2]:


command = {'함수': ['head()', 'tail()', 'shape', 'info()', 'describe()'],
            '기능': ['앞부분 출력', '뒷부분 출력', '행, 열개수 출력', '변수 속성 출력', '요약통계량 출력']}
import pandas as pd

df = pd.DataFrame(command)
df


# ### 5-1-1 외부데이터를 활용하여 명령어 다섯가지 실습하기 

# In[3]:


# exam.csv 로드

exam = pd.read_csv('data/exam.csv')


# In[4]:


exam.head()


# In[5]:


exam.tail()


# In[6]:


exam.shape

# shpae은 함수가 아니라 데이터 프레임이 가지고 있는 하나의 속성이다. (Attribute)
# 이 경우 parenthesis를 사용하지 않는다.


# In[8]:


exam.info()

# int64의 64는 변수가 64비틀 되어 있다는 의미 1비트는 2개의 값을 표현 할수 있으므로 2^64개의 정수를 표현할수 있다.


# In[9]:


exam.describe()


# ## 5-1-2 외부데이터를 활용하여 명령어 다섯가지 실습하기_MPG

# * mpg data set는 mile per gallon, 미국 환경 보호국에서 공개한 데이터로 1999-2008년 미국에서 출시된자동차 234종의 정보를 담고 있습니다. 

# In[12]:


mpg = pd.read_csv('data/mpg.csv')
mpg.head(3)


# In[13]:


mpg.tail(3)


# In[14]:


mpg.shape


# In[15]:


mpg.info()


# In[16]:


mpg_col = {'변수명': ['manufacturere', 'model', 'disp', 'year', 'cy', 'trans', 'drv', 'cty', 'hwy', 'fl', 'category'],
            '내용' : ['제조회사', '모델명', '배기량(displacement)', '생산연도', '실린더갯수(cylinders)','변속기종류(transmission)',
                   '구동방식(drive wheell)', '도시연비(city)', '고속도로 연비(highway)', '연료 종류(fule)', '자동차종류']}
mpg_col= pd.DataFrame(mpg_col)
mpg_col


# In[17]:


mpg.describe()


# ### 문자로 된 변수의 요약 통계량 함께 출력하려면?
# * describe(include = 'all') 
# 

# In[18]:


mpg.describe(include='all')


# In[19]:


# character variable statistics 

cvs = {'outcome' : ['count', 'unique', 'top', 'freq'],
          'statistics' : ['빈도', '고유값 빈도', '최빈값', '최빈값 빈도'],
      'describtion' : ['값의개수', '중복을 제거한 범주의 개수', '개수가 가장 많은 값', '개수가 가장 많은 값의 개수']}
cvs= pd.DataFrame(cvs)
cvs


# In[21]:


mpg.describe(include ='all')['manufacturer']


# * 15개의 변수가 있다.
# * 가장 많이 생산한 제조자는 dodge이다
# * dodge는 37종을 생산했다. 

#  ## 5-1-3 함수와 메서드 차이 알아보기 

# ### method와 function의 차이
# 
# * 기본적으로 method는 function의 하나의 종류입니다. 함수의 종류의 따라 입력방식이 다르다는것이 가장 중요한 포인트입니다.
# * 내장함수는 가장 기본적인 함수로 함수이름과 괄호를 입력하여 사용합니다. 
# * 패키지함수는 패키지 이름을 먼저 입력한 다음 점을 찍고 함수 이름과 괄호를 입력하여 사용합니다.
# * 메써드는 '변수가 지니고 있는 함수' 입니다. 변수명을 입력한 다음 점을 찍고 메서드 이름과 괄호를 입력하여 사용합니다. 

# ### 내장함수 

# In[24]:


mpg['displ'].sum()


# ### 패키지함수 

# In[25]:


df3= {'number' : [1,2,3]}
df3= pd.DataFrame(df3)
df3


# ### Method

# In[28]:


df = pd.read_csv('data/exam.csv')
df.head(3)
# .head 가 메써드의 한 예 변수마다 다른 메써드를 가지고 있다.


# In[29]:


var = [1,2,3]
var.head(3)


# In[30]:


# 위 같은경우  list는 해당 method을 가지고 있지 않아서 실행이 되지 않는다.


# In[32]:


print(type(df))
print(type(var))


# ## 5-2 변수명 바꾸기
# 

# In[33]:


df_raw = pd.DataFrame({'var1': [1,2,1],
                      'var2': [2, 3, 2]})
df_raw


# In[36]:


df_new = df_raw.copy()
df_new
# 복사본 만들기 원형에 변형을 가할때 카피를 해두자 


# In[38]:


df_new= df_new.rename(columns = {'var1':'v1',
                                'var2':'v2'})
df_new


# ## 5-2-2 변수명바꾸기_실습(mpg data)
# 

# In[39]:


mpg


# In[41]:


# hwy, cty -> highway, city로 바꾸기 

mpg2=mpg.copy()
mpg2=mpg2.rename(columns = {'hwy':'highway','cty':'city'})
mpg2


# # 5-3 파생변수 만들기 

# ## 1. 변수 조합해 파생변수 만들기 

# In[44]:


df = pd.DataFrame({'var1' : [4,3,8],
                   'var2' : [2, 6, 1]})
df
# var1+var2 더하여 var_sum이라는 파생변수를 만들어보자


# In[45]:


# 데이터 프레임명에 [] 을 붙여 새로 만들 변수명을 입력하고 = 로 계산 공식을 할당하는 형태로 코드를 작성하면된다.
df['var_sum'] = df['var1'] + df['var2']
df


# In[46]:


df['var_mean'] = (df['var1'] + df['var2'])/2 
df


# ## mpg 통합 연비 변수 만들기 

# In[48]:


mpg2['total'] = (mpg2['city'] + mpg2['highway']) / 2 
mpg2.head()


# In[50]:


# len 함수를 사용하여 평균 구하기
mpg2['total'] .sum() /len(mpg2)


# In[52]:


# mean 함수를 사용하여 평균 구하기
mpg2['total'].mean()


# ##  조건문을 활용해 파생변수 만들기 

# In[53]:


mpg2['total'].describe()


# In[55]:


mpg2['total'].plot.hist()
# 간단한 그래프의 경우  데이터프레임의 plot 을 사용해 볼수 있다.


# In[58]:


#Numpy 패키지의 where()을 사용하면 조건에 따라 서로 다른 값을 부여할 수 있다. 
import numpy as np
mpg2['test'] = np.where(mpg2['total'] >= 20, 'pass', 'fail')
mpg2.head(3)


# In[59]:


# 빈도표 만들기 스트링데이터의 값이 종류별로 몇개씩 있는지 알아보기 
mpg2['test'].value_counts()


# In[60]:


import seaborn as sns
sns.countplot(data=mpg2, x=mpg2['test'])


# In[63]:


# 막대 그래프로 표현하기
count_test= mpg2['test'].value_counts()
count_test.plot.bar(rot=0)


# ## 중첩조건문 활용하기 

# * mpg의 연비를 30이 넘으면 A 20-29 면 B  20미만이면 C로 분류하고 싶다.
# * 즉 이진분류가 아닌 다중분류로 바뀐다. 
# * 이때 np.where 안에 다시 np.where 을 사용해야한다. 

# In[64]:


mpg2['grade'] = np.where(mpg2['total'] >= 30, 'A',
                        np.where(mpg['total'] >= 20, 'B', 'C'))

mpg2.head(3)


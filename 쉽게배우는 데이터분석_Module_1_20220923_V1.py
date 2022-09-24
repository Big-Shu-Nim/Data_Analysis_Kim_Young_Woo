#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns


# # seaborn countplot 사용하기 

# In[ ]:





# In[4]:


var = ['a', 'a', 'c', 'd']
var


# In[5]:


sns.countplot(x= var)


# In[8]:


df = sns.load_dataset('titanic')
df


# In[9]:


sns.countplot(data = df, x= 'sex')


# In[13]:


sns.countplot(data = df, x = 'class') # x 축 class


# In[14]:


sns.countplot(data = df, x = 'class', hue = 'alive') # x축 class, alive별 표현


# In[15]:


sns.countplot(data = df, y = 'class', hue = 'alive') #y축 class, alive별 표현


# # 패키지, 모듈, 함수 
# 

# 	##module?
# 		어떤 패키지는 함수가 굉장히 많기 떄문에 비슷한 함수끼리 묶어 몇 개의 모듈로 나뉘어 있다.
# 		패키지라는 큰 꾸러비에 비슷한 함수들을 넣어둔 작은 꾸러미들을이라고 생각하면 편함
# 		 
# 			Moudle의 예 with sklearn
# 				metrics, tree, model_selection 등 여러 모듈이 존재함
# 				metrcis 모듈안에 머신러닝 모델의 예측을 측정할때 사용하는 accuracy_score()이 있음
# 				이를 사용하기 위해서는 먼저 Metrcis 모듈을 먼저  import해야 가능함

# In[20]:


import sklearn.metrics


# In[23]:


import sklearn.metrics.accuracy_score()


# In[25]:


from sklearn import metrics
metrics.accuracy_score()
# 모둘의 함수를 사용할 때  매번 패키지명을 입력하는게 번거롭다면 from 패키지명 import 모듈명으로 모듈을 로드하면 된다.
# 이경우 함수를 사용할때 모둘명.함수명()으로 호출이 가능하다


# In[29]:


from sklearn.metrics import accuracy_score
accuracy_score()
#모듈명을 입력하는 것도 번거롭다면 from 패키지명.모듈명 import 함수명으로 함수를 직접로드 하면된다.
# 이경우 함수명만 입력시 사용가능


# ## 패키지 설치하기 

# * Pydataset 패키지는 여러가지 데이터셋을 쉽게 불러 올수 있다. 

# In[30]:


pip install pydataset


# In[31]:


import pydataset


# In[32]:


pydataset.data()
# pydataset 에 등록되어 있는 데이터셋 목록 출력


# In[33]:


# mtcars 로드하여 데이터프레임에 넣기

df = pydataset.data('mtcars')
df


# In[34]:


df.info()


# In[ ]:





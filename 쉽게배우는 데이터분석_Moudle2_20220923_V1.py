#!/usr/bin/env python
# coding: utf-8

#  ## 1.데이터 프레임 만들기 

# In[1]:


import pandas as pd 


# In[3]:


df = pd.DataFrame( {'name' : ['김지훈', '이유진', '박동현', '김민지'],
                    'english' : [90, 80, 60, 70],
                     'math' : [50, 60, 100, 20]})
df

# pd.DataFrame을 통해 데이터프레임을 만든다. 주의사항은 각 첫글자가 대문자라는점 


#  왼쪽에 표시된 숫자는 각 행이 몇 번째 순서에 위치하는 나타낸 인덱스이며 0부터 시작한다.

# ## 2.데이터 프레임으로 분석하기 

# In[4]:


# 1. 데이터 프레임에서 특정 칼럼의 값들만 보고 싶을때? 여기서는 df의 english 칼럼의 값들만 보고싶다.
df['english']


# In[5]:


# 2.따로 추출한 변수(칼럼값)들의 합계를 구하고싶다면?
sum(df['english'])


# In[6]:


# 3.따로 추출한 변수(칼럼값)들의 산술평균을 구하고싶다면? 
  # 3-1 영어점수 평균을 구하시오
df['english'] \  # back slash , you can associate with the pipe in R
.sum() /4


# In[7]:


# 3-2 수학점수 평균을 구하시오

df['math'] .sum() / 4 


# In[10]:



df2 = pd.DataFrame( {'제품': ['사과', '딸기', '수박'],
                   '가격' : [1800, 1500, 300],
                   '판매량' : [24,38,13]} )
df2


# In[11]:


#데이터 프레임 생성시 주의사항
# 기본적으로 딕셔너리로 키값과 발류값을 지정하는것이다.
# string 값이 하나의 측정치로 들어갈경우 각각 quotation mark처리를 해야한다.


# ## 3.외부 데이터 이용하기 

# In[13]:


df_exam = pd.read_excel('data/excel_exam.xlsx')
df_exam
# 엑셀파일 불러오기
# 폴더안에 있을경우 \ 사용한다


# In[20]:


# 1.영어점수와 과학점수의 전체 평균을 구하세요
df_exam['english'] .sum() /20 


# In[22]:


df_exam['science'] .sum() /20 


# In[23]:


# 2.카운트를 직접하지 않고 함수를 통해서 구하기 
    # len() 함수는 값의 개수를 구하는 기능을 한다.
     # 데이트프레임을 입력하면 행의 개수를 출력한다. 


# In[31]:


# 2-1 변수의 값 개수 구하기 
x = [1,2,3,4,5]
print("what is in the variable x : ",x)
print('The number of observations in the variable x :',len(x))


# In[32]:


# 2-2 데이터프레임의 행 개수 구하기
df = pd.DataFrame({'a' : [1,2,3],
                  'b' : [4, 5, 6]})
df


# In[33]:


len(df)


# In[35]:


# 3 엑셀 파일의 첫 번째 행이 변수명이 아니라면?
# read_excel()의 경우 첫 번째 행을 변수명으로 인식함
# 따라서 만일 헤더가 없고 데이터가 바로 시작되는 경우 유실 될수가 있음
df_exam_novar = pd.read_excel('data/excel_exam_novar.xlsx')
df_exam_novar


# In[37]:


# 이 경우 파라미터 header = Non 을 입력하면 문제를해결 할 수 있다.

df_exam_novar = pd.read_excel('data/.xlsx', header=None)
df_exam_novar


# In[39]:


# 4엑셀 파일에 시트가 여러개 있을때 특정 시트의 데이터만 불러오려면?
    # sheet_name 시트이름 직접입력
    # sheet_name 몇번째 시트를 불러올지 숫자를 입력 
    # 세번째 시트를 불러오려면 sheet_name = 2 를 입력 파이썬에서는 숫자 0부터 시작하기 때문


# In[50]:


# 4-1 sheet2 시트의 데이터 불러오기
df_exam = pd. read_excel('data/중소기업_재무제표.xlsx', sheet_name = 'Sheet4')
# 세 번째 시트의 데이터 불러오기
df_exam = pd.read_excel('data/중소기업_재무제표.xlsx', sheet_name = 2)


# In[47]:


# CSV 파일
# 엑셀, R, SAS, SPSS에서 사용가능한 범용성떄문에 많은사람들이 사용하는 포맷


# In[51]:


df_csv_exam = pd.read_csv('data/exam.csv')
df_csv_exam


# In[52]:


# 4-2 데이터 프레임 CSV 파일로 저장하기 

df_midterm = pd. DataFrame( {'english' : [90, 80, 60, 70],
                            'math'     : [50, 60, 100, 20],
                            'nclass'   :   [1, 1, 2, 2]})
df_midterm


# In[54]:


df_midterm.to_csv("output_newdata.csv")


# In[56]:


# 기본값은 인덱스가 포함된다 인덱스 없이 하고싶다면

df_midterm.to_csv('output_newdata2.csv', index=False)


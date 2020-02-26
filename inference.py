#inference.py

#수정해야 할 사항 : 1. Chi-Squared test 내용 추가
#2.scipy module 말고 numpy를 사용하여 밑바닥에서 부터 구현하기.

import scipy as sc
from scipy import stats
import numpy as np
import pandas as pd
import random as rd

def print_result(t, p):
    judge=['\n[H1 is reject !!]', '\n[H0 is reject !!]'] ; indx=0
    if round(p, 2) > 0.05 : print(judge[indx], 'The value of t is %s'%(t))
    else : print(judge[indx+1], 'The value of t is %s'%(t))
    return 

def print_format_1samp(whether, p_value):
    print('\nAs result of the shapiro test...\nyou should use "%s" !!!'%(whether))
    print('The p-value is %s'%(p_value))
    return

def print_format_2samp(whether, p1, p2):
    print('\nAs result of the shapiro test...\nyou should use "%s" !!!'%(whether))
    print('\nThe p-value of Sample_1 is %s\nThe p-value of Sample_2 is %s'%(p1, p2))
    return

def one_sample_t(samp):
    popmean=resampling(samp)
    result=stats.ttest_1samp(samp, popmean) 
    print_result(str(result[0]), result[1])
    return

def two_sample_t(samp1, samp2):
    result=stats.ttest_ind(samp1, samp2)
    print_result(str(result[0]), result[1])
    return

def wilcoxon_test1(samp):
    result=stats.wilcoxon(samp) 
    print_result(str(result[0]), result[1])
    return

def wilcoxon_test2(samp1, samp2):
    result=stats.wilcoxon(samp1, samp2)
    print_result(str(result[0]), result[1])
    return    

def resampling(samp):
    result=[]
    for _ in range(5000):
        result.append(np.array([rd.choice(samp) for _ in range(len(samp))]).mean())
    return np.array(result).mean()
    
class infer:
    def __init__(self, file):
        self._file=file
        return

    def test(self): # 정규성 검사후에 이를 바탕으로 t-test, wilcox 각각의 함수 호출
        judge=int(input('>>How many variables you want (one sample or two sample) ? '))

        if judge==1: # one sample t-test
            self._v=input('>>Input the 1 Numerical variable : ')
            self._r=list(self._file[self._v])
            self._sr=sc.stats.shapiro(self._r)

            if round(self._sr[1], 2) >= 0.05 : # 정규분포인 경우
                print_format_1samp('One sample t-test', str(self._sr[1]))
                one_sample_t(self._r)       
            
            else : # 비정규분포인 경우 wilcox
                print_format_1samp('Wilcoxon rank sum test', str(self._sr[1]))
                wilcoxon_test1(self._r)
                
        elif judge==2: # two sample t-test
            self._v1, self._v2=input('>>Input the 2 Numerical variables : ').split()
            self._r1=list(self._file[self._v1]) ; self._r2=list(self._file[self._v2])
            self._sc1=sc.stats.shapiro(self._r1) ; self._sc2=sc.stats.shapiro(self._r2)

            # 두 개 sample 중 하나가 정규분포일 경우 -> two sample t-test
            if round(self._sc1[1], 2) >= 0.05 or round(self._sc2[1], 2) >= 0.05 :
                print_format_2samp('One sample t-test', str(self._sc1[1]), str(self._sc2[1]))
                two_sample_t(self._r1, self._r2)

            else : # 두 개 sample 모두 비정규분포인 경우 -> wilcox
                print_format_2samp('Wilcoxon rank sum test', str(self._sc1[1]), str(self._sc2[1]))
                wilcoxon_test2(self._r1, self._r2)
                
        return

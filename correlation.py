#correlation.py

#수정해야 할 사항 : 1. 상관계수를 구할 때, numpy의 method를 바로 이용하지 말고 pearson 상관계수를 구하는 과정을 밑바닥에서 구현

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def traditional_infer(r):
    
    if r<0:
        if r>=-0.2 : print('==> Result : (-)Low correlation.\n')
        elif r>=-0.5 : print('==> Result : (-)Middle correlation.\n')
        elif r>=-0.7 : print('==> Result : (-)High correlation.\n')
        elif r>=-1 : print('==> Result : (-)Very High correlation.\n')
        
    elif r>0:
        if r<=0.2 : print('==> Result : (+)Low correlation.\n')
        elif r<=0.5 : print('==> Result : (+)Middle correlation.\n')
        elif r<=0.7 : print('==> Result : (+)High correlation.\n')
        elif r<=1 : print('==> Result : (+)Very High correlation.\n')

    else :
        print('==> Result : No Correlation Statically!!\n')

    return

class cor:
    def __init__(self, file):
        self._file=file;
        return

    def get_coef(self):
        self._v1, self._v2=input(">>Input two variables : ").split()
        self._r1=np.array(self._file[self._v1])
        self._r2=np.array(self._file[self._v2])
        self._result=np.corrcoef(self._r1, self._r2)
        print('\n>>The value r is %.3f'%(self._result[0][1]))
        traditional_infer(round(self._result[0][1],5))
        return

    def show_scatter(self):
        plt.scatter(self._file[self._v1], self._file[self._v2])
        plt.title("Scatter plot")
        plt.show()
        return

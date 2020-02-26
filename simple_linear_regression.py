#simple_linear_regression.py

#수정해야 할 사항 : 1. multi linear regression 추가
# 2. scipy module말고 numpy를 이용하여 밑바다에서 부터 구현하기.

import scipy as sc
import pandas as pd
import matplotlib.pylab as plt
import numpy as np

class slr:
    
    def __init__(self, file):
        self._file=file
        return

    def get_results(self):
        self._v1, self._v2=input(">>Input two variables (inde-depen) : ").split()
        self._r1=np.array(self._file[self._v1])
        self._r2=np.array(self._file[self._v2])
        self._result=pd.Series(list(sc.stats.linregress(self._r1, self._r2)), index=['Slope', 'Intercept', 'Corelation Coefficent', 'p-value', 'Std of error'])
        print() ; print(self._result)
        return

    def show_regression_plot(self):
        self._ry=sc.polyval([self._result[0], self._result[1]], self._r1)
        plt.plot(self._r1, self._r2, 'k.')
        plt.plot(self._r1, self._ry, 'r.-')
        plt.title("Simple Linear Regression")
        plt.legend(['Original Data', 'Regression'])
        plt.show()
        return

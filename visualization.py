#visualization.py

#수정해야 할 사항 : 1. 

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import font_manager, rc

font_name=font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
rc('font', family=font_name)

def make_pie(data):
    v1=input(">>Input the variable : ")
    ti, ex, fig = input(">>Title/Explode([.., ..,])/Figsize((.., ..,)) : ").split('/')
    
    ex=list(map(float, ex.strip('[]').split(','))) ; fig=tuple(map(float, fig.strip('()').split(',')))

    temp=data[v1].dropna().value_counts()
    temp.plot.pie(explode=ex, labels=temp.index, autopct="%1.1f%%", figsize=fig)
    plt.title(ti) ; plt.show()
    return

def make_bar(data):
    v1=input(">>Input the variable : ")
    ti, st, ba = input(">>Title/Stack(T|F)/Barh(h|v) : ").split('/')
    
    if st=='T' : st=True
    elif st=='F' : st=False
    if ba=='v' : ba='bar'
    elif ba=='h' : ba='barh'

    data[v1].dropna().value_counts().plot(kind=ba, stacked=st)
    plt.title(ti) ; plt.show()
    return

def make_hist(data):
    v1=input(">>Input the variable : ")
    ti, fc, bi, nor = input(">>Title/Facecolor/Bins(num)/Normed(T|F) : ").split('/')
    
    if nor == 'T' : nor=True
    elif nor == 'F': nor=False
    
    plt.hist(data[v1].dropna(), facecolor=fc, bins=int(bi), normed=nor)
    plt.title(ti)
    plt.show()
    return

def line_plot(data): #line_plot 추가하기
    pass

class visual:
    
    def __init__(self, file):
        self._file=file
        return

    def get_graph(self):
       graph_menu=pd.Series(['Pie', 'Bar', 'Histogram'], index=[1,2,3])
       print() ; print(graph_menu)
       judge=int(input('\n>>Enter the number : '))

       if judge==1: make_pie(self._file)
       elif judge==2: make_bar(self._file)
       elif judge==3: make_hist(self._file)

       return

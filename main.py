#main.py

#수정해야 할 사항 : 1. pandas의 DataFrame의 다양한 method를 이용하여 titanic.csv data를 다룰 수 있도록 code를 추가한다. 

import pandas as pd
from Correlation import cor
from simple_linear_regression import slr
from inference import infer
from visualization import visual

def get_file():
    file_name=input(">>Input File Name : ")
    return pd.read_csv(file_name, sep=',', encoding='euc_kr')

def select_menu():
    menu=pd.Series(['Visualization', 'Inference', 'Correlation', 'Simple Linear Regression'], index=['(1)', '(2)', '(3)', '(4)'])
    print() ; print(menu)
    choice=int(input('\n>>Pick the menu : '))
    return choice

if __name__=="__main__":

    while True:
        try :
            file=get_file()
        except :
            print("\nError) Check the file name or location !!\n")
            continue
        else :
            break

    while True:

        choice=select_menu()

        if choice==1:
            obj=visual(file) ; obj.get_graph()
            break

        elif choice==2:
            obj=infer(file) ; obj.test()
            break

        elif choice==3:
            obj=cor(file) ; obj.get_coef() ; obj.show_scatter()
            break

        elif choice==4:
            obj=slr(file) ; obj.get_results() ; obj.show_regression_plot()
            break

        else :
            print('\nError) Wrong Number !! Input the right Number !!\n')
            continue

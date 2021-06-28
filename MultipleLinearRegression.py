import pandas as pd
import numpy as np
import math

def mean(data):
    data=data
    n=len(data)
    sum=0
    for i in range(0,n):
        sum=sum+data[i]
    mean= sum/n
    return mean

def Difference(a,b):
    a=a
    b=b
    n=len(a)
    c=[]
    for i in range(0,n):
        c.append(a[i]-b)
    return c

def Square(a):
    a=a
    n=len(a)
    sum_sqr=0
    for i in range(0,n):
        sum_sqr= sum_sqr+(a[i]*a[i])
    return sum_sqr

def multiply(a,b):
    a=a
    b=b
    n=len(a)
    sum_multiply=0
    for i in range(0,n):
        sum_multiply= sum_multiply+(a[i]*b[i])
    return sum_multiply

def r2_score(Y_mean,Y_predict, c):
    Y_mean=Y_mean
    Y_predict=np.array(Y_predict)
    c=c
    sum=0
    n=len(Y_predict)
    for i in range(0,n):
        sum=sum+((Y_predict[i]-Y_mean)*(Y_predict[i]-Y_mean))
    r2_score=sum/c
    print("The R2 Score is:"+str(r2_score))

    
    
def LinearRegression(X1_test,X2_test,Y_test):
    X1=X1_test
    X2=X2_test
    Y=Y_test
    X1_mean=mean(X1)
    X2_mean=mean(X2)
    Y_mean=mean(Y)
    X1_mean_Difference= Difference(X1,X1_mean)
    X2_mean_Difference= Difference(X2,X2_mean)
    Y_mean_Difference= Difference(Y,Y_mean)
    X1_mean_Difference_Square= Square(X1_mean_Difference)
    X2_mean_Difference_Square= Square(X2_mean_Difference)
    Y_mean_Difference_Square= Square(Y_mean_Difference)
    Y_mean_Difference_multiply_X1_mean_Difference= multiply(Y_mean_Difference,X1_mean_Difference)
    Y_mean_Difference_multiply_X2_mean_Difference= multiply(Y_mean_Difference,X2_mean_Difference)
    #print(Y_mean_Difference_multiply_X_mean_Difference)
    teta_1= (Y_mean_Difference_multiply_X1_mean_Difference/X1_mean_Difference_Square)
    teta_2= (Y_mean_Difference_multiply_X2_mean_Difference/X2_mean_Difference_Square)
    teta_0= Y_mean - (teta_1*X1_mean)- (teta_2*X2_mean)
    return [ teta_1,teta_2,teta_0,Y_mean,Y_mean_Difference_Square  ]
    

def predict(X1_predict,X2_predict):
    url= "./Real_Estate_2.csv"
    df = pd.read_csv(url)
    Linear_Reg= LinearRegression(df['area'],df['area_age'],df['price'])
    teta_0= Linear_Reg[2]
    teta_1= Linear_Reg[0]
    teta_2= Linear_Reg[1]
    Y_mean_Difference_Square= Linear_Reg[4]
    Y_mean= Linear_Reg[3]
    Y_predict=[]
    X1_predict=np.array(X1_predict)
    X2_predict=np.array(X2_predict)
    if len(X1_predict)>2 and len(X1_predict)>2:
        for i in range(0,len(X1_predict)):
            Y_predict.append(math.floor(teta_0+(teta_1*X1_predict[i])+(teta_2*X2_predict[i])))
        r2_score(Y_mean,Y_predict, Y_mean_Difference_Square)
        return Y_predict
    else:
        Y_prediction= math.floor(teta_0+(teta_1*X1_predict)+(teta_2*X2_predict))
        return Y_prediction

url= "./Real_Estate_2.csv"
df = pd.read_csv(url)
x1= [3422]
x2= [9]
predict2=predict(x1,x2)
print("Th price of area whihc is "+str(x1[0])+" sqr feet and "+str(x2[0])+" years old is:"+str(predict2))
predict=predict(df['area'],df['area_age'])
#print("The R2 Score or accuracy of prediction is:"+str(r2_score))
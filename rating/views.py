from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import pandas as pd
import numpy as np
import joblib

from rating.models import Rating

forest=joblib.load("rating/forest_financial A")


def rating_view(request):
    if request.method =='GET':
        
        return render(request,'rating/rating.html')
    elif request.method =='POST':
        Ltd = request.POST['Ltd']
        EBITDA = request.POST['EBITDA']
        Cag = request.POST['Cag']
        Ibd = request.POST['Ibd']
        Alr = request.POST['Alr']
        Ncf = request.POST['Ncf']
        Cat = request.POST['Cat']
        OP = request.POST['OP']
        Pol = request.POST['Pol']
        It = request.POST['It']
        Se = request.POST['Se']
        Roe = request.POST['Roe']

    
    

    x=[Ltd,EBITDA,Cag,Pol,Roe,Se,OP,It,Cat,Ncf,Ibd,Alr]
    x=np.matrix(x)
   
    y_pred=forest.predict(x)
    y=round(y_pred[0])
    if y==9: y='AAA.'
    if y==8: y='AA.'
    if y==7: y='A.'
    if y==6: y='BBB.'
    if y==5: y='BB.'
    if y==4: y='B.'
    if y==3: y='CCC.'
    if y==2: y='CC.'
    if y==1: y='C.'
    username = request.session['username']
    rating = Rating.objects.create(Ltd=Ltd,EBITDA=EBITDA,Cag=Cag,Pol=Pol,Roe=Roe,Se=Se,OP=OP,It=It,Cat=Cat,Ncf=Ncf,Ibd=Ibd,Alr=Alr,result=y,username=username)
   
    
    return render(request,'rating/rating.html',locals())
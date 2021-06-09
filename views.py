from django.shortcuts import render
from . import ml_predict
def home(request):
    return render(request,'index.html')

def result(request):
    battery_power=int(request.GET['battery_power'])
    blue=int(request.GET['blue'])
    dual_sim=int(request.GET['dual_sim'])
    four_g=int(request.GET['four_g'])
    int_memory=int(request.GET['int_memory'])
    mobile_wt=int(request.GET['mobile_wt'])
    three_g=int(request.GET['three_g'])
    touch_screen=int(request.GET['touch_screen'])
    wifi=int(request.GET['wifi'])


    prediction=ml_predict.prediction_model(battery_power,blue,dual_sim,four_g,int_memory,mobile_wt,three_g,touch_screen,wifi)

    return render(request,'result.html',{'predict':prediction})
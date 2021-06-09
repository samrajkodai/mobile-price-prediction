import pickle
def prediction_model(battery_power,blue,dual_sim,four_g,int_memory,mobile_wt,three_g,touch_screen,wifi):

    x=[[battery_power,blue,dual_sim, four_g,int_memory,mobile_wt,three_g,touch_screen,wifi]]
    classifier=pickle.load(open('classifier.pkl','rb'))
    prediction=classifier.predict(x)
    return prediction
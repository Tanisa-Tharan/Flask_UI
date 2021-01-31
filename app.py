# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 23:55:37 2021

@author: hp
"""


from flask import Flask,render_template,url_for,request
import pandas as pd 
import csv
import datetime
import dateutil.parser
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/data',methods=['POST'])
def data():
    if request.method == 'POST':
        f=request.form['csvfile']
        data=[]
        df = pd.read_csv("data.csv")
        max_date=max(df['DATE'])
        print(max_date)
        with open(f) as file:
            
            csvfile=csv.reader(file)
            
            #data['Date'] = pd.to_datetime(data['Date'])
            for row in csvfile:
                #print(row[0])
                if(row[0]!="DATE_TIME"):
                    if(max_date==row[8] and request.form['message3']==row[2]):
                        data.append(row)
                        
        data=pd.DataFrame(data)
        return render_template('data.html',data=data.to_html())
        
@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        my_prediction=[]
        with open('data.csv') as file:
            csvfile=csv.reader(file)
            for row in csvfile:
                #print(row[0])
                if row[2]==request.form['message']  :
                    date=row[1].strip(" ")[:10]
                    print("Date "+date)
                    if(date==request.form['message2']):
                        my_prediction.append(row[7])
        my_prediction=pd.DataFrame(my_prediction)
        return render_template('data2.html',prediction = my_prediction.to_html())       

@app.route('/mean',methods=['POST'])
def mean():
    if request.method == 'POST':
        my_prediction=[]
        with open('data.csv') as file:
            csvfile=csv.reader(file)
            for row in csvfile:
                print(type(row[4]))
                print(type(row[5]))
                try:
                    a=abs(int(float(row[5]))-int(float(row[4])))
                    my_prediction.append(a)
                except :
                    print("Error")
        
                
        my_prediction=pd.DataFrame(my_prediction)
        return render_template('data3.html',prediction = my_prediction.to_html())            
        

if __name__ == '__main__':
	app.run(debug=True)
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:44:47 2020

"""
from flask import Flask, request, render_template

app = Flask(__name__)

import sqlite3  
import logging

#initialize logging

LOG_FILE_NAME = 'AppLog1.txt'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s  %(name)-12s  %(levelname)-8s: %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    filename=LOG_FILE_NAME, 
                    filemode='w') 


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/regis',methods=['POST', 'GET'])
def complaintRegis():
    
    dt=[]
    status = " "
    if request.method == "POST":
        
        inv = request.form["invref"]
        dt.append(request.form["name"])
        dt.append(request.form["invref"])
        dt.append(request.form["invdate"])
        dt.append(request.form["pname"])
        dt.append(request.form["nature"])
        
        db_name='ABC_complaints.db'
        conn = sqlite3.connect(db_name)
        logging.info('Connected to '+db_name)
        c = conn.cursor()
        c.execute("INSERT INTO complaints (name,invref,invdate,pname,nature) VALUES (?,?,?,?,?)",dt) 
        #complaint registration number is generated automatically using autoincrement.            
        conn.commit()
        c.execute("select cref from complaints where invref = '%s'" % inv)  
        s=c.fetchall()
        for row in s:
            cmref=row[0]
            
        logging.info(type(cmref))                
        logging.info('Inserted values to '+db_name)
        status = "Complaint registered successfully and your complaint registration number is "+ str(cmref)
        
           
        
    return render_template("complaint_regis.html",complaint_success=status)

@app.route('/status',methods=['POST', 'GET'])
def complaintRetrieve():
    

    status = " "
    if request.method == "POST":
        
        cmp = request.form["cref"]
        db_name='ABC_complaints.db'
        conn = sqlite3.connect(db_name)
        logging.info('Connected to '+db_name)
        c = conn.cursor()
        t = (cmp,)
        c.execute("select status from complaints where cref = ?", t)  
        s=c.fetchall()
        if len(s) != 0:
            for row in s:
                st=row[0]
              
            if not st:
                status = "Complaint status for registration number "+cmp+ " is yet to be updated."
            
            else:
                logging.info(st +' retrieved from '+db_name) 
                status = "Complaint status for registration number "+cmp+ " : "+ st
        else:
            status = cmp+" is an invalid complaint registration number."
           
        
    return render_template("complaint_retrieve.html", complaint_status=status)



if __name__ == '__main__':
    app.run()
    
    
    
    
    
    
    
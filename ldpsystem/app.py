from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session,flash
import numpy as np
import pickle
from flask_mysqldb import MySQL
import mysql.connector
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib

import mysql.connector


app = Flask(__name__) 

model = pickle.load(open('Liver2.pkl', 'rb'))

# secret key for extra protection
app.secret_key = 'ldp'
# Enter your database connection details below
mdb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="abc_hospital"
)

# Intialize MySQL
mysql = MySQL(app) 





@app.route('/')
@app.route("/login", methods=['POST', 'GET'])
def login():
     # Output a message if something goes wrong...
    msg = ''
    
    # Check if "email" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        # Get the form data
        email = request.form['email']
        password = request.form['password']

        #checking the user in the database
        def check_user(email, password):
          with mdb.cursor(dictionary=True) as cursor:
           query = "SELECT * FROM users WHERE email = %s AND password = %s"
           cursor.execute(query, (email, password))
           user = cursor.fetchone()

           return user

        # Check if a user with the provided email and password exists
        user = check_user(email, password)

        if user:
            
            with mdb.cursor(dictionary=True) as cursor:
               query = "SELECT * FROM users WHERE email = %s AND password = %s"
               cursor.execute(query, (email, password))
               user = cursor.fetchone()
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = user['id']
            #session['email'] = user['email']
            # Redirect to home page
            return redirect('/admin')
        else:
            # Account doesn't exist or email/password is incorrect
            msg = 'Incorrect email or password try again!'

    # Show the login form with message (if any)
    return render_template('login.html', msg=msg)


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        print(request.form)
        # Get the form data
        Full_names = request.form.get("fname")
        Username=request.form.get("username")
        Email = request.form.get("email")        
        Password = request.form.get("password")

        # Ensure no required field is empty
        if not (Full_names and Username and Email and Password):
            # Handle missing form data error
            return "Missing form data. Please fill in all fields."

        else:
        # Create a cursor object to execute SQL queries
         cursor = mdb.cursor()

        # Insert the new user into the employees table
        query = "INSERT INTO users (Full_names, Username, email, Password) VALUES (%s, %s, %s, %s)"
        values = (Full_names, Username, Email, Password)
        cursor.execute(query, values)

        # Commit the changes to the database
        mdb.commit()

        flash("User registered Succeesfully!")

        # Close the cursor
        cursor.close()

        return redirect("/signup")
    
    return render_template("signup.html") 

@app.route('/admin_sign', methods=['POST', 'GET'])
def admin_sign():
    if request.method == "POST":
        print(request.form)
        # Get the form data
        Full_names = request.form.get("fname")
        Username=request.form.get("username")
        Email = request.form.get("email")        
        Password = request.form.get("password")

        # Ensure no required field is empty
        if not (Full_names and Username and Email and Password):
            # Handle missing form data error
            return "Missing form data. Please fill in all fields."

        else:
        # Create a cursor object to execute SQL queries
         cursor = mdb.cursor()

        # Insert the new user into the employees table
        query = "INSERT INTO admin (Full_names, Username, email, Password) VALUES (%s, %s, %s, %s)"
        values = (Full_names, Username, Email, Password)
        cursor.execute(query, values)

        # Commit the changes to the database
        mdb.commit()

        flash("User registered Succeesfully!")

        # Close the cursor
        cursor.close()

        return redirect("/login")
    
    return render_template("admin_sign.html") 

@app.route("/admin_login", methods=['POST', 'GET'])
def admin_login():
     # Output a message if something goes wrong...
    msg = ''
    
    # Check if "email" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        # Get the form data
        email = request.form['email']
        password = request.form['password']

        #checking the user in the database
        def check_user(email, password):
          with mdb.cursor(dictionary=True) as cursor:
           query = "SELECT * FROM admin WHERE email = %s AND password = %s"
           cursor.execute(query, (email, password))
           user = cursor.fetchone()

           return user

        # Check if a user with the provided email and password exists
        user = check_user(email, password)

        if user:
            
            with mdb.cursor(dictionary=True) as cursor:
               query = "SELECT * FROM admin WHERE email = %s AND password = %s"
               cursor.execute(query, (email, password))
               user = cursor.fetchone()
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = user['id']
            #session['email'] = user['email']
            # Redirect to signup page
            return redirect('/adminhome')
        else:
            # Account doesn't exist or email/password is incorrect
            msg = 'Incorrect email or password try again!'

    # Show the login form with message (if any)
    return render_template('admin_login.html', msg=msg)



   
@app.route("/registration", methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        print(request.form)
        # Get the form data
        fullName = request.form['fullName']
        gender = request.form['gender']
        dob = datetime.strptime(request.form['dob'], '%Y-%m-%d').date()
        age = int(request.form['age'])
        address = request.form['address']
        Phonenumber = request.form['phonenumber']
        nextofkin = request.form['nextofkin']
        relationship = request.form['relationship']
        kinnumber = request.form['kinnumber']
        insurance = request.form['insurance']
        insurancenumber = request.form['insurancenumber']
        # Ensure no required field is empty
        if not (fullName and gender and dob and age and address and Phonenumber and nextofkin and relationship and kinnumber and insurance and insurancenumber):
            # Handle missing form data error
            return "Missing form data. Please fill in all fields."

        cursor = mdb.cursor()

        # Insert the new farmer into the farmer table
        query="INSERT INTO patients (Full_names, Gender, DOB, Age, Address, Phone_number, Next_of_kin, Relationship, Contact, Insurance_scheme, Insurance_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values=(fullName, gender, dob, age, address, Phonenumber, nextofkin, relationship, kinnumber, insurance, insurancenumber)
        cursor.execute(query,values)

        # Commit the changes to the database
        mdb.commit()

        # Close the cursor
        cursor.close()

        return redirect("/registration")
    
    return render_template("registration.html")

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')

@app.route('/ldpatients', methods=['POST', 'GET'])
def ldpatients():
    if request.method == "POST":
        print(request.form)
        # Get the form data
        Full_names = request.form['Full_names']        
        age = int(request.form['age'])
        Gender = request.form['Gender']
        Address = request.form['Address']
        Phone_number = request.form['Phone_number']
        status = request.form['status']
        # Ensure no required field is empty
        if not (Full_names and age and Gender and Address and Phone_number and status):
            # Handle missing form data error
            return "Missing form data. Please fill in all fields."

        cursor = mdb.cursor()

        # Insert the new farmer into the farmer table
        query="INSERT INTO ld_patients (Full_names,Age,Gender, Address, Contact, Status) VALUES (%s, %s, %s, %s, %s, %s)"
        values=(Full_names, age, Gender, Address, Phone_number, status)
        cursor.execute(query,values)

        # Commit the changes to the database
        mdb.commit()

        # Close the cursor
        cursor.close()

        return redirect("/ldpatients")
    
    
    return render_template('ldpatients.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/admin', methods=['POST', 'GET'] )
def admin():
    return render_template("admin.html")

@app.route("/predict_search", methods=["GET"])
def predict_search():
    search_id = request.args.get("search_id")

    print("Searching for PatientID:", search_id)

    try:
        cursor = mdb.cursor()

        query = "SELECT id,Gender, age FROM patients WHERE id= %s"
        cursor.execute(query, (search_id,))
        patients= cursor.fetchone()
        print("Executed Query:", query)
        print("Result from Database:", patients)
        
        cursor.close()

        if patients:
            (id, Gender,age
            ) = patients
            message = ""
        else:
            (id,Gender,age
            ) = [""] * 3
            message = "Patient not found"

    except Exception as e:
    
        print(f"Error: {e}")
        id,Gender,	age, message = [""] * 3
        message = "An error occurred while processing your request."

    return render_template(
        "index.html",search_id=id,
       gender=Gender, age=age, message=message
    ) 




#Search the patient before recording after disease prediction
@app.route("/update_search", methods=["GET"])
def update_search():
    search_id = request.args.get("search_id")

    print("Searching for FarmerID:", search_id)

    try:
        cursor = mdb.cursor()

        query = "SELECT id, Full_names, Gender, age, Address, Phone_number FROM patients WHERE id= %s"
        cursor.execute(query, (search_id,))
        patients= cursor.fetchone()
        print("Executed Query:", query)
        print("Result from Database:", patients)
        
        cursor.close()

        if patients:
            ( id, Full_names, Gender,age, Address, Phone_number
            ) = patients
            message = ""
        else:
            (id, Full_names, Gender, age, Address, Phone_number
            ) = [""] * 7
            message = "Patient not found"

    except Exception as e:
    
        print(f"Error: {e}")
        id, Full_names, Gender,	age, Address, Phone_number, message = [""] * 7
        message = "An error occurred while processing your request."

    return render_template(
        "ldpatients.html",search_id=id,
        Full_names=Full_names, Gender=Gender, age=age, Address=Address, Phone_number=Phone_number, message=message
    ) 


#Save the patient's details after disease is detected
@app.route('/ldpredict', methods=['POST', 'GET'] )
def ldpredict():

    if request.method == "POST":
        print(request.form)
        # Get the form data
        fullName = request.form['fullName']
        age = int(request.form['age'])
        address = request.form['address']
        Phonenumber = request.form['phonenumber']
        
        # Ensure no required field is empty
        if not (fullName and age and address and Phonenumber):
            # Handle missing form data error
            return "Missing form data. Please fill in all fields."

        cursor = mdb.cursor()

        # Insert the new farmer into the farmer table
        query="INSERT INTO ld_patients (Full_names, Age, Address, Phone_number) VALUES (%s, %s, %s, %s)"
        values=(fullName, age, address, Phonenumber)
        cursor.execute(query,values)

        # Commit the changes to the database
        mdb.commit()

        # Close the cursor
        cursor.close()

        return redirect("/ldpatients")
    
    return render_template("ldpredict.html")

#End the session after all processes
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))

#Analyse the input from the system user and predict the disease
@app.route("/predict", methods=['POST', 'GET'])
def predict():  
    if request.method == 'POST':
        Age = int(request.form['Age'])
        Gender = int(request.form['gender'])
        Total_Bilirubin = float(request.form['Total_Bilirubin'])        
        Alkaline_Phosphotase = int(request.form['Alkaline_Phosphotase'])
        Alamine_Aminotransferase = int(request.form['Alamine_Aminotransferase'])
        Aspartate_Aminotransferase = int(request.form['Aspartate_Aminotransferase'])
        Total_Protiens = float(request.form['Total_Protiens'])
        Albumin = float(request.form['Albumin'])
        Albumin_and_Globulin_Ratio = float(request.form['Albumin_and_Globulin_Ratio'])

        values = np.array([[Age,Gender,Total_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]])
        prediction = model.predict(values)

        return render_template('ldpredict.html', prediction=prediction)
    
   
if __name__ == "__main__":
    app.run(debug=True)


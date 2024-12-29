from flask import Flask, request, jsonify, render_template, redirect, url_for, flash ,session
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

app.secret_key = 'Luffy'

client = MongoClient("mongodb://localhost:27017/")
db = client['MoviesDB']  
users_collection = db['Users']  

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        dob = request.form.get('dob')
        gender = request.form.get('gender')


        if users_collection.find_one({"uname": username}):
            flash("User with this email already exists!")
            return redirect(url_for('register'))

        user = {
            "_id": len(list(users_collection.find())) + 800,
            "uname": username,
            "email": email,
            "password": password,
            "dob": dob,
            "gender": gender
        }
        result = users_collection.insert_one(user)
        flash("Registration successful!")
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = users_collection.find_one({"uname": username})

        if username == 'admin' and password == 'admin':
            flash("Login successful!", category='success')
            return redirect(url_for('admin'))
        elif user and user['password'] == password:
            session['user_id'] = str(user['_id'])
            session['username'] = user['uname']
            flash("Login successful!", category='success')
            return redirect(url_for('dashboard'))  
        else:
            flash("Invalid username or password!", category='error')
            
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        flash("You need to login first!")
        return redirect(url_for('login'))


@app.route('/admin', methods=['GET', 'POST'])  
def admin():
    return render_template('admin.html')


@app.route('/user/details', methods=['GET'])
def user_details():
    
    users = list(users_collection.find({}, {"_id": 1, "uname": 1, "email": 1, "dob": 1, "gender": 1}))
    for user in users:
        user["_id"] = str(user["_id"]) 
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(debug=True)

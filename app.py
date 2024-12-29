from flask import Flask, request, jsonify, render_template, redirect, url_for, flash, session
from pymongo import MongoClient

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
            flash("User with this username already exists!")
            return redirect(url_for('register'))

        user = {
            "uname": username,
            "email": email,
            "password": password,  # Plain text password stored
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
        elif user and user['password'] == password:  # Direct password comparison
            session['user_id'] = str(user['_id'])
            session['username'] = user['uname']
            flash("Login successful!", category='success')
            return redirect(url_for('dashboard'))  
        else:
            flash("Invalid username or password!", category='error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' in session:
        collection_map = {
            'Movies': ['title', 'release_year', 'language'],
            'Directors': ['Name', 'DOB', 'Nationality'],
            'Actors': ['Name', 'DOB', 'Awards'],
            'Producer': ['Name', 'Founded Year'],
            'Awards': ['Title', 'Year', 'Recipient']
        }

        # Default to 'Movies' if no collection is selected
        selected_collection = request.form.get('collection') if request.method == 'POST' else None
        
        if not selected_collection:
            flash("Please select a collection to display data!", category="error")

        # Perform the collection query only if a collection is selected
        query = {}
        if selected_collection == 'Movies':
            search_keyword = request.form.get('search_keyword', '').strip()
            if search_keyword:
                query = {'title': {'$regex': search_keyword, '$options': 'i'}}  # Case-insensitive search
        else:
            search_keyword = ""

        # Query the collection data
        collection_data = list(db[selected_collection].find(query, {"_id": 0})) if selected_collection else []

        columns = collection_map.get(selected_collection, [])
        rows = [[entry.get(col.lower(), '') for col in columns] for entry in collection_data]

        return render_template(
            'dashboard.html',
            username=session['username'],
            collection=selected_collection,
            columns=columns,
            rows=rows,
            collections=list(collection_map.keys()),
            search_keyword=search_keyword
        )
    else:
        flash("You need to login first!", category="error")
        return redirect(url_for('login'))




@app.route('/admin', methods=['GET', 'POST'])  
def admin():
    if 'username' not in session or session['username'] != 'admin':
        flash("Access denied! Admins only.")
        return redirect(url_for('login'))
    return render_template('admin.html')


@app.route('/user/details', methods=['GET'])
def user_details():
    users = list(users_collection.find({}, {"_id": 1, "uname": 1, "email": 1, "dob": 1, "gender": 1}))
    for user in users:
        user["_id"] = str(user["_id"]) 
    return jsonify(users), 200

if __name__ == '__main__':
    app.run(debug=True)

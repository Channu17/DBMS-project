from flask import Flask, request, jsonify, render_template, redirect, url_for, flash, session
from pymongo import MongoClient
from get_details import MongoDBQuery

app = Flask(__name__)
app.secret_key = 'Luffy'

client = MongoClient("mongodb://localhost:27017/")
db = client['MoviesDB2']  
users_collection = db['Users']  
details = MongoDBQuery()


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
            "_id":len(list(users_collection.find())) + 800,
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

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        flash("You need to login first!", category="error")
        return redirect(url_for('login'))

    collections = ["Actors", "Directors", "Movies", "Producers", "Awards"]
    rows = []
    columns = []
    search_keyword = ""
    collection = ""

    if request.method == 'POST':
        collection = request.form.get('collection')
        search_keyword = request.form.get('search_keyword')

        if collection and search_keyword:
            if collection == "Actors":
                result = details.get_actor_details(search_keyword)
            elif collection == "Directors":
                result = details.get_director_details(search_keyword)
            elif collection == "Movies":
                result = details.get_movie_details(search_keyword)
            elif collection == "Producers":
                result = details.get_producer_details(search_keyword)
            elif collection == "Awards":
                result = details.get_award_details(search_keyword)
            else:
                result = {"error": "Invalid collection selected"}

            if "error" not in result:
                columns = list(result.keys())
                rows = [list(result.values())]
            else:
                flash(result["error"], category="error")
        else:
            flash("Please select a collection and provide a search keyword.", category="error")

    return render_template(
        'dashboard.html',
        collections=collections,
        collection=collection,
        search_keyword=search_keyword,
        rows=rows,
        columns=columns
    )


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html')
    
@app.route('/admin_manage', methods=['GET', 'POST'])
def admin_manage():
    if request.method == 'POST':
        collection_name = request.form.get('collection')

        if not collection_name:
            flash('Please select a collection to manage.', category='error')
            return redirect(url_for('admin_manage'))

        # Access the MongoDB collection dynamically
        collection = db[collection_name]
        data = {}

        if collection_name == 'Movies':
            data['title'] = request.form.get('title')
            data['release_year'] = int(request.form.get('release_year', 0))
            data['actors'] = [actor.strip() for actor in request.form.get('actors', '').split(',')]
            data['director'] = request.form.get('director')
            data['awards'] = [award.strip() for award in request.form.get('awards', '').split(',')]
            data['language'] = request.form.get('language')
            data['producer'] = request.form.get('producer')
            data['budget'] = request.form.get('budget')
            data['runtime'] = int(request.form.get('runtime', 0))
            data['genre'] = [genre.strip() for genre in request.form.get('genre', '').split(',')]

        elif collection_name == 'Directors':
            data['dname'] = request.form.get('director_name')
            data['DOB'] = int(request.form.get('dob', 0))
            data['nationality'] = request.form.get('nationality')
            data['gender'] = request.form.get('gender')
            data['award'] = request.form.get('award')
            data['notable_movies'] = [movie.strip() for movie in request.form.get('notable_movies', '').split(',')]

        elif collection_name == 'Actors':
            data['aname'] = request.form.get('actor_name')
            data['DOB'] = int(request.form.get('dob', 0))
            data['nationality'] = request.form.get('nationality')
            data['gender'] = request.form.get('gender')
            data['award'] = request.form.get('award')
            data['notable_movies'] = [movie.strip() for movie in request.form.get('notable_movies', '').split(',')]

        elif collection_name == 'Producers':
            data['pname'] = request.form.get('company_name')
            data['est_year'] = int(request.form.get('founded', 0))
            data['HQ'] = request.form.get('headquarters')

        elif collection_name == 'Awards':
            data['awname'] = request.form.get('award_name')
            data['start_year'] = int(request.form.get('year', 0))

        else:
            flash(f'Collection {collection_name} not recognized.', category='error')
            return redirect(url_for('admin_manage'))

        # Insert the data into the collection
        try:
            # Let MongoDB auto-generate the _id field
            collection.insert_one(data)
            flash(f'Successfully added data to {collection_name} collection!', category='success')
        except Exception as e:
            flash(f'Error inserting data: {str(e)}', category='error')

        return redirect(url_for('admin_manage'))

    return render_template('admin_manage.html')

if __name__ == '__main__':
    app.run(debug=True)

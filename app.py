from flask import Flask, request, jsonify, render_template, redirect, url_for, flash, session
from pymongo import MongoClient
from get_details import MongoDBQuery
from updateDetails import MongoDBUpdate


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
            "_id": len(list(users_collection.find())) + 800,
            "uname": username,
            "email": email,
            "password": password,
            "dob": dob,
            "gender": gender
        }
        users_collection.insert_one(user)
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
    collection_name = request.args.get('collection', None)

    if request.method == 'POST':
        collection_name = request.form.get('collection') or request.args.get('collection', None)
        
        if not collection_name:
            flash('Collection not selected!', category='error')
            return redirect(url_for('admin_manage'))

        valid_collections = ['Movies', 'Directors', 'Actors', 'Producers', 'Awards']

        if collection_name not in valid_collections:
            flash('Invalid collection selected.', category='error')
            return redirect(url_for('admin_manage'))

        collection = db[collection_name]
        data = {}

        try:
            if collection_name == 'Movies':
                data = {
                    '_id': len(list(collection.find())) + 1,
                    'title': request.form.get('title'),
                    'release_year': int(request.form.get('release_year', 0)),
                    'actors': [actor.strip() for actor in request.form.get('actors', '').split(',')],
                    'director': request.form.get('director'),
                    'awards': [award.strip() for award in request.form.get('awards', '').split(',')],
                    'language': request.form.get('language'),
                    'producer': request.form.get('producer'),
                    'budget': float(request.form.get('budget', 0)),
                    'runtime': int(request.form.get('runtime', 0)),
                    'genre': [genre.strip() for genre in request.form.get('genre', '').split(',')],
                }
            elif collection_name == 'Directors':
                data = {
                    '_id': len(list(collection.find())) + 201,
                    'dname': request.form.get('director_name'),
                    'DOB': int(request.form.get('dob', 0)),
                    'nationality': request.form.get('nationality'),
                    'gender': request.form.get('gender'),
                    'award': request.form.get('award'),
                    'notable_movies': [movie.strip() for movie in request.form.get('notable_movies', '').split(',')],
                }
            elif collection_name == 'Actors':
                data = {
                    '_id': len(list(collection.find())) + 101,
                    'aname': request.form.get('actor_name'),
                    'DOB': int(request.form.get('dob', 0)),
                    'nationality': request.form.get('nationality'),
                    'gender': request.form.get('gender'),
                    'award': request.form.get('award'),
                    'notable_movies': [movie.strip() for movie in request.form.get('notable_movies', '').split(',')],
                }
            elif collection_name == 'Producers':
                data = {
                    '_id': len(list(collection.find())) + 701,
                    'pname': request.form.get('company_name'),
                    'est_year': int(request.form.get('founded', 0)),
                    'HQ': request.form.get('headquarters'),
                }
            elif collection_name == 'Awards':
                data = {
                    '_id': len(list(collection.find())) + 601,
                    'awname': request.form.get('award_name'),
                    'start_year': int(request.form.get('year', 0)),
                }

            print("Data to insert:", data)
            result = collection.insert_one(data)
            print("Inserted ID:", result.inserted_id)
            flash(f'Successfully added data to {collection_name} collection!', category='success')

        except ValueError as ve:
            flash(f"Invalid data provided: {str(ve)}", category="error")
        except Exception as e:
            flash(f'Error inserting data: {str(e)}', category='error')

        return redirect(url_for('admin_manage', collection=collection_name))

    return render_template('admin_manage.html', collection_name=collection_name)


@app.route('/admin_delete', methods=['GET', 'POST'])
def admin_delete():
    collection_name = request.form.get('collection')
    entity_name = request.form.get('title') or request.form.get('director_name') or \
                  request.form.get('actor_name') or request.form.get('company_name') or \
                  request.form.get('award_name')

    if collection_name and entity_name:
        collection = db[collection_name]
        
        if collection_name == 'Movies':
            result = collection.delete_one({'title': entity_name})
        elif collection_name == 'Directors':
            result = collection.delete_one({'dname': entity_name})
        elif collection_name == 'Actors':
            result = collection.delete_one({'aname': entity_name})
        elif collection_name == 'Producers':
            result = collection.delete_one({'pname': entity_name})
        elif collection_name == 'Awards':
            result = collection.delete_one({'awname': entity_name})

        if result.deleted_count > 0:
            flash(f'{entity_name} deleted successfully!', 'success')
        else:
            flash(f'{entity_name} not found!', 'error')

    return render_template('admin_delete.html', collection_name=collection_name)
@app.route('/admin_update', methods=['GET', 'POST'])
def admin_update():
    collection_name = request.args.get('collection', None)

    if request.method == 'POST':
        collection_name = request.form.get('collection') or request.args.get('collection', None)
        entity_name = request.form.get('entity_name') 
        update_data = {}

        if not collection_name or not entity_name:
            flash("Collection or entity name not provided!", category="error")
            return redirect(url_for('admin_update'))

    
        valid_collections = ['Movies', 'Directors', 'Actors', 'Producers', 'Awards']

        if collection_name not in valid_collections:
            flash("Invalid collection selected!", category="error")
            return redirect(url_for('admin_update'))


        updater = MongoDBUpdate()

        try:

            if collection_name == 'Movies':
                form_data = {
                    'release_year': request.form.get('release_year'),
                    'actors': request.form.get('actors'),
                    'director': request.form.get('director'),
                    'awards': request.form.get('awards'),
                    'language': request.form.get('language'),
                    'producer': request.form.get('producer'),
                    'budget': request.form.get('budget'),
                    'runtime': request.form.get('runtime'),
                    'genre': request.form.get('genre'),
                }

                update_data = {
                    key: ([v.strip() for v in value.split(',')] if ',' in value else int(value) if key in ['release_year', 'runtime'] else float(value) if key == 'budget' else value)
                    for key, value in form_data.items() if value
                }
                result = updater.update_movie_details(entity_name, update_data)

            elif collection_name == 'Directors':
                form_data = {
                    'DOB': request.form.get('dob'),
                    'nationality': request.form.get('nationality'),
                    'gender': request.form.get('gender'),
                    'award': request.form.get('award'),
                    'notable_movies': request.form.get('notable_movies'),
                }

                update_data = {
                    key: ([v.strip() for v in value.split(',')] if ',' in value else int(value) if key == 'DOB' else value)
                    for key, value in form_data.items() if value
                }
                result = updater.update_director_details(entity_name, update_data)

            elif collection_name == 'Actors':
                form_data = {
                    'DOB': request.form.get('dob'),
                    'nationality': request.form.get('nationality'),
                    'gender': request.form.get('gender'),
                    'award': request.form.get('award'),
                    'notable_movies': request.form.get('notable_movies'),
                }

                update_data = {
                    key: ([v.strip() for v in value.split(',')] if ',' in value else int(value) if key == 'DOB' else value)
                    for key, value in form_data.items() if value
                }
                result = updater.update_actor_details(entity_name, update_data)

            elif collection_name == 'Producers':
                form_data = {
                    'est_year': request.form.get('founded'),
                    'HQ': request.form.get('headquarters'),
                }

                update_data = {
                    key: (int(value) if key == 'est_year' else value)
                    for key, value in form_data.items() if value
                }
                result = updater.update_producer_details(entity_name, update_data)

            elif collection_name == 'Awards':
                form_data = {
                    'start_year': request.form.get('year'),
                }

                update_data = {
                    key: int(value) for key, value in form_data.items() if value
                }
                result = updater.update_award_details(entity_name, update_data)

            if "error" not in result:
                flash(f'{entity_name} updated successfully in {collection_name}!', 'success')
            else:
                flash(result["error"], 'error')

        except ValueError as ve:
            flash(f"Invalid data provided: {str(ve)}", category="error")
        except Exception as e:
            flash(f"Error updating data: {str(e)}", category="error")

        return redirect(url_for('admin_update', collection=collection_name))

    return render_template('admin_update.html', collection_name=collection_name)





if __name__ == '__main__':
    app.run(debug=True)

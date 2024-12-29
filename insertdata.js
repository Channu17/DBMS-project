
db.Movies.insertMany([
    {'_id':1 ,'title':'The Dark Knight', 'release_year':2008, 'actors':['Christian Bale', 'Heath Ledger'], 'director':"Christopher Nolan", 'awards':['Academy Awards', 'Golden Globe Awards'], 'language':'English', 'producer':'Warner Bros. Pictures', 'budget':'$185 millions', 'runtime':153, 'genre':['Action','Super-Hero']},
    {'_id':2 ,'title':'Inception', 'release_year':2010, 'actors':['Leonardo Decapri', 'Elliot Page', 'Cillian Murphy'], 'director':"Christopher Nolan", 'awards_id':['Academy Awards', 'Golden Globe Awards', 'Critics Choice Movies Awards'], 'language':'English', 'producer':'Warner Bros. Pictures', 'budget':'$160 millions', 'runtime':148, 'genre':['Thriller','Sci-Fi']},
    {'_id':3 ,'title':'The Fight Club', 'release_year':1999, 'actors':['Edward Nortan', 'Brad Pitt'], 'director':'David Fincher', 'awards':['BAFTA'], 'language':'English', 'producer':'20th Century Studios', 'budget':'$63 millions', 'runtime':139, 'genre':['Thriller','Action']},
    {'_id':4 ,'title':'Avengers', 'release_year':2012, 'actors':['Robert Downey JR', 'Chris Evans', 'Scarlet Johnson'], 'director':'Jose whedon', 'awards':['Academy Awards', 'Golden Globe Awards', 'BAFTA', 'Critics Choice Movies Awards'], 'language':'English', 'producer':703, 'budget':'$220 millions', 'runtime':143, 'genre':['Super-Hero','Action','Sci-Fi']},
    {'_id':5 ,'title':'Iron Man', 'release_year':2008, 'actors':['Robert Downey JR' ], 'director':'Jon Favreau', 'awards':['Academy Awards', 'Critics Choice Movies Awards'], 'language':'English', 'producer':'Marvel Studios', 'budget':'$140 millions', 'runtime':126, 'genre':['Super-Hero','Action','Sci-Fi', 'Fantacy']},
    {'_id':6 ,'title':'Vikram Vedha', 'release_year':2022, 'actors':['Hritik Roshan', 'Saif Ali Khan'], 'director':'Pushkar Gayatri', 'awards':['IIFA'], 'language':'Hindi', 'producer':'T-Series Films', 'budget':'$22 millions', 'runtime':140, 'genre':['Action', 'Thriller']},
    {'_id':7 ,'title':'Dhangal', 'release_year':2016, 'actors':['Amir Khan'], 'director':'Nithis Tiwari', 'awards':['Filmfare Awards','IIFA','Zee Cine Awards'], 'language':'Hindi', 'producer':'Disney Studios', 'budget':'$10 millions', 'runtime':161, 'genre':['Drama', 'Biopic']},
    {'_id':8 ,'title':'Jawan', 'release_year':2023, 'actors':['Shah Rukh Khan', 'Vijay Sethupati'], 'director':'Atlee Kumar', 'awards':['National Film Awards','Screen Awards'], 'language':'Hindi', 'producer':'Red Chillies Entertainment', 'budget':'$25 millions', 'runtime':169, 'genre':['Action', 'Thriller']},
    {'_id':9 ,'title':'3 Idiots', 'release_year':2009, 'actors':['Shah Rukh Khan'], 'director':'Rajkumar Hirani', 'awards':['National Film Awards','Zee Cine Awards'], 'language':'Hindi', 'producer':'Dharma Productions', 'budget':'$8 millions', 'runtime':170, 'genre':['Drama', 'Comedy']},
    {'_id':10 ,'title':'Chichore', 'release_year':2019, 'actors':['Shushant singh Rajput', 'Shraddha Kapoor'], 'director':'Nithis Tiwari', 'awards':['National Film Awards','Screen Awards'], 'language':'Hindi', 'producer':'Nadiadwala Grandson Entertainment', 'budget':'$6 millions', 'runtime':143, 'genre':['Drama', 'Comedy']},
    {'_id':11 ,'title':'Kantara', 'release_year':2022, 'actors':['Rishab Shetty'], 'director':'Rishab Shetty', 'awards':['National Film Awards'], 'language':'Kannada', 'producer':'Hombale Films', 'budget':'$2 millions', 'runtime':148, 'genre':['Action','Mystery']},
    {'_id':12 ,'title':'KGF', 'release_year':2018, 'actors':['Yash'], 'director':'Prashant Neel', 'awards':['Screen Awards', 'Zee Cine Awards'], 'language':'Kannada', 'producer':'Hombale Films', 'budget':'$10 millions', 'runtime':155, 'genre':['Action','Thriller']},
    {'_id':13 ,'title':'Raajakumar', 'release_year':2017, 'actors':['Puneet Rajkumar', 'Priya Anand'], 'director':'Santhosh Anand', 'awards':['Zee Cine Awards'], 'language':'Kannada', 'producer':'Rockline Productions', 'budget':'$9 millions', 'runtime':148, 'genre':['Drama', 'Action']}
])



db.Directors.insertMany([
    {'_id':201, 'dname':'Christopher Nolan', 'DOB':1970, 'nationality':'USA', 'gender':'Male', 'award':'Academy Awards', 'notable_movies':['The Dark Knight', 'Inception']},
    {'_id':202, 'dname':'David Fincher', 'DOB':1962, 'nationality':'USA', 'gender':'Male', 'award':'Golden Globe Awards', 'notable_movies':['The Fight Club']},
    {'_id':203, 'dname':'Jose Whedon', 'DOB':1964, 'nationality':'USA', 'gender':'Male', 'award':'BAFTA', 'notable_movies':['Avengers']},
    {'_id':204, 'dname':'Jon Favreau', 'DOB':1966, 'nationality':'UK', 'gender':'Male', 'award':'BAFTA', 'notable_movies':['Iron Man']},
    {'_id':205, 'dname':'Pushkar Gayatri', 'DOB':1981, 'nationality':'India', 'gender':'Female', 'award':'Zee Cine Awards', 'notable_movies':['Vikram Vedha']},
    {'_id':206, 'dname':'Nithis Tiwari', 'DOB':1974, 'nationality':'India', 'gender':'Male', 'award':'National Film Awards', 'notable_movies':['Dhangal', 'Chichore']},
    {'_id':207, 'dname':'Atlee Kumar', 'DOB':1986, 'nationality':'India', 'gender':'Male', 'award':'Screen Awards', 'notable_movies':['Jawan']},
    {'_id':208, 'dname':'Rajkumar Hirani', 'DOB':1962, 'nationality':'India', 'gender':'Male', 'award':'IIFA', 'notable_movies':['3 Idiots']},
    {'_id':209, 'dname':'Rishab Shetty', 'DOB':1983, 'nationality':'India', 'gender':'Male', 'award':'IIFA', 'notable_movies':['Kantara']},
    {'_id':210, 'dname':'Prashant Neel', 'DOB':1981, 'nationality':'India', 'gender':'Male', 'award':'Screen Awards', 'notable_movies':['KGF']},
    {'_id':211, 'dname':'Santhosh Anand', 'DOB':1985, 'nationality':'India', 'gender':'Male', 'award':'Filmfare Awards', 'notable_movies':['Raajakumar']}
])

db.Actors.insertMany([
    {'_id':101, 'aname':'Christian Bale', 'DOB':1974, 'nationality':'UK', 'gender':'Male', 'award':'Golden Globe Awards', 'notable_movies':['The Dark Knight']},
    {'_id':102, 'aname':'Heath Ledger', 'DOB':1979, 'nationality':'UK', 'gender':'Male', 'award':'BAFTA', 'notable_movies':['The Dark Knight']},
    {'_id':103, 'aname':'Leonardo Decapri', 'DOB':1974, 'nationality':'USA', 'gender':'Male', 'award':'Critics Choice Movies Awards' , 'notable_movies':['Inception']},
    {'_id':104, 'aname':'Elliot Page', 'DOB':1980, 'nationality':'Canada', 'gender':'Female', 'award':'Critics Choice Movies Awards', 'notable_movies':['Inception']},
    {'_id':105, 'aname':'Cillian Murphy', 'DOB':1976, 'nationality':'Irish', 'gender':'Male', 'award':'Academy Awards', 'notable_movies':['Inception']},
    {'_id':106, 'aname':'Edward Nortan', 'DOB':1969, 'nationality':'USA', 'gender':'Male', 'award':'BAFTA', 'notable_movies':['The Fight Club']},
    {'_id':107, 'aname':'Brad Pitt', 'DOB':1963, 'nationality':'USA', 'gender':'Male', 'award':'Academy Awards', 'notable_movies':['The Fight Club']},
    {'_id':108, 'aname':'Robert Downey JR', 'DOB':1965, 'nationality':'USA', 'gender':'Male', 'award':'Golden Globe Awards', 'notable_movies':['Avengers', 'Iron Man']},
    {'_id':109, 'aname':'Chris Evans', 'DOB':1981, 'nationality':'USA', 'gender':'Male', 'award':'BAFTA', 'notable_movies':['Avengers']},
    {'_id':110, 'aname':'Scarlet Johnson', 'DOB':1984, 'nationality':'USA', 'gender':'Female', 'award':'Critics Choice Movies Awards', 'notable_movies':['Avengers']},
    {'_id':111, 'aname':'Hritik Roshan', 'DOB':1974, 'nationality':'India', 'gender':'Male', 'award':'Filmfare Awards', 'notable_movies':['Vikram Vedha']},
    {'_id':112, 'aname':'Saif Ali Khan', 'DOB':1970, 'nationality':'India', 'gender':'Male', 'award':'Screen Awards', 'notable_movies':['Vikram Vedha']},
    {'_id':113, 'aname':'Amir Khan', 'DOB':1965, 'nationality':'India', 'gender':'Male', 'award':'IIFA', 'notable_movies':['Dhangal','3 Idiots']},
    {'_id':114, 'aname':'Shah Rukh Khan', 'DOB':1965, 'nationality':'India', 'gender':'Male', 'award':'National Film Awards', 'notable_movies':['Jawan']},
    {'_id':115, 'aname':'Vijay Sethupati', 'DOB':1978, 'nationality':'India', 'gender':'Male', 'award':'IIFA', 'notable_movies':['Jawan']},
    {'_id':116, 'aname':'Shushant singh Rajput', 'DOB':1986, 'nationality':'India', 'gender':'Male', 'award':'Screen Awards', 'notable_movies':['Chichore']},
    {'_id':117, 'aname':'Shraddha Kapoor', 'DOB':1987, 'nationality':'India', 'gender':'Female', 'award':'Filmfare Awards', 'notable_movies':['Chichore']},
    {'_id':118, 'aname':'Rishab Shetty', 'DOB':1983, 'nationality':'India', 'gender':'Male', 'award':'IIFA', 'notable_movies':['Kantara']},
    {'_id':119, 'aname':'Yash', 'DOB':1986, 'nationality':'India', 'gender':'Male', 'award':'Screen Awards', 'notable_movies':['KGF']},
    {'_id':120, 'aname':'Puneet Rajkumar', 'DOB':1975, 'nationality':'India', 'gender':'Male', 'award':'National Film Awards', 'notable_movies':['Raajakumar']},
    {'_id':121, 'aname':'Priya Anand', 'DOB':1986, 'nationality':'India', 'gender':'Female', 'award':'Zee Cine Awards', 'notable_movies':['Raajakumar']},
])




db.Producer.insertMany([
    {'_id':701, 'pname':'Warner Bros. Pictures', 'est_year':1923, 'HQ':'Burbank, California, USA'},
    {'_id':702, 'pname':'Universal Pictures', 'est_year':1912, 'HQ':'Universal City, California, USA'},
    {'_id':703, 'pname':'Marvel Studios', 'est_year':1993, 'HQ':'Burbank, California, USA'},
    {'_id':704, 'pname':'Paramount Pictures', 'est_year':1912, 'HQ':'Hollywood, California, USA'},
    {'_id':705, 'pname':'Disney Studios', 'est_year':1923, 'HQ':'Burbank, California, USA'},
    {'_id':706, 'pname':'20th Century Studios', 'est_year':1935, 'HQ':'Los Angeles, California, USA'},
    {'_id':707, 'pname':'Yash Raj Films (YRF)', 'est_year':1970, 'HQ':'Mumbai, Maharashtra, India'},
    {'_id':708, 'pname':'Dharma Productions', 'est_year':1976, 'HQ':'Mumbai, Maharashtra, India'},
    {'_id':709, 'pname':'T-Series Films', 'est_year':1983, 'HQ':'Noida, Uttar Pradesh, India'},
    {'_id':710, 'pname':'Red Chillies Entertainment', 'est_year':2003, 'HQ':'Mumbai, Maharashtra, India'},
    {'_id':711, 'pname':'Excel Entertainment', 'est_year':1999, 'HQ':'Mumbai, Maharashtra, India'},
    {'_id':712, 'pname':'Hombale Films', 'est_year':2014, 'HQ':'Bengaluru, Karnataka, India'},
    {'_id':713, 'pname':'Jayanna Combines', 'est_year':2001, 'HQ':'Bengaluru, Karnataka, India'},
    {'_id':714, 'pname':'Rockline Productions', 'est_year':1996, 'HQ':'Bengaluru, Karnataka, India'},
    {'_id':715, 'pname':'Nadiadwala Grandson Entertainment', 'est_year':1952, 'HQ':'Mumbai, Maharashtra, India'}
])


db.Awards.insertMany([
    {'_id':601, 'awname':'Academy Awards', 'start_year':1929},
    {'_id':602, 'awname':'Golden Globe Awards', 'start_year':1944},
    {'_id':603, 'awname':'BAFTA', 'start_year':1947},
    {'_id':604, 'awname':'Critics Choice Movies Awards', 'start_year':1995},
    {'_id':605, 'awname':'Filmfare Awards', 'start_year':1954},
    {'_id':606, 'awname':'National Film Awards', 'start_year':1954},
    {'_id':607, 'awname':'IIFA', 'start_year':2000},
    {'_id':608, 'awname':'Screen Awards', 'start_year':1994},
    {'_id':609, 'awname':'Zee Cine Awards', 'start_year':1998},
])


from pymongo import MongoClient

class MongoDBQuery:
    def __init__(self, db_name="MoviesDB2"):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]

    def get_actor_details(self, actor_name):
        actor = self.db.Actors.find_one({"aname": actor_name})
        if actor:
            return {key: ", ".join(value) if isinstance(value, list) else value for key, value in actor.items() if key != "_id"}
        else:
            return {"error": "Actor not found"}

    def get_director_details(self, director_name):
        director = self.db.Directors.find_one({"dname": director_name})
        if director:
            return {key: ", ".join(value) if isinstance(value, list) else value for key, value in director.items() if key != "_id"}
        else:
            return {"error": "Director not found"}

    def get_movie_details(self, movie_title):
        movie = self.db.Movies.find_one({"title": movie_title})
        if movie:
            return {key: ", ".join(value) if isinstance(value, list) else value for key, value in movie.items() if key != "_id"}
        else:
            return {"error": "Movie not found"}

    def get_producer_details(self, producer_name):
        producer = self.db.Producer.find_one({"pname": producer_name})
        if producer:
            return {key: ", ".join(value) if isinstance(value, list) else value for key, value in producer.items() if key != "_id"}
        else:
            return {"error": "Producer not found"}

    def get_award_details(self, award_name):
        award = self.db.Awards.find_one({"awname": award_name})
        if award:
            return {key: ", ".join(value) if isinstance(value, list) else value for key, value in award.items() if key != "_id"}
        else:
            return {"error": "Award not found"}
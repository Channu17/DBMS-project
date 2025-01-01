from pymongo import MongoClient

class MongoDBUpdate:
    def __init__(self, db_name="MoviesDB2"):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]

    def update_actor_details(self, actor_name, update_data):
        result = self.db.Actors.update_one({"aname": actor_name}, {"$set": update_data})
        if result.matched_count > 0:
            return {"message": "Actor details updated successfully"}
        else:
            return {"error": "Actor not found"}

    def update_director_details(self, director_name, update_data):
        result = self.db.Directors.update_one({"dname": director_name}, {"$set": update_data})
        if result.matched_count > 0:
            return {"message": "Director details updated successfully"}
        else:
            return {"error": "Director not found"}

    def update_movie_details(self, movie_title, update_data):
        result = self.db.Movies.update_one({"title": movie_title}, {"$set": update_data})
        if result.matched_count > 0:
            return {"message": "Movie details updated successfully"}
        else:
            return {"error": "Movie not found"}

    def update_producer_details(self, producer_name, update_data):
        result = self.db.Producer.update_one({"pname": producer_name}, {"$set": update_data})
        if result.matched_count > 0:
            return {"message": "Producer details updated successfully"}
        else:
            return {"error": "Producer not found"}

    def update_award_details(self, award_name, update_data):
        result = self.db.Awards.update_one({"awname": award_name}, {"$set": update_data})
        if result.matched_count > 0:
            return {"message": "Award details updated successfully"}
        else:
            return {"error": "Award not found"}

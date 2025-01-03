
db.createCollection("Movies",{
    validator:{
        $jsonSchema:{
            required:['_id','title','release_year'],
            properties:{
                _id:{
                    bsonType:'number'
                },
                title:{
                    bsonType:'string',
                },
                release_year:{
                    bsonType:'number'
                }
            }
        }
    }
})

db.createCollection("Actors",{
    validator:{
        $jsonSchema:{
            required:['_id','aname'],
            properties:{
                actor_id:{
                    bsonType:'number'
                },
                aname:{
                    bsonType:'string'
                }
            }
        }
    }
})


db.createCollection("Directors",{
    validator:{
        $jsonSchema:{
            required:['_id','dname'],
            properties:{
                _id:{
                    bsonType:'number'
                },
                dname:{
                    bsonType:'string'
                }
            }
        }
    }
})

db.createCollection("Reviews",{
    validator:{
        $jsonSchema:{
            required:['_id', 'movie_id', 'rating'],
            properties:{
                _id:{
                    bsonType:'number'
                },
                movie_id:{
                    bsonType:'number'
                },
                rating:{
                    bsonType:'number'
                }
            }
        }
    }
})

db.createCollection("Users",{
    validator:{
        $jsonSchema:{
            required:['_id','uname'],
            properties:{
                _id:{
                    bsonType:'number'
                },
                uname:{
                    bsonType:'string'
                }
            }
        }
    }
})

db.createCollection("Awards",{
    validator:{
        $jsonSchema:{
            required:['_id', 'awname'],
            properties:{
                _id:{
                    bsonType:'number'
                },
                awname:{
                    bsonType:'string'
                }
            }
        }
    }
})

db.createCollection("Producer",{
    validator:{
        $jsonSchema:{
            required:['_id', 'pname'],
            properties:{
                _id:{
                    bsonType:'number'
                },
                pname:{
                    bsonType:'string'
                }
            }
        }
    }
})




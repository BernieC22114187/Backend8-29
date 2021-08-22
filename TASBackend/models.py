import mongoengine
from mongoengine.fields import StringField

import jwt
from config import config
from datetime import datetime, timedelta

class Member (mongoengine.Document):
    account = mongoengine.StringField()
    password = mongoengine.StringField()
    weight = mongoengine.IntField()
    height = mongoengine.IntField()
    timestamp = mongoengine.IntField()
    
    @property
    def token(self):
        return self._generate_jwt_token()
    
    def _generate_jwt_token(self):
        token = jwt.encode({
            'exp': datetime.utcnow() + timedelta(days = 1),
            'iet': datetime.utcnow(),
            'data':{
                'id':str(self.id),
            }
        }, config['SECRET_KEY'], algorithm = 'HS256')
        return token.decode("utf-8")
    # data = mongoengine.DictField()
    # add dish model

class dish (mongoengine.Document):
    Name = mongoengine.StringField() # name has to be the same as the string in serializer
    Calories = mongoengine.IntField()
    Total_Fat = mongoengine.FloatField()    
    Cholesterol = mongoengine.IntField() 
    Sodium = mongoengine.IntField()
    Total_Carbs = mongoengine.IntField()
    Protein = mongoengine.IntField()
    Index = mongoengine.IntField()
    Timestamp = mongoengine.IntField()

class data(mongoengine.Document): # member's daily nutrition data
    Member_id = mongoengine.StringField()
    Timestamp = mongoengine.StringField()
    Calories = mongoengine.FloatField()
    Total_Fat = mongoengine.FloatField()    
    Cholesterol = mongoengine.IntField() 
    Sodium = mongoengine.IntField()
    Total_Carbs = mongoengine.IntField()
    Protein = mongoengine.IntField()

class doExercise(mongoengine.Document):
    Member_id = mongoengine.StringField()
    Timestamp = mongoengine.StringField()
    burnedCalories = mongoengine.FloatField()

class exercise(mongoengine.Document):
    Name = mongoengine.StringField()
    Ratio = mongoengine.FloatField()


class dailyMenu(mongoengine.Document):
    Date = mongoengine.DateTimeField()
    RestName = mongoengine.StringField()
    Main = mongoengine.ListField(StringField())
    Side = mongoengine.ListField(StringField())
    Fruit = mongoengine.ListField(StringField())

class constantMenu(mongoengine.Document):
    
    dailyCarbs = mongoengine.ListField()
    drinks = mongoengine.ListField()
    saladBar = mongoengine.ListField()
    pizzaBar = mongoengine.ListField()
    snackBarPastries = mongoengine.ListField()
    snackBarCookies = mongoengine.ListField()
    snackBarOther = mongoengine.ListField()
    snackBarDesserts = mongoengine.ListField()
    snackBarPies = mongoengine.ListField()
    snackBarMisc = mongoengine.ListField()




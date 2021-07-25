import mongoengine
from mongoengine.fields import StringField

class Member (mongoengine.Document):
    account = mongoengine.StringField()
    password = mongoengine.StringField()
    weight = mongoengine.IntField()
    height = mongoengine.IntField()
    timestamp = mongoengine.IntField()
    
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
    Calories = mongoengine.IntField()
    Total_Fat = mongoengine.FloatField()    
    Cholesterol = mongoengine.IntField() 
    Sodium = mongoengine.IntField()
    Total_Carbs = mongoengine.IntField()
    Protein = mongoengine.IntField()

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




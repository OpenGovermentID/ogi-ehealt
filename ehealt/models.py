from mongoengine import *
import datetime

# Create your models here.
class Contact(EmbeddedDocument):
	content = StringField(max_length=50)
	types = StringField(max_length=50)

class Facility(EmbeddedDocument):
	name = StringField(max_length=50)
	description = StringField(max_length=250)
	types = StringField(max_length=50)

class Location(EmbeddedDocument):
	lat = StringField(max_length=50)
	lon = StringField(max_length=50)
	
class Hospital(Document):
	name = StringField(max_length=120, required=True)
	types = StringField(max_length=50)
	ownership = StringField(max_length=50)
	description = StringField(max_length=250)
	address = StringField(max_length=120)
	city = StringField(max_length=30)
	province = StringField(max_length=30)
	zip_code = StringField(max_length=30)
	contact = ListField(EmbeddedDocumentField(Contact))
	country = StringField(max_length=50)
	facility = ListField(EmbeddedDocumentField(Facility))
	location = EmbeddedDocumentField(Location)
	created_at = DateTimeField(required=True, default=datetime.datetime.now)
	updated_at = DateTimeField(required=True, default=datetime.datetime.now)
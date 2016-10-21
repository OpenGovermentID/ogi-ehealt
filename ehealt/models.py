from mongoengine import *
import datetime

# Create your models here.
class Contact(EmbeddedDocument):
	CONTACT_TYPES = (
			('phone', 'Phone'),
			('email', 'E-Mail'),
			('fax', 'Fax'),
			('website', 'Website'),
			('whatsapp', 'WhatsApp'),
			('twitter', 'Twitter'),
			('facebook', 'Facebook'),
			('instagram', 'Instagram'),
			('bbm', 'Blackberry Messenger'),
		)

	content = StringField(max_length=50)
	types = StringField(max_length=25, choices=CONTACT_TYPES)

class Facility(EmbeddedDocument):
	FACILITY_TYPES = (
			('medical', 'Medical'),
			('general', 'General'),	
			('restaurant', 'Restaurant'),	
			('sport', 'Sport'),	
		)
	name = StringField(max_length=50)
	description = StringField(max_length=250)
	types = StringField(max_length=25, choices=FACILITY_TYPES)

class Hospital(Document):
	name = StringField(max_length=120, required=True)
	types = StringField(max_length=50)
	ownership = StringField(max_length=50)
	description = StringField(max_length=250)
	
	address = StringField(max_length=120)
	city = StringField(max_length=30)
	province = StringField(max_length=30)
	country = StringField(max_length=50)
	zip_code = StringField(max_length=30)
	
	contact = ListField(EmbeddedDocumentField(Contact))
	facility = ListField(EmbeddedDocumentField(Facility))
	location = DictField()
	
	created_at = DateTimeField(required=True, default=datetime.datetime.now)
	updated_at = DateTimeField(required=True, default=datetime.datetime.now)
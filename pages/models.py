from django.http import HttpResponse
from django.db import models

# Create your models here.
def home_view(*args, **kwargs): # *args, **kwargs
	return "<h1>Hello World</h1>" # string of HTML code
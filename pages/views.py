from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
	print(args, kwargs) # print in shell
	print(request.user)
	#return HttpResponse("<h1>Hello World</h1>") # string of HTML code
	return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
	return render(request, "contact.html", {})


def about_view(request, *args, **kwargs): # *args, **kwargs
	my_context = {
		"title": "this is about us",
		"my_number": 123,
		"my_list": [123, 4242, 123123, "AAA"]

	}
	return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
	return HttpResponse("<h1>Social Page</h1>")

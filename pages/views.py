from django.shortcuts import render

def home(request):
	return render(request, "home.html", {})

def about(request):
	from pages.description import description1
	return render(request, "about.html", {"describing" : description1})
from django.shortcuts import render

def index(request):
	return render(request, 'index.html')


def about(request):
	return render(request, 'about.html')

def portfolio(request):
	return render(request, 'portfolio.html')

def services(request):
	return render(request, 'services.html')

def contact(request):
	return render(request, 'contact.html')

# Create your views here.

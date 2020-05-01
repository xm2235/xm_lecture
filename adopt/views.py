from django.http import HttpResponse
from django.shortcuts import render
from .models import Pet


def index(request): 
	return HttpResponse('Hello World, XM!!!')

def list_pets(request):
       	# response = '<ul>'
	pets = Pet.objects.all()
	
	return render(request,'adopt/list.html',{'pets':pets}) 

def get_pet(request,pet_id):
	
	pet = Pet.objects.get(id = pet_id)	
	
	return HttpResponse( f'Hello, This is {pet.name}!')




	

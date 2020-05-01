from django.http import HttpResponse

from .models import Pet


def index(request): 
	return HttpResponse('Hello World, XM!!!')

def list_pets(request):
        response = '<ul>'

        pets = Pet.objects.all()
        for pet in pets:
                response += f'<li><a href="/adopt/{pet.id}">{pet.name}</a></li>'       
        response += '</ul>'

        return HttpResponse(response)

def get_pet(request,pet_id):
	
	pet = Pet.objects.get(id = pet_id)	
	
	return HttpResponse( f'Hello, This is {pet.name}!')




	

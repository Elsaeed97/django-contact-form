from django.shortcuts import render
from .models import Message
# Create your views here.

def contact(request):
	if request.method == 'POST':
		name = request.POST.get("name")
		email = request.POST.get("email")
		message = request.POST.get("message")
		# Insert Data into the Model 
		contact = Message()
		contact.name 	= name  
		contact.email 	= email
		contact.message = message
		contact.save()


	return render(request, "index.html",{})
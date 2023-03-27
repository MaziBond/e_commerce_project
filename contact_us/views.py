from django.shortcuts import render
from .form import ContactUsForm
from .models import ContactUs
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method == "POST":
        contact_us_form = ContactUsForm()
        if contact_us_form.is_valid():
	        contact_us_form.save()
		    messages.success(request, ('Your comment were successfully saved.'))
		else:
	        messages.error(request, ('Error saving your comment'))
	else:
		messages.error(request, ('Error saving your comment'))
	
    contact_us_form = ContactUsForm()
	contact_us = ContactUs.objects.all()
	return render(request=request, template_name="contact_us.html", 
	       context={'contact_us_form': contact_us_form, 
		            'contact_us': contact_us})
		




# Create your views here.
def homepage(request):
	if request.method == "POST":
		movie_form = MovieForm(request.POST, request.FILES)
		if movie_form.is_valid():
			movie_form.save()
			messages.success(request, ('Your movie was successfully added!'))
		else:
			messages.error(request, 'Error saving form')
			
    else:
			messages.error(request, 'Error saving form')
		
		
		return redirect("main:homepage")
	
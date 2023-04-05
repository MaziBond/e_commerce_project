from django.contrib import messages
from django.shortcuts import render, redirect

from contact_us.forms import ContactUsForm

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Request Submitted Successfully')
            return redirect('contact-us')
    else:
        form = ContactUsForm()
    
    context = {
        'form': form,
    }
    return render(request, 'contact_us/contact.html', context)

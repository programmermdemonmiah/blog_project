from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Contact

def contact_us(request):
    return render(request, 'contact_us.html', {'title': 'Contact Us'})

def contact_submit(request):
    if request.method == "POST":
        contact = Contact(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )

        try:
            contact.save_contact()
            messages.success(request, "Message sent successfully.")
            return redirect("business:contact_us")
        except ValidationError as e:
            messages.error(request, "There were errors in your submission.")
            return render(
                request,
                "contact_us.html",
                {
                    "errors": e.message_dict,
                    "old": request.POST,
                    "title": "Contact Us"
                },
            )

    return render(request, 'contact_us.html', {'title': 'Contact Us'})
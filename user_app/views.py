from django.shortcuts import render, redirect 
from .models import User
# Import models from the User table in db


# Create your views here. THIS METHOD IS THE R IN CRUD.
def index(request):
    # R in the CRUD for all movies
    # Get all users - models.py
    all_users = User.objects.all()
    # we are assigning an objects value to a all_users var, which we assign to a context dict
    print(all_users)

    context = {
        # context is a dict
        'users': all_users
        # users is a key and all_users is the var 
        # READ INDEX EXPLANATION
    }
    return render(request, 'index.html', context)
    # putting context into the argument sends it to the template

def create(request):
    # C in CRUD to create a user
    print(request.POST)
    # I am printing to see make sure I am getting the info and not recreating info FROM HTML
    User.objects.create(first_name=request.POST['form_first_name'], last_name=request.POST['form_last_name'], email_address=request.POST['form_email'], age=request.POST['form_age'])
    return redirect('/')
    # after c info we want to redirect back to the same place 
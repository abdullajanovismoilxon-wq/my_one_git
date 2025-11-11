from django.shortcuts import render, redirect
from .models import Person
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        company = request.POST.get('company')
        phone = request.POST.get('phone')
        exist = request.POST.get('exist', 'No')


        Person.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            company=company,
            phone=phone,
            exist=exist
        )

        return redirect('registered')

    return render(request, 'register.html')


def registered(request):
    people = Person.objects.all().order_by('-id')
    return render(request, 'registered.html', {'people': people})
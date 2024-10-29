from django.shortcuts import render
from uni_app.models import Cat

# Create your views here.
def usView(request):
    return render(request, 'contact.html', {'cats':Cat.objects.all()})
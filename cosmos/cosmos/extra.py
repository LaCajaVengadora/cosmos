from django.shortcuts import render; from uni_app.models import Cat
def extra(r):return render(r,'extra/extra.html',{'cats':Cat.objects.order_by("name")})
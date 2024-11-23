from django.shortcuts import render, redirect; from uni_app.models import Cat
def extra(r):return render(r,'extra/extra.html',{'cats':Cat.objects.order_by("name")})
def git(r):return redirect("https://github.com/LaCajaVengadora/cosmos")
def custom_500_view(r, e=None): return render(r, 'extra/error.html', {'status':500}, status=500)
def custom_404_view(r, e=None): return render(r, 'extra/error.html', {'status':404}, status=404)
def custom_403_view(r, e=None): return render(r, 'extra/error.html', {'status':403}, status=403)
def custom_400_view(r, e=None): return render(r, 'extra/error.html', {'status':400}, status=400)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='auth:login')
def blog_view(request): return render(request, 'blog.html')
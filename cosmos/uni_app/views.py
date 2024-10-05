from django.shortcuts import render
from django.core.paginator import Paginator
from uni_app.models import Carrera, Cat, Uni
from django.db.models import Q

# Create your views here.
def testView(request): return render(request, "test.html", {})

'''
HOME
- SEARCHER (CATS, CARRERAS & UNIS) => SEARCH PAGE (VIEW)

'''
def home_view(request):
    ctx = {"unis":Uni.objects.all(), "cats":Cat.objects.all(), "carreras":Carrera.objects.all()}
    return render(request, "home.html", ctx)

def search_view(request, type, id):
    if type=="cat": 
        filter = Cat.objects.get(id=id)
        carreras = Carrera.objects.filter(cat=filter)
    elif type=="uni": 
        filter = Uni.objects.get(id=id)
        carreras = Carrera.objects.filter(uni=filter)
    ctx = {"unis":Uni.objects.all(),"cats":Cat.objects.all(), 
           "carreras":carreras, "filter":filter}
    return render(request, "search.html", ctx)

#def home_filtered_view(request): return get_data(request);

'''def get_data(request, cat=None):
    query = request.GET.get('q'); raw_items = Carrera.objects.all()

    if cat: raw_items = raw_items.filter(category__name=cat)
    if query: 
        raw_items = raw_items.filter(
            Q(ID__icontains=query) | Q(marca__icontains=query) | Q(modelo__icontains=query)
        )

    paginator = Paginator(raw_items.order_by('-price'), 12)# con Paginator, teniendo los items, divide cada 12 items por pag
    pag_num = request.GET.get('page', 1) # Obtiene num de pag del request, por defecto da 1
    items = paginator.get_page(pag_num) # Devuelve la pag con sus items
    
    cats = Category.objects.all()

    return render(request, 'home.html', {'items':items,'cats':cats})'''


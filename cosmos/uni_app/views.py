from django.shortcuts import render
from django.core.paginator import Paginator
from uni_app.models import Carrera, Cat, Uni
from django.db.models import Q

# Create your views here.
def testView(request): return render(request, "test.html", {})

def home_view(request):

    carreras = Carrera.objects.all() # GET ALL ITEMS ON Carrera
    ctx = {"unis" : Uni.objects.all(), "cats" : Cat.objects.all(), "carreras" : carreras}
    # ↑ SAME WITH Uni & Cat; MAKE ctx DICTIONARY WITH ALL
    
    return render(request, "home.html", ctx) # IF NOT query, RENDER home.html TEMPLATE WITH ctx

# ------------ UNUSED -----------
def filter_view(request, type, id): # GET type & id FROM URL

    if type=="cat": # IF FILTER type IS cat, GET Cat BY id & FILTER Carrera WITH THAT Cat
        filter = Cat.objects.get(id=id); carreras = Carrera.objects.filter(cat=filter)
    elif type=="uni": # ↑ SAME
        filter = Uni.objects.get(id=id); carreras = Carrera.objects.filter(uni=filter)

    ctx = {"unis":Uni.objects.all(),"cats":Cat.objects.all(), 
           "carreras":carreras, "filter":filter.name}
    
    return render(request, "filter.html", ctx) # RENDER filter.html TEMPLATE WITH ctx

def search_view(request):
    query = request.GET.get('q')
    cat = request.GET.get('cat'); uni = request.GET.get('uni')
    loc = request.GET.get('loc'); price = request.GET.get('pr'); duration = request.GET.get('dur')

    ctx = {"unis" : Uni.objects.all(), "cats" : Cat.objects.all(), "query": None}
    carreras = Carrera.objects.all()

    if query and query!="": # IF THERE WAS query
        carreras = carreras.filter(
            Q(id__icontains=query) | Q(desc__icontains=query) | Q(name__icontains=query)
        )
        ctx["query"] = f"'{query}'"
    if cat: carreras = carreras.filter(cat=Cat.objects.get(id=cat))
    if uni: carreras = carreras.filter(uni=Uni.objects.get(id=uni))
    #if loc: carreras = carreras.filter(uni=Uni.objects.filter(Q(location__icontains=loc)[0]))
    ctx["carreras"]=carreras # UPDATE ctx DICTIONARY WITH carreras FILTERED
    #if price: carreras.filter(price=Cat.objects.get(id=cat))
    #if duration: carreras.filter(cat=Cat.objects.get(id=cat))

    return render(request, "search.html", ctx) # RENDER filter.html TEMPLATE WITH ctx

def carrera_view(request, id):
    carrera = Carrera.objects.get(id=id); ctx = {"carrera":carrera}
    return render(request, "carrera.html", ctx)

def uni_view(request, id):
    uni = Uni.objects.get(id=id); carreras = Carrera.objects.filter(uni=uni)
    ctx = {"uni": uni,"carreras":carreras}
    return render(request, "uni.html", ctx)


''' ---------------------- ↓ IGNORE THIS BUT DO NOOOOT DELETE!!!! ↓ -----------------------
def get_data(request, cat=None):
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


from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from uni_app.models import Carrera, Cat, Uni, Curso, Beca
from django.db.models import Q

# Create your views here.
def testView(request): return render(request, "test.html", {})

def home_view(request):
    
    return render(request, "home.html", {"cats" : Cat.objects.order_by('name')})


def search_view(request):
    
    query = request.GET.get('q')
    cat = request.GET.get('cat'); uni = request.GET.get('uni')
    #loc = request.GET.get('loc'); price = request.GET.get('pr'); duration = request.GET.get('dur')

    ctx = {"cats" : Cat.objects.order_by('name'), "unis" : Uni.objects.order_by("name"), "query": None}
    carreras = Carrera.objects.order_by('name')

    if query and query!="": # IF THERE WAS query
        carreras = carreras.filter(
            Q(desc__icontains=query) | Q(name__icontains=query) | Q(uni__name__icontains=query)
        )
        ctx["query"] = f"'{query}'"
    if cat: carreras = carreras.filter(cat=Cat.objects.get(id=cat))
    if uni: carreras = carreras.filter(uni=Uni.objects.get(id=uni))
    
    paginator = Paginator(carreras, 6)
    page = request.GET.get('page', 1)
    carreras = paginator.get_page(page)

    ctx["carreras"]=carreras # UPDATE ctx DICTIONARY WITH carreras FILTERED
    #if loc: carreras = carreras.filter(uni=Uni.objects.filter(Q(location__icontains=loc)[0]))
    #if price: carreras.filter(price=Cat.objects.get(id=cat))
    #if duration: carreras.filter(cat=Cat.objects.get(id=cat))

    return render(request, "search.html", ctx) # RENDER filter.html TEMPLATE WITH ctx


def many_view(request, type):
    
    ctx = {'cats':Cat.objects.order_by('name'), "type":type}; result=None

    if type=="unis": result=Uni.objects.order_by('name')
    elif type=="cursos": result=Curso.objects.order_by('name')
    elif type=="becas": result=Beca.objects.order_by('name')
    else: return redirect("extra")

    paginator = Paginator(result, 8)
    page = request.GET.get('page', 1)
    result = paginator.get_page(page)

    ctx["result"]=result

    return render(request, "many.html", ctx)


def one_view(request, type, id):

    ctx = {'cats':Cat.objects.order_by('name'), "type":type}

    if type=="unis": 
        uni = Uni.objects.get(id=id); ctx["one"]=uni
        ctx["carreras"]=Carrera.objects.filter(uni=uni)
        ctx["cursos"]=Curso.objects.filter(uni=uni)
        ctx["becas"]=Beca.objects.filter(uni=uni)
    elif type=="cursos":
        curso = Curso.objects.get(id=id)
        ctx["one"]=curso; ctx["related"]=Curso.objects.filter(cat=curso.cat).exclude(id=id)[:3]
    elif type=="carreras":
        carrera = Carrera.objects.get(id=id)
        ctx["one"]=carrera; ctx["related"]=Carrera.objects.filter(cat=carrera.cat).exclude(id=id)[:3]
    elif type=="becas":
        ctx["one"]=Beca.objects.get(id=id)
    else: return redirect("extra")

    return render(request, "one.html", ctx)

#
#def carrera_view(request, id):
#    carrera = Carrera.objects.get(id=id); ctx = {"carrera":carrera, 'cats':Cat.objects.all()}
#    return render(request, "individual/carrera.html", ctx)
#
#def curso_view(request, id):
#    curso = Curso.objects.get(id=id); ctx = {"curso":curso, 'cats':Cat.objects.all()}
#    return render(request, "individual/curso.html", ctx)
#
#def uni_view(request, id):
#    uni = Uni.objects.get(id=id); carreras = Carrera.objects.filter(uni=uni)
#    ctx = {"uni": uni, "carreras":carreras, "cats":Cat.objects.all()}
#    return render(request, "individual/uni.html", ctx)
#
#def unis_view(request):
#    return render(request, "unis.html", {'unis':Uni.objects.all(), "cats":Cat.objects.all()})
#
#def cursos_view(request):
#    return render(request, "cursos.html", {'cursos':Curso.objects.all(), "cats":Cat.objects.all()})
#
def compare_view(request, type):

    ctx={"type":type, "cats":Cat.objects.order_by('name'), "options":None, "chosen":None}
    
    if type=='unis': ctx["options"]=Uni.objects.order_by('name')
    elif type=='carreras': ctx["options"]=Carrera.objects.order_by('name')
    elif type=='cursos': ctx["options"]=Curso.objects.order_by('name')
    else: ctx["options"]=Beca.objects.order_by('name')
    
    id1, id2 = request.GET.get('id1'), request.GET.get('id2')
    if id1 and id2 and id1!=id2:
        if type=="unis":
            uni1, uni2 = Uni.objects.get(id=id1), Uni.objects.get(id=id2)
            ctx["chosen"]=zip((uni1, uni2),
                              (Carrera.objects.filter(uni=uni1), Carrera.objects.filter(uni=uni2)),
                              (Curso.objects.filter(uni=uni1), Curso.objects.filter(uni=uni2)),
                              (Beca.objects.filter(uni=uni1), Beca.objects.filter(uni=uni2)))
        elif type=="carreras":
            ctx["chosen"]=(Carrera.objects.get(id=id1), Carrera.objects.get(id=id2))
        elif type=="cursos":
            ctx["chosen"]=(Curso.objects.get(id=id1), Curso.objects.get(id=id2))
        else:
            ctx["chosen"]=(Beca.objects.get(id=id1), Beca.objects.get(id=id2))

    return render(request, "compare.html", ctx)


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
# ------------ UNUSED -----------
def filter_view(request, type, id): # GET type & id FROM URL

    if type=="cat": # IF FILTER type IS cat, GET Cat BY id & FILTER Carrera WITH THAT Cat
        filter = Cat.objects.get(id=id); carreras = Carrera.objects.filter(cat=filter)
    elif type=="uni": # ↑ SAME
        filter = Uni.objects.get(id=id); carreras = Carrera.objects.filter(uni=filter)

    ctx = {"unis":Uni.objects.all(),"cats":Cat.objects.all(), 
           "carreras":carreras, "filter":filter.name}
    
    return render(request, "filter.html", ctx) # RENDER filter.html TEMPLATE WITH ctx


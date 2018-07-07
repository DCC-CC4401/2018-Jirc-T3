from django.shortcuts import render, redirect

from .models import Item, FechaDeReserva
# Create your views here.


def lista(request):

    item = Item.objects.all()

    if request.method == 'POST':
        for inv in item:
            if inv.id in request.POST:
                context = {
                    'item': inv
                }
                return render(request, 'fichaArticulo.html', context)

    context = {
        'item': item
    }

    return render(request, 'listaArticulos.html', context)


def fichaArticulo(request):
    item = Item.objects.all()

    if request.method == 'POST':
        for inv in item:
            if inv.id in request.POST:
                context = {
                    'item': inv
                }
                idate = request.POST['idate']
                fdate = request.POST['fdate']
                itime = request.POST['itime']
                ftime = request.POST['ftime']
                fecha = FechaDeReserva(iDate=idate, fDate=fdate, iTime=itime, fTime=ftime)
                fecha.save()
                inv.save()
                inv.Reserva.add(fecha)
                inv.save()
                return render(request, 'fichaArticulo.html', context)

    context = {
        'item': item
    }

    return render(request, 'fichaArticulo.html', context)


def reserva(request):
    item = Item.objects.all()

    context = {
        'item': item
    }
    if request.method == 'POST':
        name = request.POST['name']
        img = request.FILES.get('imgFile')
        it = Item(name=name, description="un articulo de prueba", state=1, img=img)
        it.save()
        return redirect('/fichaArticulo/')

    return render(request, 'fichaArticulo.html', context)


def editar(request):
    item = Item.objects.all()

    if request.method == 'POST':
        for inv in item:
            if inv.id in request.POST:
                context = {
                    'item': inv
                }
                return render(request, 'fichaArticuloEdit.html', context)

    context = {
        'item': item
    }

    return render(request, 'fichaArticuloEdit.html', context)


def editarDes(request):
    item = Item.objects.all()

    if request.method == 'POST':
        for inv in item:
            if inv.id in request.POST:
                context = {
                    'item': inv
                }
                return render(request, 'fichaArticuloEditDes.html', context)

    context = {
        'item': item
    }

    return render(request, 'fichaArticuloEdit.html', context)


def editarFoto(request):
    item = Item.objects.all()

    if request.method == 'POST':
        for inv in item:
            if inv.id in request.POST:
                context = {
                    'item': inv
                }
                return render(request, 'fichaArticuloEditarFoto.html', context)

    context = {
        'item': item
    }

    return render(request, 'fichaArticuloEdit.html', context)


def editarEst(request):
    item = Item.objects.all()

    if request.method == 'POST':
        for inv in item:
            if inv.id in request.POST:
                context = {
                    'item': inv
                }
                return render(request, 'fichaArticuloEditarEst.html', context)

    context = {
        'item': item
    }

    return render(request, 'fichaArticuloEdit.html', context)


def aceptarNombre(request):
    item = Item.objects.all()

    if request.method == 'POST':
        for inv in item:
            if inv.id in request.POST:
                context = {
                    'item': inv
                }
                inv.name = request.POST['name']
                inv.save()
                return render(request, 'fichaArticulo.html', context)

    context = {
        'item': item
    }

    return render(request, 'fichaArticuloEdit.html', context)


def cancelarNombre(request):
    item = Item.objects.all()

    if request.method == 'POST':
        for inv in item:
            if inv.id in request.POST:
                context = {
                    'item': inv
                }
                return render(request, 'fichaArticulo.html', context)

    context = {
        'item': item
    }

    return render(request, 'fichaArticuloEdit.html', context)


def aceptarDes(request):
    item = Item.objects.all()

    if request.method == 'POST':
        for inv in item:
            if inv.id in request.POST:
                context = {
                    'item': inv
                }
                inv.description = request.POST['description']
                inv.save()
                return render(request, 'fichaArticulo.html', context)

    context = {
        'item': item
    }

    return render(request, 'fichaArticuloEdit.html', context)


def aceptarFoto(request):
    item = Item.objects.all()

    if request.method == 'POST':
        for inv in item:
            if inv.id in request.POST:
                context = {
                    'item': inv
                }
                inv.img = request.FILES.get('imgFile')
                inv.save()
                return render(request, 'fichaArticulo.html', context)

    context = {
        'item': item
    }

    return render(request, 'fichaArticuloEdit.html', context)

def aceptarEst(request):
    item = Item.objects.all()

    if request.method == 'POST':
        for inv in item:
            if inv.id in request.POST:
                context = {
                    'item': inv
                }
                inv.state = request.POST['state']
                inv.save()
                return render(request, 'fichaArticulo.html', context)

    context = {
        'item': item
    }

    return render(request, 'fichaArticuloEdit.html', context)

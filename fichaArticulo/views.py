from django.shortcuts import render, redirect

from .models import Item, FechaDeReserva
# Create your views here.


def fichaArticulo(request):
    item = Item.objects.all()

    context = {
        'item': item
    }

    if request.method == 'POST':
        for inv in item:
            idate = request.POST['idate']
            fdate = request.POST['fdate']
            itime = request.POST['itime']
            ftime = request.POST['ftime']
            fecha = FechaDeReserva(iDate=idate, fDate=fdate,iTime=itime , fTime=ftime)
            fecha.save()
            inv.save()
            inv.Reserva.add(fecha)
            inv.save()
        return redirect('/fichaArticulo/')

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

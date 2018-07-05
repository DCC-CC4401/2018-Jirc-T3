from django.shortcuts import render, get_object_or_404, redirect

from .models import Item
# Create your views here.


def fichaArticulo(request):
    item = Item.objects.all()

    context = {
        'item': item
    }

    if request.method == 'POST':
        name = request.POST['nombre']
        img = request.FILES.get('imgFile')
        it = Item(name=name, description="un articulo de prueba", state=1, img=img)
        it.save()
        return redirect('/fichaArticulo/')

    return render(request, 'fichaArticulo.html', context)

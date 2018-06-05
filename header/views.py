import django.shortcuts


def header(request):
    context = {}
    return django.shortcuts.render(request, 'header.html', context)

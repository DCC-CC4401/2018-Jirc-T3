from django.shortcuts import render, get_object_or_404, redirect


def header(request):
    context = {}
    return render(request, 'header.html', context)


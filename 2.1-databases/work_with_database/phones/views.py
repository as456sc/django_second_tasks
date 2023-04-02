from django.shortcuts import render, redirect

from phones.models import Phone




def index(request):
    return redirect('catalog')




def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get('sort')
    phones = Phone.objects.all()
    if sort_pages == 'low':
        phones = phones.order_by('price')
    elif sort_pages == 'high':
        phones = phones.order_by('-price')
    elif sort_pages == 'alph':
        phones = phones.order_by('name')
    context = {'phones': phones,
               }
    return render(request, template, context=context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug)
    context = {'phone': phone}
    return render(request, template, context=context)
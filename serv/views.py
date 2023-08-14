from django.shortcuts import render

# Create your views here.


def services(request):
    dict4 = {'services': 'active'}
    return render(request, 'serv/services.html', context=dict4)

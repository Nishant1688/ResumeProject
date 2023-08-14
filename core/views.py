from django.shortcuts import render

# Create your views here.



def home(request):
    dict1 = {'home': 'active'}
    return render(request, 'core/index.html', context=dict1)


def contact(request):
    dict2 = {'contact': 'active'}
    return render(request, 'core/contact.html', context=dict2)

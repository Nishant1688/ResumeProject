from django.shortcuts import render

# Create your views here.


def skill(request):
    dict3 = {'skill': 'active'}
    return render(request, 'edu/skill.html', context=dict3)

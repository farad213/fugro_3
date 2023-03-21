from django.shortcuts import render
from .models import Piles
from django.db.models import Q

def buildings(request):
    context = {}
    return render(request, "sisecam/buildings.html", context)

def ajax_buildings_select(request):
    partial_sorszam = str(request.GET["sorszam"])
    options = Piles.objects.filter(Q(sorszam__icontains=partial_sorszam)).order_by("sorszam")
    options = [option for option in options if not option.sorszam.isnumeric()]
    context = {"options": options}
    return render(request, "sisecam/ajax/buildings_select.html", context)

def ajax_buildings_calculate(request):
    sorszam = str(request.GET["sorszam"])
    select = request.GET["select"]
    try:
        if select:
            result = Piles.objects.get(pk=int(select))
        else:
            result = Piles.objects.get(sorszam=str(sorszam))
    except:
        result = "Érvénytelen sorszám"
    context = {"result": result}
    return render(request, "sisecam/ajax/buildings_calculate.html", context)
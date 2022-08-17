from pprint import pprint

from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv
from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    path = BUS_STATION_CSV

    with open(path, "r", encoding='utf-8') as f:
        bus_stations = list(csv.DictReader(f))

    paginator = Paginator(bus_stations, per_page=10)
    page_num = int(request.GET.get('page', 1))

    page = paginator.get_page(page_num)

    context = {
        'bus_stations': page,
        'page': page,
    }

    return render(request, 'stations/index.html', context)

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
    print(f'BUS_STATION_CSV: {BUS_STATION_CSV}')
    path = BUS_STATION_CSV
    bus_stations = list()

    with open(path, "r", encoding='utf-8') as f:
        CONTENT = csv.DictReader(f)
        for row in CONTENT:
            print(f"Name: {row['Name']}\t Street: {row['Street']}\tDistrict: {row['District']}\t")
            bus_stations.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})

    paginator = Paginator(bus_stations, 20)
    page_num = int(request.GET.get('page', 1))

    page = paginator.get_page(page_num)

    context = {
        'bus_stations': bus_stations,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

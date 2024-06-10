from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from .models import Link

def scrape(request):
    if request.method == 'POST':
        site = request.POST.get('site', '')
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')

        link_data = []

        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            link_data.append({'address': link_address, 'name': link_text})
            Link.objects.create(address=link_address, name=link_text)

        return HttpResponseRedirect('/')  # You might want to specify a different URL

    data = Link.objects.all()

    return render(request, 'myapp/result.html', {'data': data})



def clear(request):
    Link.objects.all().delete()
    return render(request, 'myapp/result.html')
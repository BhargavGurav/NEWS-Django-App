from django.shortcuts import render
import requests
# Create your views here.


# https://newsapi.org/v2/top-headlines?country=in&apiKey=475b20337c55407e939ec730ec2400a1 
def home(request):
    url = ('https://newsapi.org/v2/everything?q=politics&apiKey=475b20337c55407e939ec730ec2400a1')
    if request.method == 'GET':
        query = request.GET.get('query')
        url = (f'https://newsapi.org/v2/everything?q={query}&apiKey=475b20337c55407e939ec730ec2400a1')

    response = requests.get(url)
    dictionary = response.json()
    context = {}
    context['news'] = dictionary['articles']

    return render(request, 'base.html', context)

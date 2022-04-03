from django.shortcuts import render,redirect
import requests
# Create your views here. 
def home(request):
    
    if request.method == 'POST':
        city=request.POST['city']
        urls = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=0afba858d74acf07dcdb6993e6fbd8d4'
    
        w = requests.get(urls.format(city)).json()
        weather={
            'city':city,
            'temperature':w['main']['temp'],
            'description':w['weather'][0]['description'],
            'icon':w['weather'][0]['icon'],

        }
        
        data = {'weather':weather}
        return render(request,'index.html',data)
    else:
        urls = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=0afba858d74acf07dcdb6993e6fbd8d4'
        city='alaska'
        w = requests.get(urls.format(city)).json()
        weather={
            'city':city,
            'temperature':w['main']['temp'],
            'description':w['weather'][0]['description'],
            'icon':w['weather'][0]['icon'],

        }
        
        data = {'weather':weather}
        return render(request,'index.html',data)
         
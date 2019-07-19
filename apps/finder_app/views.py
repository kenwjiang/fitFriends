from django.shortcuts import render, HttpResponse, redirect
from apps.login_and_registration.models import User, Gym, Preference
import googlemaps
import pprint
import time
import json
import requests
from apps.finder_app.places import APIKey

API_KEY = APIKey.key
def index(request):
    return render(request, 'finder_app/index.html')

def dashboard(request):
    user = User.objects.get(id=request.session['user_id'])
    def_gym_id = user.def_gym.place_id
    context = {
    'def_gym_id': def_gym_id,
    }
    return render(request, 'finder_app/dashboard.html', context)

def finder(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    # defines client
    gmaps = googlemaps.Client(key = API_KEY)

    #define search
    places_result = gmaps.places_nearby(location='37.4323 , -121.8996', open_now = False, type = 'gym', radius= 10000)

    #loop through to find name, address, and lng lat
    gyms = {}
    for place in places_result['results']:
        new_gym = {place['name']: {
        'address': place['vicinity'],
        'geocode':place['geometry']['location'],
        'place_id':place['place_id'],
            }
        }
        gyms.update(new_gym)

    #creates json file from the gyms dict
    gyms_json = json.dumps(gyms)
    context = {
    'gyms': gyms_json,
    }

    return render(request, 'finder_app/finder.html', context)

def gym_page(request, place_id):
    if 'user_id' not in request.session:
        return redirect('/login')
    # search returns name and address of location using place id
    # returns object as json object
    fields = ['name', 'formatted_address']
    place_details = get_page_details(place_id, fields)
    place_json = json.dumps(place_details)

    #checks to see if the gym has been created as a location in database
    # if havent been created, then set into data base
    # else set this gym with matching gym id
    gym_list = Gym.objects.filter(place_id=place_id)
    count = 0
    for gym in gym_list:
        if place_id == gym.place_id:
            count+= 1
    if count == 0:
        this_gym = Gym.objects.create(place_id = place_id)
    else:
        this_gym = Gym.objects.filter(place_id=place_id)

    members = User.objects.filter(def_gym = this_gym)
    pref_info = Preference.objects.all().values()

    # if gym id and the default gym's place_id are the same, return true
    user = User.objects.get(id=request.session['user_id'])
    default = False
    if place_id == user.def_gym.place_id:
        default = True

    def_gym_id = user.def_gym.place_id
    context = {
    'name': place_details['result']['name'],
    'address': place_details['result']['formatted_address'],
    'place_id': place_id,
    'place': place_json,
    'default': default,
    'members': members,
    'pref_info': pref_info,
    'def_gym_id':def_gym_id,
    }
    return render(request, 'finder_app/gym_page.html', context)

def set_gym_default(request, place_id):
    user = User.objects.get(id=request.session['user_id'])
    this_gym = Gym.objects.filter(place_id=place_id)

    user.def_gym = this_gym[0]
    user.save()
    return redirect('/gym/'+ place_id)

def get_page_details(place_id, fields):
    # url to query for information from google
    endpoint_url = 'https://maps.googleapis.com/maps/api/place/details/json'

    # params to pass through to the URL
    params = {
    'placeid': place_id,
    'fields': ",".join(fields),
    'key': API_KEY,
    }

    #creates url for query combining api url and the parameters, returns a json object
    result = requests.get(endpoint_url,  params = params)
    place_details = json.loads(result.content)
    return place_details

def pref_form_page(request):
    if 'user_id' not in request.session:
        return redirect('/login')
    user = User.objects.get(id=request.session['user_id'])
    def_gym_id = user.def_gym.place_id
    context = {
    'def_gym_id': def_gym_id,
    }
    return render(request, 'finder_app/preference_form.html', context)

def pref_form_submit(request):
    user = User.objects.get(id=request.session['user_id'])
    category = ",".join(request.POST.getlist('categories'))
    monHour = 'Mon:' + request.POST['monTime']
    tuesHour = 'Tues:'+ request.POST['tuesTime']
    wedHour = 'Wed:' + request.POST['wedTime']
    thuHour= 'Thu:' + request.POST['thuTime']
    friHour = 'Fri:' + request.POST['friTime']
    satHour = 'Sat:' + request.POST['satTime']
    sunHour = 'Sun:' + request.POST['sunTime']
    schedule = ','.join([monHour, tuesHour, wedHour, thuHour, friHour, satHour, sunHour])
    print(schedule)

    user_pref =  Preference.objects.create(gender=request.POST['genderPref'], user_schedule=schedule, categories=category, userPref= user)


    return redirect('/preference')

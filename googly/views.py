from django.http import JsonResponse
from django.shortcuts import render
import requests

def place_search(request):
	key = "AIzaSyB8Jlmjo9zCmeOoQ1IqZYqrJmu1TAp9KrA"
	search="Starbucks"
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?key=%s&query=%s&region=kw"%(key, search)
	
	next_page_token = request.GET.get('next_page')
	if next_page_token:
		url+= "&pagetoken=%s"%(next_page_token)

	response = requests.get(url).json()
	context = {
	"response":response
	}

	return render(request, 'place_search.html', context)

# Create your views here.
def place_detail(request):
	key = "AIzaSyDGbT7kHUPQO9_Bk5z9LkBPIeTCCf-xPwk"
	place_id= request.GET.get('place_id')
	url = "https://maps.googleapis.com/maps/api/place/details/json?key=%s&placeid=%s"%(key, place_id)
	

	response = requests.get(url).json()
	context = {
	"response":response
	}

	return render(request, 'details.html', context)
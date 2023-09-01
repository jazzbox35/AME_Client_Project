#   Function:     Add and query level 1 propositions with the AbsoluteMode Engine (absolutemode.agiengine.online)
#   Input:        User propositions and associated keywords 
#   Output:       Server evaluation of proposition and submission of a case for training

#   This program and associated Django files is free to clone as desired

import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    # Submit a transaction to the server to create a new case upon invocation

    api_url = 'https://apr6.agiengine.online/createcase'

    headers = {
        'api-key': '00035' 
    }

    data = {}

    try:
        response = requests.put(api_url, headers=headers, json=data)
    except:
        return HttpResponse("Cannot communicate with AME server")
    data = response.json()
    case = data['case']
    message = data['message']

    next_action = 'input_terms'
    return render(request, "ame_client_app/home.html", {"data": data, "next_action": next_action})

def CreateL0(request):
  case = request.GET.get('case')
  proposition = request.GET.get('L0value')
  #appearance =  request.GET.get('appearance')
  data = {
    "case": case,
    "proposition" :  proposition,
    "appearance" :  "appearance",
    "level" : 0
  }
  return JsonResponse(data)

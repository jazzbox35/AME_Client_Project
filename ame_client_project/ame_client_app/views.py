#   Function:     Add and query level 1 propositions with the AbsoluteMode Engine (absolutemode.agiengine.online)
#   Input:        User propositions and associated keywords 
#   Output:       Server evaluation of proposition and submission of a case for training

#   This program and associated Django files is free to clone as desired

import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import logging

ame_api_key = '18574'
ame_node = 'part2'

logging.basicConfig(filename="ame_client_app.log",filemode='a',format='%(asctime)s:%(levelname)s:%(message)s',level=logging.INFO)

def index(request):
    # Submit a transaction to the server to create a new case upon invocation

    api_url = 'https://' + ame_node + '.agiengine.online/createcase'
    headers = {
        'api-key':  ame_api_key
    }
    data = {}
    try:
        response = requests.put(api_url, headers=headers, json=data)
    except:
        return HttpResponse("Cannot communicate with AME server")
    data = response.json()
    logging.info("Create case>" + str(data) + " status>" + str(response.status_code))
    
    next_action = 'input_terms'
    return render(request, "ame_client_app/home.html", {"data": data, "next_action": next_action})

def CreateL0(request):
    # Create level 0, system 1 judgment(s) and post to the server
    case = request.GET.get('case')
    proposition = request.GET.get('L0value')
    appearance = request.GET.get('L0appear')
    api_url = 'https://' + ame_node + '.agiengine.online/sys1-proposition'
    headers = {
          'api-key':  ame_api_key
      }
    if len(appearance) == 0:
        appearance = "NIL"
    data = {
      "case": int(case),
      "proposition" :  proposition,
      "appearance"  :  appearance,
      "essence"     : "",
      "level"       : 0
    }
    try:
        response = requests.put(api_url, headers=headers, json=data)
    except:
        return HttpResponse("Cannot communicate with AME server")
    data = response.json()
    logging.info("L0 proposition>" + str(data) + " status>" + str(response.status_code))
    return JsonResponse(data)

def CreateL1(request):
    # Create level 1, system 1 judgment(s) and post to the server
    case = request.GET.get('case')
    proposition = request.GET.get('L1value')
    api_url = 'https://' + ame_node + '.agiengine.online/sys1-proposition'
    headers = {
          'api-key':  ame_api_key
      }
    #appearance =  request.GET.get('appearance')
    data = {
      "case": int(case),
      "proposition" :  proposition,
      "appearance"  :  "",
      "essence"     :  "",
      "level"       :  1
    }
    
    try:
        response = requests.put(api_url, headers=headers, json=data)
    except:
        return HttpResponse("Cannot communicate with AME server")
    data = response.json()
    logging.info("L1 S1 proposition>" + str(data) + " status>" + str(response.status_code))
    return JsonResponse(data)

def CreateL2(request):
    # Create level 1, system 2 judgment(s) and post to the server
    case = request.GET.get('case')
    proposition = request.GET.get('L1value')
    desired = request.GET.get('L1Desired')
    api_url = 'https://' + ame_node + '.agiengine.online/sys2-proposition'
    headers = {
          'api-key':  ame_api_key
      }
    #appearance =  request.GET.get('appearance')
    data = {
      "case": int(case),
      "proposition" :  proposition,
      "desired"     :  desired,
      "appearance"  :  "",
      "essence"     :  "",
      "level"       :  1
    }
    
    try:
        response = requests.put(api_url, headers=headers, json=data)
    except:
        return HttpResponse("Cannot communicate with AME server")
    data = response.json()
    logging.info("L1 S2 proposition>" + str(data) + " status>" + str(response.status_code))
    return JsonResponse(data)

def CreateL3(request):
    # Create level 1, system 2 judgment(s) and post to the server
    case = request.GET.get('case')
    api_url = 'https://' + ame_node + '.agiengine.online/sys2-realistic'
    headers = {
          'api-key':  ame_api_key
      }
    #appearance =  request.GET.get('appearance')
    data = {
      "case": int(case),
    }
    
    try:
        response = requests.put(api_url, headers=headers, json=data)
    except:
        return HttpResponse("Cannot communicate with AME server")
    data = response.json()
    logging.info("realistic call>" + str(data) + " status>" + str(response.status_code))
    return JsonResponse(data)

def CreateL4(request):
    # Retract the most recent proposition
    case = request.GET.get('case')
    api_url = 'https://' + ame_node + '.agiengine.online/retract_that'
    headers = {
          'api-key':  ame_api_key
      }
    #appearance =  request.GET.get('appearance')
    data = {
      "case": int(case),
    }
    
    try:
        response = requests.put(api_url, headers=headers, json=data)
    except:
        return HttpResponse("Cannot communicate with AME server")
    data = response.json()
    logging.info("retract that>" + str(data) + " status>" + str(response.status_code))
    return JsonResponse(data)

def CreateL5(request):
    # Mark case for training -- but no further updates allowed
    case = request.GET.get('case')
    api_url = 'https://' + ame_node + '.agiengine.online/traincase'
    headers = {
          'api-key':  ame_api_key
      }
    #appearance =  request.GET.get('appearance')
    data = {
      "case": int(case),
    }
    
    try:
        response = requests.put(api_url, headers=headers, json=data)
    except:
        return HttpResponse("Cannot communicate with AME server")
    data = response.json()
    logging.info("train case>" + str(data) + " status>" + str(response.status_code))
    return JsonResponse(data)

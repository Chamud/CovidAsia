from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import countryCases
import sys
import json



# Create your views here.

def home(request):
	return HttpResponse('Append "/cases/" to the URL')

def cases(request):
	allModels = countryCases.objects.all()
	countryName = []
	confirmed = []
	recovered = []
	deaths = []
	updated = []
	case = '{'
	i=0
	for each in allModels:
		countryName.append(f"{each.country}")
		confirmed.append(f"{each.confirmed}")
		recovered.append(f"{each.recovered}")
		deaths.append(f"{each.deaths}")
		updated.append(f"{each.updated}")
		if i!=0:
			case+=","
		case += '''
				"'''+countryName[i]+'''":{ "All": { "confirmed": '''+confirmed[i]+''', "recovered": '''+recovered[i]+''',"deaths": '''+deaths[i]+''',"updated": "'''+updated[i]+'''"} } 
		'''
		i+=1
	case+='}'
	jcase = json.loads(case)
	return JsonResponse(jcase)
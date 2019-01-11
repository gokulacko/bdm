from django.shortcuts import render
from rest_framework import viewsets

# from rest_framework.generics import ListAPIView, CreateAPIView, GenericAPIView
from .serializers import LeadSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import requests
from requests.auth import HTTPBasicAuth


# Create your views here.

class LeadViewSet(APIView):
    serializer_class = LeadSerializer

    def post(self, request, format=None):
        serializer = LeadSerializer(data=request.data)
    
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
        if serializer.is_valid():
            
            serializer.save()
            # print("ser",serializer.data["Phone"])
            data = serializer.data
            lead = dict()
            lead1 = dict()
            lead2 = dict()
            lead3 = dict()
            total = list()
            lead["Attribute"] = "FirstName"
            lead["Value"] = data["FirstName"]
            total.append(lead)
            lead1["Attribute"] = "Phone"
            lead1["Value"] = int(data["Phone"])
            total.append(lead1)
            lead2["Attribute"] = "mx_City"
            lead2["Value"] = data["mx_city"]
            total.append(lead2)
            lead3["Attribute"] = "mx_Model"
            lead3["Value"] = data["mx_Model"]
            total.append(lead3)

            json_data = json.dumps(total)
            headers = {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials" : "true",
                "Access-Control-Allow-Headers": "Access-Control-Allow-Origin",
            }
                

            r = requests.post('https://api-in21.leadsquared.com/v2/LeadManagement.svc/Lead.Capture?accessKey=u$rbeb1b5a0cd1fb8b7fb0affd7ae64f6cd&secretKey=d188eff5cc646a031365ac62f378808c0dc9beaa', auth=('t1@gmail.com', 'Ackodrive@12'), headers=headers, data=json_data)
            r = json.loads(r.text)
            print(r)
            
            # json_data = json.dumps(total)
            # headers = {
            # 'Content-Type': 'application/json',
            # "Access-Control-Allow-Origin": "*",
            # "Access-Control-Allow-Credentials" : "true",
            # "Access-Control-Allow-Headers": "Access-Control-Allow-Origin",
            # }
            

            # r = requests.post('https://api-in21.leadsquared.com/v2/LeadManagement.svc/Lead.Capture?accessKey=u$rbeb1b5a0cd1fb8b7fb0affd7ae64f6cd&secretKey=d188eff5cc646a031365ac62f378808c0dc9beaa', auth=('t1@gmail.com', 'Ackodrive@12'), headers=headers, data=json_data)
            # r = json.loads(r.text)
            # print(r)
            
            # json_data = JSONRenderer().render(total)
            # print(json_data)
            return Response(r)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


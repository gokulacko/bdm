from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
import json
import requests
from requests.auth import HTTPBasicAuth


class LeadSerializer(serializers.Serializer):
    FirstName = serializers.CharField(max_length=100)
    Phone = serializers.CharField(max_length=10)
    mx_city = serializers.CharField(max_length=100)
    mx_Model = serializers.CharField(max_length=100)

    def create(self, validated_data):
        
        data = validated_data
        # payload = [
        #        {
        #            "Attribute": "FirstName",
        #            "Value": data["FirstName"]
        #        },
        #        {
        #            "Attribute": "Phone",
        #            "Value": int(data["Phone"])
        #        },
        #        {
        #            "Attribute": "mx_City",
        #            "Value": data["mx_city"]
        #        },
        #        {
        #            "Attribute": "mx_Model",
        #            "Value": data["mx_Model"]
        #        }
        #    ]
          
        # lead = dict()
        # lead1 = dict()
        # lead2 = dict()
        # lead3 = dict()
        # total = list()
        # lead["Attribute"] = "FirstName"
        # lead["Value"] = data["FirstName"]
        # total.append(lead)
        
       
        # # print(total)
        # lead1["Attribute"] = "Phone"
        # lead1["Value"] = int(data["Phone"])
        # total.append(lead1)
        
        # lead2["Attribute"] = "mx_city"
        # lead2["Value"] = data["mx_city"]
        # total.append(lead2)

        # lead3["Attribute"] = "mx_Model"
        # lead3["Value"] = data["mx_Model"]
        # total.append(lead3)
        
        # # json_data = serializers.serialize('json', total)
        
        # json_data = json.dumps(total)
        # headers = {
        #     'Content-Type': 'application/json',
        #     "Access-Control-Allow-Origin": "*",
        #     "Access-Control-Allow-Credentials" : "true",
        #     "Access-Control-Allow-Headers": "Access-Control-Allow-Origin",
        # }
            

        # r = requests.post('https://api-in21.leadsquared.com/v2/LeadManagement.svc/Lead.Capture?accessKey=u$rbeb1b5a0cd1fb8b7fb0affd7ae64f6cd&secretKey=d188eff5cc646a031365ac62f378808c0dc9beaa', auth=('t1@gmail.com', 'Ackodrive@12'), headers=headers, data=json_data)
        # r = json.loads(r.text)
        # print(r)
        
        return validated_data

   
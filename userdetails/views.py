from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import User
from .serializer import UserSerializer
import requests
import json


# Create your views here.


@api_view(['POST'])
def RegisterUser(request):

    phone_number = request.data['phone_number']
    pin_code = request.data['pin_code']

    # check if user already exists
    check_invalid_user = User.objects.filter(phone_number=phone_number).first()

    # if user doesn't exist
    if not check_invalid_user:
        try:
            # get pincode details from another microservice
            url = 'http://127.0.0.1:8001/getdetails/details'
            data = {'pin_code': pin_code}
            response = requests.get(url, data=data)

            # raise exception if status code received from "Pincode" microservice is not 200
            response.raise_for_status()

            # filter out city and state from response
            data = json.loads(response.text)
            request.data.update({"state": data['state']})
            request.data.update({"city": data['city']})

            # create a serializer object to save the user data
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            result = json.dumps(request.data)
            return HttpResponse(result)
        except requests.exceptions.RequestException as e:
            return HttpResponse(f"Error: {str(e)}", status=500)

    else:
        return Response("User Already Exists")

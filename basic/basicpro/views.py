# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import viewsets,response
import json
from .models import *
from .serializers import *
from django.http import HttpResponse
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas
from rest_framework_swagger.views import get_swagger_view
# Create your views here.
'''
class SignUpViewset(viewsets.ModelViewSet):
    queryset = Signup.objects.all()
    serializer_class = SignUpSerializer
    #def create(self,request,*args,**kwrgs):
        #serializer = SignUpSerializer(data=request.data)
        #if serializer.is_valid():
            #request_ob = serializer.save()
            #return HttpResponse("sucess")
        #else:
            #return HttpResponse("validation wrong")
'''
class SignUpViewSet(viewsets.ViewSet):
    def create(self, request):
        data = request.data
        first_name = data['first_name']
        email = data['email']

        newnumber = ContactNumber.objects.create(number=data['number'])
        signobj = Signup.objects.create(first_name=first_name, email=email, number=newnumber)
        print signobj
        if 'last_name' in data:
            signobj.last_name = data['last_name']
        if 'dob' in data:
            signobj.dob = data['dob']
        signobj.save()
        return response.Response("sucess")
    def list(self,request):
         sign = Signup.objects.all()
         sign_serializer = SignUpSerializer(sign, many=True)
         return response.Response(sign_serializer.data)

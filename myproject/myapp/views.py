from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
from .models import studentModel
from .serializers import studentSerializer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.renderers import JSONRenderer


# Create your views here.

class all_data(View):
    
    def get(self,request):
        stu = studentModel.objects.all()
        serialized_stu = studentSerializer(stu,many=True)
        return JsonResponse(serialized_stu.data,safe=False)

    def post(self,request):
        pass

class stu_data(View):
    
    def get(self,request,pk):
        # if pk not in 
        stu = studentModel.objects.get(id=pk)
        serialized_stu = studentSerializer(stu,many=False)
        return JsonResponse(serialized_stu.data,safe=False)

    def post(self,request):
        pass

class home(View):
    
    def get(self,request):
        return HttpResponse('Home Page')

    def post(self,request):
        pass


# class create(View):

#     def get(self,request):
#         pass

@csrf_exempt
def create_data(request,pk):
            print('you are in post of create')
            json_data = json.dumps(pk)
            json_data = str.encode(json_data)
            print(type(json_data))
            # json_data = request.body
            # json_data = pk
            stream = io.BytesIO(json_data)
            python_data = JSONParser().parse(stream)
            serializer = studentSerializer(data=python_data)
            serializer = dict(serializer)
            print(serializer)
            print(type(serializer))
            if serializer.is_valid():
                serializer.save()
                resp = {'msg':'Record Created !!!'}
                return JsonResponse(resp,safe=False)
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type = 'application/json')
        





from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TodoSerializer
# Create your views here.

@api_view(['GET', 'POST', 'PATCH'])
def home(request):
    if request.method == 'POST':
        return  Response({
            
            'status': 200,
            "messsage":'POst data'
        })
    elif request.method == 'GET':
        return  Response({
            
            'status': 200,
            "messsage":'GET data'
        })
    elif request.method == 'PATCH':
        return  Response({
            
            'status': 200,
            "messsage":'PATCH data'
        })
    else:
        return  Response({
            
            'status': 404,
            "messsage":'invalid  Method'
        })
        
        
        
        
@api_view(['POST'])
def post_todo(request):
    try:
        data= request.data
        serializer=TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return  Response({
            
            'status': 200,
            "messsage":'data saved'
        })
        else:
            return  Response({
            
            'status': 404,
            "messsage":'ops you skip something'
        })
            


    except Exception as e:
        print(e)
    

"vaidate and advaced serializer concept"

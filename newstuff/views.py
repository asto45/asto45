from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response 
from rest_framework.views import APIView


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "slackUsername": 'Seun Amos',
            "backend": True,
            "age": 25, 
            "bio": 'I am a zealous and diligent individual. i love the programming world.' ,
        }
        return Response(data)

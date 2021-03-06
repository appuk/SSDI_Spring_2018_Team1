from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from rest_framework.decorators import api_view

from beton.models import Userinfo
from beton.serializers import PostSerializer
from rest_framework.renderers import JSONRenderer
from django.core import serializers
# Create your views here.


def Dbtest(request):
    users = Userinfo.objects.all()
    if users.count() > 0:
        return render_to_response('userinfo.html',{'users':users})

@api_view(['GET'])
def post_collection(request):
    if request.method == 'GET':
        posts = Userinfo.objects.all()
        json_data = serializers.serialize('json', posts)
        return HttpResponse(json_data, content_type="application/json")


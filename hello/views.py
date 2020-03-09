import os

from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from hello.models import Party
from hello.serializer import PartySerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    rest_list = Party.objects.order_by('-dateTime')
    serializer = PartySerializer(rest_list, many=True)
    return JsonResponse(serializer.data, safe=False)



'''
# Rest api end point
def get_rest_list(request):
    """
    Returns Json list of all restaurants
    """
    if request.method == "GET":
        rest_list = Party.objects.order_by('-dateTime')
        serializer = PartySerializer(rest_list, many=True)
        return JsonResponse(serializer.data, safe=False)
'''

def db(request):

    party = Party()
    party.save()

    parties = Party.objects.all()

    return render(request, "db.html", {"parties": parties})

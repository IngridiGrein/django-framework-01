from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def index(request):
    html= """<html>
        <head>
        </head>
        <body>
         <h1><marquee><font-size="20px">Hello World!</marquee></h1>
        </body>    
    </html>"""
   

    return HttpResponse(html)

def hora(request):
    html= """<html>
        <head>
        </head>
        <body>
         <h1>%s</h1>
        </body>    
    </html>"""% datetime.now()

    return HttpResponse(html)
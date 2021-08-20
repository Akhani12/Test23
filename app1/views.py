from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app1.models import Video


def Home(request):
    list_data = list(Video.objects.values('desc', 'image', 'links'))
    print(list_data)

    context = {"video_data":list_data}

    return render(request, "portfolio.html", context=context)

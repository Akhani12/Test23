from django.shortcuts import render
from app1.models import Video


def Home(request):
    list_data = list(Video.objects.values('desc', 'image', 'links'))
    print(list_data)
    context = {"video_data":list_data}
    return render(request, "portfolio.html", context=context)

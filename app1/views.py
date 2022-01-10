from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from app1.models import Video


class Home(TemplateView):
    def get(self, request, **kwargs):
        list_data = list(Video.objects.values('desc', 'image','code'))
        print(list_data)
        context = {"video_data": list_data}
        return render(request, "portfolio.html", context=context)

    def post(self, request, **kwargs):
        email = request.POST.get("email")
        code = request.POST.get("code")
        messages.info(request,"Successfully subscribe it.")

        print(email)
        return redirect("/home/")


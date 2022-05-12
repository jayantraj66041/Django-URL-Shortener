from django.shortcuts import render, redirect
from django.views import View
from api.models import UrlManage

# Create your views here.
class UrlShortView(View):
    def get(self, request):
        return render(request, 'home.html')
    

class LongUrlView(View):
    def get(self, request, token):
        try:
            url = UrlManage.objects.get(short_url=token).url
        except DoesNotExist:
            pass
        return redirect(url)

class AboutUs(View):
    def get(self, request):
        return render(request, 'about.html')
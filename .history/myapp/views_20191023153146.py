from django.shortcuts import render

# Create your views here.
from .models import Service

# Create your views here.
def services(req):
    if req.method == 'POST':
        post = req.POST
        s = Service()
        s.icon = post['icon']
        s.title = post['title']
        s.detail = post['detail']
        s.save()
        services = Service.objects.all()
        print(services)
        return render(req, 'linuxapp/services.html', { 'services': services })
    else:
        print('ร้องขอทำมะดา')
        services = Service.objects.all()
        print(services)
        return render(req, 'linuxapp/services.html', { 'services': services })
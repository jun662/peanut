from django.shortcuts import render
import re
from user.models import PeanutInfo
# Create your views here.
def register(request):
    return render (request,'index.html')

def rpost(request):
    if request.method=='POST':
        user_name = request.POST.get('username')
        pd = request.POST.get('password')
        pwds = request.POST.get('pwd')
        emails = request.POST.get('email')
        if not all([user_name,pd,pwds,emails]):
            return render (request,'index.html')
        if not re.match(r'^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$',emails):
            return render(request,'index.html')
        if not re.match(r'^\w{8,16}$',pd):
            return render(request,'index.html')
        if not re.match(r'^\w{8,16}$',pwds):
            return render(request,'index.html')
        if not re.match(r'^[a-zA-Z][a-zA-Z0-9]{3,15}$',user_name):
            return render(request,'index.html')
        user=PeanutInfo.objects.create_user(username=user_name,email=emails,password=pd)
        user.is_active
        user.save()
        return render(request,'index.html')
        


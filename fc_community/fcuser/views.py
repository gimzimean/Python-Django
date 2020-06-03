from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import Fcuser

# Create your views here.


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')  # 이미 templates 폴더를 바라보고 있슴
    elif request.method == "POST":
        useremail = request.POST.get('useremail', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}
        if not(username and useremail and password and re_password):
            res_data['error'] = '모든항목을 입력해야합니다..'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            fcuser = Fcuser(
                useremail=useremail,
                username=username,
                password=make_password(password)
            )
            fcuser.save()
        # 이미 templates 폴더를 바라보고 있슴
        return render(request, 'register.html', res_data)

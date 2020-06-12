from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Fcuser
from .forms import LoginForm

# Create your views here.


# def home(request):
#     user_id = request.session.get('user')
#     print("userId", user_id)
#     if user_id:
#         fcuser = Fcuser.objects.get(pk=user_id)
#         return HttpResponse(fcuser.username)
#     return HttpResponse('home')

def home(request):
    return render(request, 'home.html')


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # 세션체크
            request.session['user'] = form.user_id
            return redirect("/")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# def login(request):
#     if request.method == "GET":
#         return render(request, 'login.html')  # 이미 templates 폴더를 바라보고 있슴
#     elif request.method == "POST":
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)

#         res_data = {}
#         if not (username and password):
#             res_data['error'] = '모든 값을 입력해야합니다.'
#         else:
#             fcuser = Fcuser.objects.get(username=username)
#             if check_password(password, fcuser.password):
#                 # 비밀번호 일치 ,로그인 처리
#                 # 세션
#                 request.session['user'] = fcuser.id  # 딕셔너리 user 키에 id값을 넣음
#                 # redirect
#                 return redirect('/')
#             else:
#                 res_data['error'] = '비밀번호가 틀렸습니다.'
#         return render(request, 'login.html', res_data)


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

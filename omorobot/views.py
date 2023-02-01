from django.shortcuts import render
from .models import User, Mycar, MycarAll
from django.http import HttpResponseRedirect
from django.urls import reverse
import sqlite3
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


context = {
            "joinmessage" : "",
            "message" : "",
            }


###
#  인덱스 페이지 관련
#  렌더사항
###

# main index페이지 보여주기
def index(request):
    mycar = Mycar.objects.all()
    global context
    context = {
        "joinmessage" : "",
        "message" : "",
        "mycars": mycar
    }
    return render(request, "index.html", context)


# 회원별 index페이지 보여주기
def user(request, pk) :
    mycar = Mycar.objects.all()
    old_user = User.objects.get(user_name=f"{pk}")
    username = old_user.user_name
    context = {
        "user_name" : username,
        "mycars" : mycar,
    }
    return render(request, "index.html", context)



###
#  회원가입 페이지 관련
#  렌더 상황
###

#회원가입
def join(request) :
    return render(request, "join.html", context)

# 회원가입로직
def create_user(request) :
    global context
    if request.method == "POST":
        join_username = request.POST.get("username")
        join_password = request.POST.get("password")
        join_confirm = request.POST.get("password_confirm")

        # 빈칸 확인
        if join_username == "" :
            context = {
                "message" : "ID를 입력하세요"
            }
            return HttpResponseRedirect(reverse("omorobot:join"))
        # 중복아이디 확인
        elif User.objects.filter(user_name = f"{join_username}").exists() :
            context = {
                "message" : "중복id가있다."
            }
            return HttpResponseRedirect(reverse("omorobot:join"))  
        else :
            # 암호 빈칸확인
            if join_password == "" :
                context = {
                    "message" : "PW가 비어있습니다"
                }
                return HttpResponseRedirect(reverse("omorobot:join"))
            # 암호가 같은지 확인
            # 같으면 로그인 된 회원페이지로 이동
            else :
                if join_password == join_confirm :
                    new_user = User()
                    new_user.user_name = join_username
                    new_user.user_password = join_password
                    new_user.save()
                    return HttpResponseRedirect(f"/{join_username}")
                else : 
                    context ={
                        "message" : "비밀번호 확인하세요"
                    }
                    return HttpResponseRedirect(reverse("omorobot:join"))
    else :
        return render(request, "join.html", context)


###
#  로그인 페이지 관련
#  렌더 상황
###

# 로그인페이지
def login(request) :
    return render(request, "login.html", context)

# 로그인 로직
def enterlogin(request) :
    global context
    if request.method == "POST":
        login_username = request.POST.get("username")
        login_password = request.POST.get("password")

        # 빈칸 확인
        if login_username == "" :
            context = {
                "message" : "ID를 입력하세요"
            }
            return HttpResponseRedirect(reverse("omorobot:login"))
                
        else :
            # 암호 빈칸확인
            if login_password == "" :
                context = {
                    "message" : "PW가 비어있습니다"
                }
                return HttpResponseRedirect(reverse("omorobot:login"))
            # 같으면 로그인 된 회원페이지로 이동
            else :
                if User.objects.filter(user_name = f"{login_username}").exists() :
                    old_user = User.objects.get(user_name = f"{login_username}")
                    user_password = old_user.user_password
                    if user_password != login_password :
                        context ={
                            "message" : "비밀번호 확인하세요"
                        }
                        return HttpResponseRedirect(reverse("omorobot:login"))
                    else : 
                        return HttpResponseRedirect(f"/{login_username}/")
                else : 
                    context ={
                        "message" : "아이디가 없습니다"
                        }
                    return HttpResponseRedirect(reverse("omorobot:login"))                    
    else :
        return render(request, "login.html", context)



###
#  mycar 관련 데이터 제공 1개씩
#  추출해서 저장하기
###

# 한개씩 만들기
def create_mycar(request, pk):
    if request.method == "POST" :
        mycarseletor = request.POST.get("mycarselector")
        number = request.POST.get("number")
        new_mycar = Mycar()
        old_user = User.objects.get(user_name=f"{pk}")
        new_mycar.user_name = old_user

        if mycarseletor == "speed" :
            new_mycar.mycar_speed = int(number)
        elif mycarseletor == "battery":
            new_mycar.mycar_battery = int(number)
        else:
            new_mycar.mycar_color = number
        new_mycar.save()
        return HttpResponseRedirect(f"/{pk}")




###
#  mycar 관련 데이터 제공 여러개
#  추출해서 저장하기
###

def create_mycarset(request, pk):
  if request.method == "POST" : 
    mycar_speed = request.POST.get("speed")
    mycar_battery = request.POST.get("battery")
    mycar_color = request.POST.get("color")
    
    new_mycar = Mycar()
    old_user = User.objects.get(user_name=f"{pk}")

    new_mycar.user_name = old_user
    new_mycar.mycar_speed = int(mycar_speed)
    new_mycar.mycar_battery = int(mycar_battery)
    new_mycar.mycar_color = mycar_color
    new_mycar.save()
    return HttpResponseRedirect(f"/{pk}")

# 한개씩 삭제
def delete_mycar(request, pk, fk):
    mycar = Mycar.objects.filter(user_name=fk)
    del_mycar = mycar.filter(pk = pk)
    del_mycar.delete()
    return HttpResponseRedirect(f"/{fk}")



###
#  차트용 mycar 관련 데이터 제공
#  추출해서 저장하기
###

def create_mycarall(request, pk) :
  if request.method == "POST" : 
    mycar_speed = request.POST.get("speed")
    mycar_battery = request.POST.get("battery")
    mycar_color = request.POST.get("color")
    mycar_encoder_or = request.POST.get("encoder_or")
    mycar_encoder_ac = request.POST.get("encoder_ac")
    check_time = request.POST.get("check_time")

    new_mycar = MycarAll()
    old_user = User.objects.get(user_name=f"{pk}")
    new_mycar.user_name = old_user

    new_mycar.mycar_speed = int(mycar_speed)
    new_mycar.mycar_battery = int(mycar_battery)
    new_mycar.mycar_color = mycar_color
    new_mycar.mycar_encoder_or = int(mycar_encoder_or)
    new_mycar.mycar_encoder_ac = int(mycar_encoder_ac)
    new_mycar.check_time = int(check_time)
    new_mycar.save()
    return HttpResponseRedirect(f"/{pk}")


def delete_allmycar(request, pk, fk):
    mycar = MycarAll.objects.filter(user_name=fk)
    del_mycar = mycar.filter(pk = pk)
    del_mycar.delete()
    return HttpResponseRedirect(f"/{fk}")




###
#  기타 데이터 제공 관련 컨트롤러
#  추출해서 저장하기
###




@csrf_exempt
def chart(request):
    if request.method=="POST":
        data =json.loads(request.body)
        print("들어온 데이터 : ", data)
       
        print(data["speed"], data["encoder"])

        qs = MycarAll.objects.filter(mycar_speed=data["speed"], mycar_encoder_or=data["encoder"])

        ac_dict = {}
        i = 0
        for s in qs: 
            ac_dict[i] = s.mycar_encoder_ac
            i += 1

        i =5 
        for b in qs:
            ac_dict[i] = b.mycar_battery
            i += 1
        
        i =10
        for e in qs:
            ac_dict[i] = e.mycar_encoder_or
            i += 1
        
        i =15
        for c in qs:
            ac_dict[i] = c.mycar_color
            i += 1
        
        ac_dict['length'] = i

        return JsonResponse(ac_dict)
        
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from blog import models
import datetime



def index(request):
    try:

        name=request.session['user_name']
    except:
        return redirect('/login/')


    return render(request, 'index.html', {'username': name})


def foodlist(request):
    name=request.session['user_name']
    food_list=models.RestaurantInfo.objects.all()

    return render(request, 'foodlist.html', {'food_list':food_list})

def review(request):
    res_id=request.GET.get('id')
    try:
        id=int(res_id)
    except:
        id=1
    res_inf = models.RestaurantInfo.objects.get(id=id)
    res_review=models.Review.objects.filter(res_id=res_id)
    r=[]
    k=[]
    for i in res_review:
        if i.is_sub=='f':
            r.append(i)
        else:
            k.append(i)
    r.reverse()
    return render(request, 'review.html',{'res_inf':res_inf,'review1':r,'review2':k})


def writereview(request):
    
    if request.method == "GET":
        res_id=request.GET.get('res_id')
        try:
            id=int(res_id)
        except:
            id=1
        res_inf = models.RestaurantInfo.objects.get(id=id)
        sub_id=request.GET.get('id')
        if sub_id is None:
            sub_id=0

        return render(request, 'writereview.html',{'res_inf':res_inf,'subid':sub_id})
    else:
        res_id=request.GET.get('res_id')

        try:
             scontent=request.POST.get('scontent')
        except:
             scontent='None'

        try:
            content=request.POST.get('content')
        except:
            content='None'


        try:
            name=request.session['user_name']
        except:
            name='111'
        start='5'
        is_sub='t'
        try:
            subid=request.GET.get('subid')
            subid=int(subid)
            is_sub='t'
            if subid==0:
                is_sub='f'
        except:
            subid=0
            is_sub='f'

        db=models.Review()
        db.name=name
        db.scontent=scontent
        db.content=content
        db.start=start
        db.time=datetime.datetime.now().strftime('%m-%d')
        db.subid=subid
        db.is_sub=is_sub
        db.res_id=res_id
        db.save()


        return redirect('/review.html?id='+res_id)



def login(request):
    
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        message = "Please enter your username and password        default username:111 password:2222"
        if username and password:  
            username = username.strip()
            try:
                user = models.UserInfo.objects.get(username=username)
                if user.password == password:

                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return redirect('/index/')
                else:
                    message = "Incorrect Password"
            except:
                message = "Incorrect username"
        return render(request, 'login.html', {"message": message})

    else:
        return render(request, 'login.html')


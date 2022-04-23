from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import karbaruser
from django.contrib.auth.models import User
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.core.mail import send_mail
from indexpage.models import footerdb



def register(request):
    homepageshow = 1
    footerdbs = footerdb.objects.all()
    context = {
        'homepageshow' :homepageshow ,
        'footerdbs' :footerdbs ,
        
    }
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tell = request.POST['tell']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password == password2:
                if karbaruser.objects.filter(email=email).exists():
                    messages.error(request, 'ایمیل تکراری است')
                    return redirect('register')
                else:
                   karbaruser11 = karbaruser.objects.create(username=email, email=email, first_name=first_name, last_name=last_name, tell=tell,)
                   user = User.objects.create_user(username=email, email=email, first_name=first_name, last_name=last_name, password=password,)
                   karbaruser11.save()
                   user.save()

                #    send_mail(
                #         'wowweb.ir/ (register) Do not Replay',
                #         'first name: '+str(first_name) +'\n'+'\n'+ 'last name: '+str(last_name) +'\n'+'\n'+'user email: '+str(email)+'\n'+'\n'+'tell: '+str(tell),
                #         'message_email',
                #         ['rezahoseini.ng@gmail.com','mirhadi410@gmail.com','mirhadi651@gmail.com',email],
                #         )


                   messages.success(request, 'ثبت نام شما با موفقیت انجام شد')
                   return redirect('login')
        else:
            messages.error(request, 'پسورد اول و دوم با هم مطابقت ندارد')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html',context)


def login(request):
    homepageshow = 1
    footerdbs = footerdb.objects.all()
    context = {
        'homepageshow' :homepageshow ,
        'footerdbs' :footerdbs ,
        
    }
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       user = auth.authenticate(username=username, password=password)
       if user is not None:
           auth.login(request, user)
           messages.success(request, 'شما به سیستم وارد شدید')
           return redirect('index')
       else:
            messages.error(
                request, 'مشخصات کاربری اشتباه است لطفا دوباره امتحان کنید')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html',context)

        
def logout(request):
    if request.method == 'POST':
         auth.logout(request,)
         messages.success(request, 'شما از سیستم خارج شدید')
         return redirect('index')
    return render(request, 'accounts/register.html')




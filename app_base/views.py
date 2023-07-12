from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    title = 'Login'
    print(request.GET.get('next'))
    if request.method == 'POST':
        url = '/'
        try:
            url_aux = str(request.META.get('HTTP_REFERER'))
            if url_aux.count('next'):
                url = url_aux.split('next=/')
                url = '/' + str(url[1])
        except:
            pass
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect(url)
        else:
            msg = 'Usuário ou senha incorreto!'
            return render(request, 'app_base/login.html', locals())
    return render(request, 'app_base/login.html', locals())


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


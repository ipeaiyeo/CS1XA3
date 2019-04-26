from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'tapp/login.html')

def sessionIncrease(request):
  index = request.session.get('counter',0)
  request.session['counter'] = index+1

  return HttpResponse("Counter= " + str(request.session['counter']))

def sessionGet(request):
  #increase = request.session.get('counter',0)
  return HttpResponse("Counter =" + str(request.session['counter']))

def userAdd(request):
    json_req = json.loads(request.body)
    uName = json_req.get('username','')
    pword = json_req.get('password','')

    if uName != '':
        user = User.objects.create_user(username=uName,
                                        pasword=pword)

        login(request,user)
        return HttpResponse('Logged In')

    else:
        return HttpResponse('Logged Out')

def loggedUser(request):
    json_req = json.loads(request.body)
    uName = json_req.get('username','')
    pword = json_req.get('password','')

    user = authenticate(request,username=uName,password=pword)
    if user is not None:
        login(request,user)
        return HttpResponse('Logged In')
    else:
        return HttpResponse('Login Failed')

def usersInfo(request):
    if not request.user.is_authenticated:
        return HttpResponse("Logged Out")
    else:
        return HttpResponse("Welcome back " + request.user.first_name)

def authOnly(request):
    user = request.user
    if user.is_authenticated:
        HttpResponse("Authenticated User Information")

from django.shortcuts import render
import os
import pykeepass as kp

# Create your views here.
db=""
def home(request):
    message=""
    if os.path.isfile('password_db.kdbx'):
        if request.method == "POST":
            pass1=request.POST.get('pass')
            try:
                global db
                db=kp.PyKeePass('password_db.kdbx',password=pass1)
            except kp.exceptions.CredentialsError:
                message="Incorrect Password"
            else :
                print("login success")
                print(db)

        return render(request,'unlock.html',{'message':message})
    else:
        os.system('pwd')
        return render(request,'create.html')



def data(request):
    for i in db.entries:
        print(i)
    print(db)
    return render(request,'create.html')


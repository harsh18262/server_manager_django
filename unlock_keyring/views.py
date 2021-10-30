from logging import root
from django.shortcuts import redirect, render
import os
import pykeepass as kp
from dashboard import views
from unlock_keyring import context_processors

# Create your views here.
db = ""


def home(request):
    message = ""
    if os.path.isfile("password_db.kdbx"):
        if request.method == "POST":
            pass1 = request.POST.get("pass")
            try:
                global db
                db = kp.PyKeePass("password_db.kdbx", password=pass1)
            except kp.exceptions.CredentialsError:
                message = "Incorrect Password"
            else:
                print("login success")
                # return redirect("/dash", db=db)
                context=context_processors.get_db_context(request)
                context.update({"db": db})
                return views.home(request, db)
                print(db)

        return render(request, "unlock.html", {"message": message})
    else:
        os.system("pwd")
        return render(request, "create.html")


def data(request):

    return render(request, "add.html")

def add(request):
    db1=db
    entries=db.entries
    if request.method == "POST":
        host = request.POST.get("host")
        user = request.POST.get("user")
        pass1 = request.POST.get("pass")
        key = request.POST.get("key")
        db.add_entry(db.root_group, host, user, pass1,notes=key)
        db.save()
        message="entry added successfully"
        return render(request, "add.html", {"message": message})
    
    return render(request, "add.html")
    
    


from logging import root
from django.shortcuts import redirect, render
import os
import pykeepass as kp
from dashboard import views
import re


# Create your views here.
db = ""


def unlock(request):
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
                return views.dashboard(request, db)

        return render(request, "unlock.html", {"message": message})
    else:
        pass1 = request.POST.get("pass")
        pass2 = request.POST.get("confirm_pass")
        print(pass1)
        if pass1 == pass2 and pass1 != None:
            kp.create_database("password_db.kdbx", password=pass1)
            return render(request, "unlock.html")
        else:
            return render(request, "create.html")


def testing(request):

    return render(request, "add.html")


def add_key(request):
    db1 = db
    entries = db.entries
    if request.method == "POST":
        host = request.POST.get("host")
        user = request.POST.get("user")
        pass1 = request.POST.get("pass")

        key = request.POST.get("key")

        key = key.replace("\r", "")
        re.sub("\n", "\\n", key)
        key = repr(key)
        db.add_entry(db.root_group, host, user, pass1, notes=key)
        db.save()
        message = "entry added successfully"
        return render(request, "add.html", {"message": message})

    return render(request, "add.html")

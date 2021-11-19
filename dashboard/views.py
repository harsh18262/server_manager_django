from django.shortcuts import redirect, render
from unlock_keyring import views as uk_view

# Create your views here.

db1 = ""


def dashboard(request, db=db1):
    global db1
    if db1 == "":
        if db == "":
            return redirect("/")
        db1 = db
    elif db == "":

        db = db1
    title = request.GET.get("server", "")
    entries = db.entries
    if "server" in request.GET:
        entry = db.find_entries(title=title, first=True)
    else:
        entry = db.find_entries(title="127.0.0.1", first=True)

    return render(request, "index.html", {"entries": entries, "entry": entry})


def test(request):

    return render(request, "base.html", {"entries": entries})


def keys(request):
    if db1 == "":
        return redirect("/")
    db = db1
    key_entry = db.entries
    for i in key_entry:
        print(i.title)

    return render(request, "keys.html", {"entries": key_entry})


def pass_db():
    return db1

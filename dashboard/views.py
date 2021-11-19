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
    entry = []
    pkey_available = False
    if "server" in request.GET:
        host_selected = True
        entry = db.find_entries(title=title, first=True)
        if entry.notes != "''":
            pkey_available = True
        else:
            pkey_available = False
    else:
        host_selected = False

    return render(
        request,
        "index.html",
        {
            "entries": entries,
            "entry": entry,
            "host_selected": host_selected,
            "pkey_available": pkey_available,
        },
    )


def test(request):

    return render(request, "temp.html", {"a": "a"})


def monitoring(request):
    if db1 == "":
        return redirect("/")
    db = db1
    server_text = ""
    key_entry = db.entries
    server = request.GET.get("server", "")
    if "server" in request.GET:
        host_selected = True
        server_text = "server=" + server
    else:
        host_selected = False

    return render(
        request,
        "monitoring.html",
        {"entries": key_entry, "server": server_text, "host_selected": host_selected},
    )


def keys(request):
    if db1 == "":
        return redirect("/")
    db = db1
    key_entry = db.entries

    return render(request, "keys.html", {"entries": key_entry})


def pass_db():
    return db1


def logout(request):
    global db1
    db1 = ""
    return render(request, "logout.html")

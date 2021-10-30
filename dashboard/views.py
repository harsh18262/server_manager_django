from django.shortcuts import render

# Create your views here.

db1 = ""


def home(request, db=db1):
    global db1
    if db1=="":
        
        db1 = db
    else:
        db=db1
    title=request.GET.get('server', '')
    print(title)
    entries = db.entries
    if "server" in request.GET:
        entry = db.find_entries(title=title, first=True)
    else:
        entry = db.find_entries(title="127.0.0.1", first=True)

    return render(request, "index.html", {"entries": entries, "entry": entry})


def test(request):

    return render(request, "base.html", {"entries": entries})

def keys(request):
    db=db1
    key_entry=db.entries
    for i in key_entry:
        print(i.title)

  
    
    return render(request,"keys.html",{"entries":key_entry})


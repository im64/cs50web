from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entryName):
    data = util.get_entry(entryName)
    if data is None:
        return render(request, "encyclopedia/404.html", {
            "name": entryName,
        })
    
    

    return render(request, "encyclopedia/entry.html", {
        "name": entryName,
        "data": data
    })

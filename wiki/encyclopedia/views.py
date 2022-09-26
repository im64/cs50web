from django.shortcuts import render

from . import util


def index(request):
    q = request.GET.get("q")
    if q is not None:
        return search(request, q)

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def newpage(request):
    if request.method != "POST":
        return render(request, "encyclopedia/newpage.html")

    name = request.POST["pagename"]
    if name in util.list_entries():
        return render(request, "encyclopedia/404.html", {
            "name": str(name + "already exists"),
        })

    data = request.POST["content"]
    util.save_entry(name, data)
    return render(request, "encyclopedia/entry.html", {
        "name": name,
        "data": util.get_entry(name)
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


def editpage(request, entryName):
    data = util.get_entry(entryName)
    return render(request, "encyclopedia/edit.html", {
        "name": entryName,
        "content": data,
    })
    

def search(request, query):
    results = []
    for i in util.list_entries():
        # if full match -> redirect
        if query.lower() == i.lower():
            return render(request, "encyclopedia/entry.html", {
                "name": i,
                "data": util.get_entry(i)
            })
        if query.lower() in i.lower():
            results.append(i)

    # if no matches -> 404
    if not results:
        return render(request, "encyclopedia/404.html", {
            "name": query,
        })

    # if partial match -> display every item
    return render(request, "encyclopedia/search.html", {
        "entries": results,
        "query": query
    })

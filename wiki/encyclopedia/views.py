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
    return entry(request, name)


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
    if request.method == "GET":
        return render(request, "encyclopedia/edit.html", {
            "name": entryName,
            "content": util.get_entry(entryName),
        })
    if request.method == "POST":
        data = request.POST["content"]
        util.save_entry(entryName, data)
        print(data)
        return entry(request, entryName)

    

def search(request, query):
    results = []
    for i in util.list_entries():
        # if full match -> redirect
        if query.lower() == i.lower():
            return entry(request, i)
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

import datetime
from django.shortcuts import render


# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "xmas/index.html", {
        "isXmas": now.month == 12 and now.day == 25,
        "now": now,
    })
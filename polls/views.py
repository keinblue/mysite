from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Menuda")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def post(request):
    if request.method == "POST":
         return HttpResponse("POST, Menuda")
    else:
        return HttpResponse("GET, Menuda")
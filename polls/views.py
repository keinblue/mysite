from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Menuda")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def post(request):
	if request.method == "POST":
		msg = request.POST['choice']
		return HttpResponse("POST, Menuda %s" % msg)
	else :
		return HttpResponse("GET, Menuda")
#    if request.method == "POST":
#    	msg = request.POST['choice']
#		return HttpResponse("POST, Menuda [%s]", % msg)
#    else:
#        return HttpResponse("GET, Menuda")
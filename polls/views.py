from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("Hello, Menuda")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

@csrf_exempt
def post(request):
	if request.method == "POST":
		LoginSNS = request.POST['LoginSNS']
		LoginID = request.POST['LoginID']
		LoginPW = request.POST['LoginPW']
		Msg = "LoginSNS:%s\nLoginID:%s\nLoginPW:%s" % (LoginSNS, LoginID, LoginPW)
		return HttpResponse("POST, Menuda\n%s" % Msg)
	else :
		return HttpResponse("GET, Menuda")
#    if request.method == "POST":
#    	msg = request.POST['choice']
#		return HttpResponse("POST, Menuda [%s]", % msg)
#    else:
#        return HttpResponse("GET, Menuda")
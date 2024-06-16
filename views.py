from django.shortcuts import render
from .forms import PollForm
from .models import PollModel

def upoll(request):
	polls = PollModel.objects.all()
	return render(request,"upoll.html",{"msg":polls})

def ucreate(request):
	if request.method == "POST":
		data = PollForm(request.POST)
		if data.is_valid():
			data.save()
			msg = "Poll Created"
			fm = PollForm()
			return render(request,"ucreate.html",{"fm":fm,"msg":msg})
		else:
			msg = "check errors"
			return render(request,"ucreate.html",{"fm":data,"msg":msg})
	else:
		fm = PollForm()
		return render(request,"ucreate.html",{"fm":fm})

def uresult(request):
	return render(request,"uresult.html")

def uvote(request,poll_id):
	p_id = PollModel.objects.get(poll_id)
	return render(request,"uvote.html")

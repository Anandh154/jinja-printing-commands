from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'KVR','age':25}
    return render(request,'wish.html',context=d)

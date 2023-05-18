from django.shortcuts import render

# Create your views here.
def filters(request):
    d={'data':'Hai HoW aRe YoU'}
    return render(request,'filters.html',d)
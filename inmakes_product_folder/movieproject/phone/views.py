from django.shortcuts import render, redirect
from django.http import HttpResponse

from . models import Phone
from . forms import PhoneForm
# Create your views here.
#def index(request):

 #   return HttpResponse("helo")
def index(request):
    phone=Phone.objects.all()
    context={
        'phone_list':phone
    }
    #return HttpResponse("hello am new")
    return render(request,'phoneindex.html',context)
def detail(request,phone_id):
   # return HttpResponse("this is  movie number   %s" % movie_id)
    phone=Phone.objects.get(id=phone_id)
    return render (request,"phonedetail.html",{'phone':phone})

def add(request):

     if request.method=="POST":
         name=request.POST.get('name',)
         desc=request.POST.get('desc',)
         year=request.POST.get('year',)
         img = request.FILES['img']
         phone=Phone(name=name,desc=desc,year=year,img=img)
         phone.save()

     return render(request, 'phoneadd.html')

def update(request, id):
    phone=Phone.objects.get(id=id)
    form = PhoneForm(request.POST or None,request.FILES, instance=phone)

    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'phoneedit.html',{'form':form,'phone':phone})

def delete(request,id):
    if request.method=='POST':
        phone=Phone.objects.get(id=id)
        phone.delete()
        return redirect('/')
    return render(request,'phonedelete.html')

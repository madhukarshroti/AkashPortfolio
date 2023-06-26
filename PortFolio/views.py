from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import View
from Projects.models import ProjectShow
from Certificate.models import Certificate
from django.template.loader import render_to_string

def index(request):
    CertificatesData= Certificate.objects.all()
    Projectsdata= ProjectShow.objects.all()
    data = {
        'Projectsdata':Projectsdata,
        'Certificates':CertificatesData,
    }
    return render(request,'index.html',data)




def ProjectHandle(request,myid):
    ProjectDetails=ProjectShow.objects.filter(id=myid)
    ProDetails=ProjectShow.objects.all()
    print(ProDetails)
    return render(request, 'blog-single.html',{'ProjectDetails':ProjectDetails[0]})

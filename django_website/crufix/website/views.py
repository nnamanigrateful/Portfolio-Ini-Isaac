from django.shortcuts import render
from django.contrib import messages
from .models import Testimonial,Project, ProjectDetailImage

# Create your views here.
def home(request):
    testimonies = Testimonial.objects.all()
    project = Project.objects.all()
    context = {
        'testimonies':testimonies,
        'project':project
    }
    return render(request, 'home.html',context)

def portfolio(request):
    project = Project.objects.all()
    return render(request, 'portfolio.html', {'project':project})

def project_detail(request,proj):
    project_id = Project.objects.get(id)
    project_images = ProjectDetailImage.objects.filter(project=project_id)
    # project_id = project.id
    # project_images = project.projectdetailimage_set.all()
    return render(request, 'project_detail.html', {'project_images':project_images,'project_id':project_id})

    
    # project_list = 
    # project_images = 
    pass
    # proj = proj.replace('_', ' ')
    # #Get project name from db
    # try:
    #     project = Project.objects.get(name=proj)
    #     project_detail = ProjectDetailImage.objects.filter(project=project)
    #     return render(request, 'project_detail.html',{'project_detail':project_detail, 'project':project})
    # except:
    #     return render(request, 'home.html')

    # pass

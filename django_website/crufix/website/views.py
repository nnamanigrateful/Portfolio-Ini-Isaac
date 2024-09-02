from django.shortcuts import render, get_object_or_404
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


def project_detail(request, proj):
    # Retrieve the project using the 'proj' parameter from the URL
    project = get_object_or_404(Project, id=proj)
    
    # Fetch all images related to this project
    project_images = ProjectDetailImage.objects.filter(project=project) 

    # Pass the project and its images to the template
    return render(request, 'project_detail.html', {
        'project': project,
        'project_images': project_images
    })

# def project_detail(request,proj):
#     project_id = Project.objects.get(id)
#     project_images = ProjectDetailImage.objects.filter(project=project_id)
    # project_id = project.id
    # project_images = project.projectdetailimage_set.all()
    # return render(request, 'project_detail.html', {'project_images':project_images,'project_id':project_id})

    
    # project_list = 
    # project_images = 
    # pass
    # proj = proj.replace('_', ' ')
    # #Get project name from db
    # try:
    #     project = Project.objects.get(name=proj)
    #     project_detail = ProjectDetailImage.objects.filter(project=project)
    #     return render(request, 'project_detail.html',{'project_detail':project_detail, 'project':project})
    # except:
    #     return render(request, 'home.html')

    # pass

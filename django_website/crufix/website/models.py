from django.db import models

class Project(models.Model):
    DESIGN_TYPE = (
        ('Website Design','Website Design'),
        ('Mobile Design','Mobile Design'),
        ('Web App Design','Web App Design')
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    design_type = models.CharField(max_length=25, choices= DESIGN_TYPE)
    cover_image = models.ImageField(upload_to='project_covers/', blank=True, null=True)

    def __str__(self):
        return self.name


class ProjectDetailImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='detail_images')
    image = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return f"{self.project.name} - Image"


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    testimony = models.TextField( default='')
    stars = models.IntegerField(default=1)
    image = models.ImageField(upload_to='testimonial_images/')
    
    def __str__(self):
        return self.name
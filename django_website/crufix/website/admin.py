from django.contrib import admin
from .models import ProjectDetailImage, Project, Testimonial
# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectDetailImage)
admin.site.register(Testimonial)
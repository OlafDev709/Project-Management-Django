from django.forms import ModelForm

from .models import Project, ProjectFile

class ProjectFileForm(ModelForm):
    class Meta:
        model = ProjectFile
        fields = ['name', 'attachment']
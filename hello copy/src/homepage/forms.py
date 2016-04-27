#django imports
from django import forms
from django.forms import ModelForm

#model imports
from .models import blog

class BlogPost(ModelForm):
    class Meta:
        #model we are using is from the class, blog
        model = blog
        fields = ['title', 'context', 'after', 'initial']
from django.forms import ModelForm
from  .models import Bb
class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title','contentt','price', 'rubric')
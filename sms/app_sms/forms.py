from django.forms import ModelForm
from .models import SMS
class CreateForm(ModelForm):
    class Meta:
        model = SMS
        fields = '__all__'
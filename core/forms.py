from django.forms import ModelForm
from .models import Clientele

class ClienteleForm(ModelForm):
    class Meta:
        model = Clientele
        fields = ['name', 'last_name', 'age', 'salary', 'email', 'photo', 'date_birth', 'doc_id']

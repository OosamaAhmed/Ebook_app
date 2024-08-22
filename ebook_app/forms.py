


from django import forms 
from .models import EBooksModel

class EbooksForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
                    field.widget.attrs['class'] = 'form-control' 
    class Meta:
        model = EBooksModel
        fields = ('__all__')
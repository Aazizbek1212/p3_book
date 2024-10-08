from django import forms

from main.models import Book



class AddForm(forms.ModelForm):
    class Meta:
        model = Book
        fields  = '__all__'






class SearchForm(forms.Form):
    query = forms.CharField(label='Qidiruv', max_length=100)

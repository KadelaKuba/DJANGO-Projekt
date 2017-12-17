from django import forms
from .models import Movie, Director, Genre


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = "__all__"


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"

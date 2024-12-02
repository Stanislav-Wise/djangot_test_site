from django import forms

class MovieFilterForm(forms.Form):
    title = forms.CharField(required=False, label="Название фильма")
    genre = forms.CharField(required=False, label="Жанр")
    min_rating = forms.DecimalField(required=False, label="Минимальный рейтинг", max_digits=3, decimal_places=1)
    max_rating = forms.DecimalField(required=False, label="Максимальный рейтинг", max_digits=3, decimal_places=1)
    release_date_from = forms.DateField(required=False, label="Дата выпуска (с)", widget=forms.DateInput(attrs={'type': 'date'}))
    release_date_to = forms.DateField(required=False, label="Дата выпуска (по)", widget=forms.DateInput(attrs={'type': 'date'}))

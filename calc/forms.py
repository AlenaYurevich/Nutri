from django import forms

Choices_notice = [(1, f'Женщина'),
                  (2, f'Мужчина')]


class IdmtForm(forms.Form):
    height = forms.IntegerField(label="Введите свой рост в сантиметрах", min_value=120, initial=170,
                                widget=forms.NumberInput(attrs={'class': "form-control", 'autofocus': 'autofocus'}))
    weight = forms.DecimalField(label="Введите свой вес", min_value=1, initial=60,
                                decimal_places=1, widget=forms.NumberInput(attrs={'class': "form-control"}))
    gender = forms.TypedChoiceField(label="Пол", choices=Choices_notice, initial=1,
                                          widget=forms.RadioSelect())


class ImtForm(forms.Form):
    height = forms.IntegerField(label="Введите свой рост", min_value=120, initial=170,
                                widget=forms.NumberInput(attrs={'class': "form-control"}))
    weight = forms.DecimalField(label="Введите свой вес", min_value=1, initial=60,
                                decimal_places=1, widget=forms.NumberInput(attrs={'class': "form-control"}))

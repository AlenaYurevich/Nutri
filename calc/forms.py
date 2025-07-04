from django import forms

Choices_notice = [(1, f'Женщина'),
                  (2, f'Мужчина')]


class ImtForm(forms.Form):
    height = forms.IntegerField(label="Введите свой рост в сантиметрах", min_value=120, initial=170,
                                widget=forms.NumberInput(attrs={'class': "form-control"}))
    gender = forms.TypedChoiceField(label="Пол", choices=Choices_notice, initial=1,
                                          widget=forms.RadioSelect())

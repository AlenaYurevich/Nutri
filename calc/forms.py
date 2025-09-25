from django import forms

Choices_notice = [(1, f'Женщина'),
                  (2, f'Мужчина')]

Activity = [(1.2, f'Минимальная активность'),
            (1.375, f'Слабый уровень активности'),
            (1.55, f'Умеренный уровень активности'),
            (1.7, f'Тяжелая или трудоемкая активность'),
            (1.9, f'Экстремальный уровень активности')]


class IdmtForm(forms.Form):
    height = forms.IntegerField(label="Введите свой рост, см", min_value=120, initial=170,
                                widget=forms.NumberInput(attrs={'class': "form-control", 'autofocus': 'autofocus'}))
    weight = forms.DecimalField(label="Введите свой вес, кг", min_value=1, initial=60,
                                decimal_places=1, widget=forms.NumberInput(attrs={'class': "form-control"}))
    age = forms.IntegerField(label="Введите свой возраст, полных лет", min_value=10,
                             widget=forms.NumberInput(attrs={'class': "form-control"}))
    gender = forms.TypedChoiceField(label="Пол", choices=Choices_notice, initial=1,
                                          widget=forms.RadioSelect())
    activity = forms.TypedChoiceField(label="Физическая активность", choices=Activity, initial=1.2,
                                      widget=forms.RadioSelect())


class ImtForm(forms.Form):
    height = forms.IntegerField(label="Введите свой рост", min_value=120, initial=170,
                                widget=forms.NumberInput(attrs={'class': "form-control"}))
    weight = forms.DecimalField(label="Введите свой вес", min_value=1, initial=60,
                                decimal_places=1, widget=forms.NumberInput(attrs={'class': "form-control"}))

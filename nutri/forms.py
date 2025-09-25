from django import forms


class BMIForm(forms.Form):
    height = forms.DecimalField(label="Введите свой рост, см", min_value=50, max_value=250, initial=170,
                                widget=forms.NumberInput(attrs={'class': "form-control"}))
    weight = forms.DecimalField(label="Введите свой вес, кг", min_value=10, initial=60,
                                decimal_places=1, widget=forms.NumberInput(attrs={'class': "form-control"}))


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': "Ваше имя*", 'autocomplete': "given-name"}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': "form-control phone", 'placeholder': "Ваш телефон*", 'autocomplete': "tel"}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={
        'class': "form-control", 'placeholder': "Email*", 'autocomplete': "email"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control",
                                                           'placeholder': "Услуга, желаемая дата и время*"}),
                              max_length=1000)

from django import forms
from .models import Institute, InstituteOwner, DebitCard


class DebitCardForm(forms.ModelForm):
    class Meta:
        model = DebitCard
        fields = "__all__"


class InstituteForm(forms.ModelForm):
    class Meta:
        model = Institute
        fields = "__all__"
        exclude = ('Card_ID', 'URL', 'Token', )


class InstituteOwnerForm(forms.ModelForm):
    class Meta:
        model = InstituteOwner
        exclude = ('Institute_ID',)
        widgets = {
            'password': forms.PasswordInput
        }

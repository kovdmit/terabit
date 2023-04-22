from django.forms import ModelForm

from .models import Balance


class BalanceForm(ModelForm):

    class Meta:
        model = Balance
        fields = ('value',)

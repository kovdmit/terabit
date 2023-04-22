from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404

from .forms import BalanceForm

User = get_user_model()


def pay(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = BalanceForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data.get('value')
            if user.balance.value < value:
                raise ValueError('Недостаточно средств')
            user.balance.balance_minus(value)
    form = BalanceForm()
    current_balance = user.balance.value
    return render(request, 'shop/pay.html', {
        'form': form,
        'pk': pk,
        'current_balance': current_balance
    })

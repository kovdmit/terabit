from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.cache import cache_page

from .forms import BalanceForm

User = get_user_model()


@cache_page(60 * 5)
def settings_api(request):
    return JsonResponse(settings.SITE_OPTIONS)


def pay(request, pk):
    """View-функция, отнимающая баланс по данным из POST запроса."""
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = BalanceForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data.get('value')
            if user.balance.value < value:
                messages.error(request, 'Недостаточно средств')
                # смотря какая нужна ошибка
                raise ValueError('Недостаточно средств')
            messages.success(request, 'Успех')
            user.balance.balance_minus(value)
    form = BalanceForm()
    current_balance = user.balance.value
    return render(request, 'shop/pay.html', {
        'form': form,
        'pk': pk,
        'current_balance': current_balance
    })

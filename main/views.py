from django.shortcuts import render

from .forms import RequestForm


def home(request):
    form = RequestForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        form = RequestForm()
        return render(request, 'main/home.html', {
            'form': form,
            'success_message': 'Дякуємо! Ми отримали заявку та скоро зв’яжемося з вами.',
        })

    return render(request, 'main/home.html', {'form': form})

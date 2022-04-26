from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from snack.models import Snacks
from snack.forms import SnackForm


def list_snacks(request):
    snacks = Snacks.objects.all()
    return render(request, 'list_snacks.html', {'snacks' : snacks})


def create_snack(request):
    form = SnackForm(request.POST or None)
    # a line to create an object when a "submit" is requested.

    if form.is_valid():
        form.save()
        return redirect('list_snacks')

    return render(request, 'snack_form.html', {'form': form})


# update member
def update_snack(request, id):
    snack = Snacks.objects.get(id=id) # get the one row matched id
    form = SnackForm(request.POST or None, instance=snack)
    # forward instance to the form, instance = member object

    # 유효성 검증
    if form.is_valid():
        form.save()
        return redirect('list_snacks')

    return render(request, 'snack_form.html', {'form': form, 'snack': snack})


def delete_snack(request, id):
    snack = Snacks.objects.get(id=id)

    if request.method == 'POST':
        snack.delete()
        return redirect('list_snacks')

    return render(request, 'snack_delete.html', {'snack': snack})
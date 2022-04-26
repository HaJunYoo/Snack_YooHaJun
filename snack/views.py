from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from snack.models import Snacks


from snack.forms import SnackForm


def list_members(request):
    members = Snacks.objects.all()
    return render(request, 'snack/list_snacks.html', {'members' : members})
# render => request 받아와 경로에 model의 members 객체 전달


def create_member(request):
    form = SnackForm(request.POST or None)
    # a line to create an object when a "submit" is requested.

    if form.is_valid():
            # function that return boolean (true/false) to confirm
            # that a form is valid or not.
        form.save() # function to execute the form and submit the data in the form into particular functions.

        return redirect('list_snacks') # function to execute a HTML file according to the name

    return render(request, 'snack/snack_form.html', {'form': form})
    # render 함수는 파이썬 데이터를 템플릿에 적용하여 HTML로 반환하는 함수

# update member
def update_member(request, id):
    member = Snacks.objects.get(id=id) # get the one row matched id
    form = SnackForm(request.POST or None, instance=member)
    # forward instance to the form, instance = member object

    # 유효성 검증
    if form.is_valid():
        form.save()
        return redirect('list_snacks')

    return render(request, 'snack/snack_form.html', {'form': form, 'member': member})


def delete_member(request, id):
    member = Snacks.objects.get(id=id)

    if request.method == 'POST':
        member.delete()
        return redirect('list_snacks')

    return render(request, 'snack/snack_delete.html', {'member': member})
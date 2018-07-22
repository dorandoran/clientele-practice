from django.shortcuts import render, redirect, get_object_or_404
from .models import Clientele
from .forms import ClienteleForm
from django.contrib.auth.decorators import login_required


def list_clientele(request):
    clientele = Clientele.objects.all()
    return render(request, 'clientele.html', {'clientele': clientele})


@login_required
def new_client(request):
    form = ClienteleForm(request.POST or None, request.FILES or None)

    #validate form
    if form.is_valid():
        form.save()
        return redirect(list_clientele)

    return render(request, 'form.html', {'form': form})


@login_required
def update_client(request, id):
    client = get_object_or_404(Clientele, pk=id)
    form = ClienteleForm(request.POST or None, request.FILES or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect(list_clientele)

    return render(request, 'form.html', {'form': form})


@login_required
def delete_client(request, id):
    client = get_object_or_404(Clientele, pk=id)

    if request.method == 'POST':
        client.delete()
        return redirect(list_clientele)

    return render(request, 'confirm.html', {'client': client})

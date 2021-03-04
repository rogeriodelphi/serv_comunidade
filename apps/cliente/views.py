from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

from .forms import ClienteForm


@login_required
@permission_required('cliente.add_cliente')
def adicionar_cliente(request):
    template_name = 'cliente/adicionar_cliente.html'
    context = {}
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:area_logada')
    form = ClienteForm()
    context['form'] = form
    return render(request, template_name, context)

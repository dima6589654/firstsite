from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView

from testapp.forms import SMSCreateForm
from testapp.models import SMS


class AddSms(CreateView):
    template_name = 'testapp/create.html'
    form_class = SMSCreateForm
    success_url = reverse_lazy('index')


class ReadSms(DetailView):
    model = SMS
    template_name = 'testapp/read.html'


class ListSms(ListView):
    model = SMS
    template_name = 'testapp/list.html'
    context_object_name = 'sms_list'


class DeleteSms(DeleteView):
    model = SMS
    template_name = 'testapp/delete.html'
    success_url = reverse_lazy('index')


class UpdateSms(UpdateView):
    model = SMS
    template_name = 'testapp/update.html'
    form_class = SMSCreateForm
    success_url = reverse_lazy('index')

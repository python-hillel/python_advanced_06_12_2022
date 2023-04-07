from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from groups.forms import GroupCreateForm, GroupUpdateFrom
from groups.models import Group
from students.models import Student


class ListGroupView(ListView):
    model = Group       # object_list
    template_name = 'group/list.html'


class CreateGroupView(CreateView):
    model = Group
    form_class = GroupCreateForm
    success_url = reverse_lazy('groups:list')
    template_name = 'group/create.html'

    def form_valid(self, form):
        response = super().form_valid(form)

        new_group = form.save()

        students = form.cleaned_data['students']
        for student in students:
            student.group = new_group
            student.save()

        return response


class UpdateGroupView(UpdateView):
    model = Group
    form_class = GroupUpdateFrom
    success_url = reverse_lazy('groups:list')
    template_name = 'group/update.html'

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['headman_field'] = self.object.headman.pk
        except AttributeError:
            pass

        return initial

    def form_valid(self, form):
        response = super().form_valid(form)

        students = form.cleaned_data['students']
        for student in students:
            student.group = self.object
            if hasattr(student, 'headman_group'):
                group = student.headman_group
                group.headman = None
                group.save()
            student.save()

        headman_pk = int(form.cleaned_data.get('headman_field'))
        if headman_pk:
            form.instance.headman = Student.objects.get(pk=headman_pk)
        else:
            form.instance.headman = None

        form.save()

        return response


def detail_group(request, pk):
    return HttpResponse(f'DETAIL GROUP VIEW for group {pk}')


def delete_group(request, pk):
    return HttpResponse(f'DELETE GROUP VIEW for group {pk}')

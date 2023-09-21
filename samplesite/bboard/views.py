from django.db import transaction
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView
from django.views import View
from bboard.forms import BbForm
from bboard.models import Bb, Rubric


class CommonDataMixin(View):
    def get_common_data(self):
        rubrics = Rubric.objects.all()
        count_bb = self.count_bb()
        return {'rubrics': rubrics, 'count_bb': count_bb}

    def count_bb(self):
        result = dict()
        for r in Rubric.objects.annotate(num_bbs=Count('bb')):
            result.update({r.pk: r.num_bbs})
        return result


class BbCreateView(CommonDataMixin, CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_common_data())
        return context


class IndexView(CommonDataMixin, View):
    def get(self, request):
        bbs = Bb.objects.all()
        context = {'bbs': bbs}
        context.update(self.get_common_data())
        return HttpResponse(render_to_string('bboard/index.html', context, request))


class BbByRubricView(CommonDataMixin, TemplateView):
    template_name = 'bboard/by_rubric.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_rubric'] = get_object_or_404(Rubric, pk=context['rubric_id'])
        context['bbs'] = get_list_or_404(Bb, rubric=context['rubric_id'])
        return context


class AddView(CommonDataMixin, FormView):
    template_name = 'bboard/create.html'
    form_class = BbForm

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('by_rubric', kwargs={'rubric_id': form.cleaned_data['rubric'].pk}))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


class AddSaveView(CommonDataMixin, View):
    def post(self, request):
        bbf = BbForm(request.POST)

        if bbf.is_valid():
            try:
                with transaction.atomic():
                    bbf.save()
            except Exception as e:
                # Обработка ошибки и отмена транзакции
                transaction.set_rollback(True)
                return HttpResponse(f"Произошла ошибка: {str(e)}", status=500)

            return HttpResponseRedirect(reverse('by_rubric', kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
        else:
            context = {'form': bbf}
            context.update(self.get_common_data())
            return render(request, 'bboard/create.html', context)


class DetailView(CommonDataMixin, View):
    def get(self, request, rec_id):
        bb = get_object_or_404(Bb, pk=rec_id)
        bbs = get_list_or_404(Bb, rubric=bb.rubric.pk)
        context = {'bb': bb, 'bbs': bbs}
        context.update(self.get_common_data())
        return HttpResponse(render_to_string('bboard/detail.html', context, request))


class IndexRespView(CommonDataMixin, View):
    def get(self, request):
        resp = HttpResponse("Здесь будет главная страница сайта", content_type='text/plain; charset=utf-8')
        resp['keywords'] = 'Python, Django'
        return resp


class ByRubricView(CommonDataMixin, View):
    def get(self, request, rubric_id, **kwargs):
        current_rubric = get_object_or_404(Rubric, pk=rubric_id)
        bbs = get_list_or_404(Bb, rubric=rubric_id)
        context = {'bbs': bbs, 'current_rubric': current_rubric}
        context.update(self.get_common_data())
        return render(request, 'bboard/by_rubric.html', context)

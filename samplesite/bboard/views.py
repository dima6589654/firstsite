from django.db.models import Min, Max, Count
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views import View

from bboard.forms import BbForm
from bboard.models import Bb, Rubric


def count_bb():
    result = dict()
    for r in Rubric.objects.annotate(num_bbs=Count('bb')):
        result.update({r.pk: r.num_bbs})

    return result


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        context['count_bb'] = count_bb()
        return context


class IndexView(View):
    def get(self, request):
        bbs = Bb.objects.all()
        rubrics = Rubric.objects.all()
        context = {'bbs': bbs, 'rubrics': rubrics, 'count_bb': count_bb(), }
        return HttpResponse(render_to_string('bboard/index.html', context, request))


class BbByRubricView(TemplateView):
    template_name = 'bboard/by_rubric.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_rubric'] = Rubric.objects.get(pk=context['rubric_id'])
        context['bbs'] = Bb.objects.filter(rubric=context['rubric_id'])
        context['rubrics'] = Rubric.objects.all()
        return context


class AddView(View):
    def get(self, request):
        bbf = BbForm()
        context = {'form': bbf}
        return render(request, 'bboard/create.html', context)


class AddSaveView(View):
    def post(self, request):
        bbf = BbForm(request.POST)

        if bbf.is_valid():
            bbf.save()

            return HttpResponseRedirect(reverse('by_rubric',
                                                kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
        else:
            context = {'form': bbf}
            return render(request, 'bboard/create.html', context)


class DetailView(View):
    def get(self, request, rec_id):
        bb = get_object_or_404(Bb, pk=rec_id)
        bbs = get_list_or_404(Bb, rubric=bb.rubric.pk)
        context = {'bb': bb, 'bbs': bbs}
        return HttpResponse(render_to_string('bboard/detail.html', context, request))


class IndexRespView(View):
    def get(self, request):
        resp = HttpResponse("Здесь будет", content_type='text/plain; charset=utf-8')
        resp.write(' главная')
        resp.writelines((' страница', ' сайта'))
        resp['keywords'] = 'Python, Django'
        return resp


class ByRubricView(View):
    def get(self, request, rubric_id, **kwargs):
        current_rubric = Rubric()
        try:
            current_rubric = Rubric.objects.get(pk=rubric_id)
        except current_rubric.DoesNotExist:
            return HttpResponseNotFound('Такой рубрики нет!')

        bbs = Bb.objects.filter(rubric=rubric_id)
        rubrics = Rubric.objects.all()

        context = {
            'bbs': bbs,
            'rubrics': rubrics,
            'current_rubric': current_rubric,
            'count_bb': count_bb(),
            'kwargs': kwargs,
        }

        return render(request, 'bboard/by_rubric.html', context)

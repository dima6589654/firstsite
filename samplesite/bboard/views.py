from django.db.models import Min, Max, Count, Q, Sum, IntegerField, Avg
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from bboard.forms import BbForm
from bboard.models import Bb, Rubric


def count_bb():
    result = Rubric.objects.annotate(num_bbs=Count('bb')).values('pk', 'num_bbs')
    return {r['pk']: r['num_bbs'] for r in result}


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        context['count_bb'] = count_bb()
        return context


def index(request):
    bbs = Bb.objects.order_by('-published')
    rubrics = Rubric.objects.all()

    result = Bb.objects.aggregate(
        min_price=Min('price'),
        max_price=Max('price'),
        diff_price=Max('price') - Min('price')
    )

    context = {
        'bbs': bbs,
        'rubrics': rubrics,
        'min_price': result.get('min_price'),
        'max_price': result.get('max_price'),
        'diff_price': result.get('diff_price'),
        'count_bb': count_bb(),
    }
    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id, **kwargs):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)

    context = {
        'bbs': bbs,
        'rubrics': rubrics,
        'current_rubric': current_rubric,
        'count_bb': count_bb(),
        'kwargs': kwargs,
    }
    return render(request, 'bboard/by_rubric.html', context)

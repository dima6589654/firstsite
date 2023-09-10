from django.urls import path

from bboard.views import IndexView, ByRubricView, BbCreateView, DetailView, AddView, AddSaveView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:rubric_id>/', ByRubricView.as_view(), name='by_rubric'),
    path('add/', BbCreateView.as_view(), name='add'),
    # path('add/save/', AddSaveView.as_view(), name='add_save'),
    # path('add/', AddView.as_view(), name='add'),
    path('read/<int:rec_id>/', DetailView.as_view(), name='read'),
]

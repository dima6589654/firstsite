from django.urls import path

from testapp.views import AddSms, ReadSms, ListSms, DeleteSms, UpdateSms

app_name = 'testapp'

urlpatterns = [
    path('addsms/', AddSms.as_view(), name='add_sms'),
    path('readsms/<int:pk>/', ReadSms.as_view(), name='read_sms'),
    path('listsms/', ListSms.as_view(), name='list_sms'),
    path('deletesms/<int:pk>/', DeleteSms.as_view(), name='delete_sms'),
    path('updatesms/<int:pk>/', UpdateSms.as_view(), name='update_sms'),
]

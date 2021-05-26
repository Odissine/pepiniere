from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'order'

urlpatterns = [
    path('list/', views.order_list, name='order_list'),
    path('detail/<int:id>', views.order_detail, name='order_detail'),
    path('valid/<int:id>', views.order_valid, name='order_valid'),
    path('update/<int:id>', views.order_update, name='order_update'),
    path('remove/<int:id>', views.order_remove, name='order_remove')
]

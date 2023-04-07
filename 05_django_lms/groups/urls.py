from django.urls import path

from .views import detail_group
from .views import delete_group
from .views import ListGroupView
from .views import CreateGroupView
from .views import UpdateGroupView

app_name = 'groups'

urlpatterns = [
    path('', ListGroupView.as_view(), name='list'),
    path('create/', CreateGroupView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateGroupView.as_view(), name='update'),
    path('detail/<int:pk>/', detail_group, name='detail'),
    path('delete/<int:pk>/', delete_group, name='delete'),
]

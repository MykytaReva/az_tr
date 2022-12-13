from django.contrib import admin
from django.urls import path

from links.views import update_prices, home, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    # path('delete/<pk>/', LinkDeleteView.as_view(), name='delete-view'),
    path('delete/<pk>/', delete, name='delete-view'),
    path('update/', update_prices, name='update'),
    # path('del/<pk>/', delete_view, name='delete-v'),
]

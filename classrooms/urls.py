
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes.views import (classroom_update,classroom_delete,
classroom_create,classroom_detail,classroom_list)
from API.views import (ListView,DetailView,UpdateView,DeleteView,CreateView)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', classroom_detail, name='classroom-detail'),

    path('classrooms/create', classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/',classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/',classroom_delete, name='classroom-delete'),
    


    path('class/list', ListView.as_view(), name='list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('class/<int:classroom_id>/detail', DetailView.as_view(), name='detail'),
    path('class/<int:classroom_id>/update', UpdateView.as_view(), name='update'),
    path('class/<int:classroom_id>/delete', DeleteView.as_view(), name='delete'),
    path('class/create', CreateView.as_view(), name='create'),




]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

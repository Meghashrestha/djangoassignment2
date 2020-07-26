from django.urls import path
from .views import index, user_profile,feed, post,edit_profile, delete_profile

from django.conf import settings
from django.conf.urls.static import static
from .views import *
app_name = 'setup'

urlpatterns = [
    path('', index),
    path('post/', post),
    path('profile/', user_profile),
    path('editprofile/', edit_profile),
    path('deleteprofile/', delete_profile),

    # path('user_login/', user_login),
    # path('register/', register),
    # path('logout/', user_logout),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)



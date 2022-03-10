from django.contrib import admin
from django.urls import path, include
from accounts.views import SignupPageView


urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignupPageView.as_view(), name='signup'),

    # local
    path('', include('news.urls'))
]


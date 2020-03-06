"""habit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from habit_tracker import views

urlpatterns = [
    path('', views.habit_list, name='habit_list'),
    path('habit/new/', views.habit_new, name='habit_new'),
    path('habit/<int:pk>/', views.habit_detail, name='habit_detail'),
    #path('record/<int:habit_pk>', views.record, name='record'),
    # path('/<int:pk>/edit/', views.habit_edit, name='habit_edit'),
    path('<int:pk>/delete/', views.habit_delete, name='habit_delete'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
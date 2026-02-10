"""
URL configuration for fashion_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from .views import home_page
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    # path('accounts/', include("django.contrib.auth.urls")),
    path('users/', include("user.urls")),
    path('', include("products.urls")),
    path('common/', include("common.urls")),
    path('addresses/', include("address.urls")),
    path('reviews/', include("reviews.urls")),
    path("api/schema/", SpectacularAPIView.as_view(),
         name="schema"),  # raw schema
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"),
         name="swagger-ui"),  # swagger ui
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"),
         name="redoc"),  # redoc ui
]

# ============= ARCHIVO: src/urls.py =============
from django.urls import path
from .views.fraction_views import FractionView
from .controller.fraction_controller import FractionController

app_name = 'fractions'

urlpatterns = [
    path('', FractionView.as_view(), name='calculator'),
    path('api/', FractionController.as_view(), name='api'),
]
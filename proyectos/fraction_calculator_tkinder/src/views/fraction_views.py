# ============= ARCHIVO: src/views/fraction_views.py =============
from django.shortcuts import render
from django.views import View

class FractionView(View):
    """Vista principal para la calculadora de fracciones"""
    
    def get(self, request):
        return render(request, 'calculator.html')
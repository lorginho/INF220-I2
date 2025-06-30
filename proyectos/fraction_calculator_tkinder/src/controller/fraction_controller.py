# ============= ARCHIVO: src/controller/fraction_controller.py =============
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from ..model.fraction import Fraction, FractionCalculator

@method_decorator(csrf_exempt, name='dispatch')
class FractionController(View):
    """Controlador para manejar operaciones con fracciones"""
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            action = data.get('action')
            
            if action == 'calculate':
                return self._handle_calculation(data)
            elif action == 'compare':
                return self._handle_comparison(data)
            elif action == 'sort':
                return self._handle_sorting(data)
            else:
                return JsonResponse({'error': 'Acción no válida'}, status=400)
                
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON inválido'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    def _handle_calculation(self, data):
        """Maneja las operaciones de cálculo"""
        try:
            fraction1_str = data.get('fraction1')
            fraction2_str = data.get('fraction2')
            operation = data.get('operation')
            
            if not all([fraction1_str, fraction2_str, operation]):
                return JsonResponse({'error': 'Faltan parámetros'}, status=400)
            
            fraction1 = Fraction.from_string(fraction1_str)
            fraction2 = Fraction.from_string(fraction2_str)
            
            result = FractionCalculator.calculate(fraction1, operation, fraction2)
            
            return JsonResponse({
                'success': True,
                'result': str(result),
                'fraction1': str(fraction1),
                'fraction2': str(fraction2),
                'operation': operation,
                'decimal': round(result.to_decimal(), 6)
            })
            
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    def _handle_comparison(self, data):
        """Maneja la comparación de fracciones"""
        try:
            fractions_str = data.get('fractions', [])
            
            if len(fractions_str) < 2:
                return JsonResponse({'error': 'Se necesitan al menos 2 fracciones'}, status=400)
            
            fractions = [Fraction.from_string(f) for f in fractions_str]
            comparisons = FractionCalculator.compare_fractions(fractions)
            
            result = [
                {
                    'fraction': str(fraction),
                    'position': position,
                    'decimal': round(fraction.to_decimal(), 6)
                }
                for fraction, position in comparisons
            ]
            
            return JsonResponse({
                'success': True,
                'comparisons': result
            })
            
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    def _handle_sorting(self, data):
        """Maneja el ordenamiento de fracciones"""
        try:
            fractions_str = data.get('fractions', [])
            ascending = data.get('ascending', True)
            
            if not fractions_str:
                return JsonResponse({'error': 'No se proporcionaron fracciones'}, status=400)
            
            fractions = [Fraction.from_string(f) for f in fractions_str]
            sorted_fractions = FractionCalculator.sort_fractions(fractions, ascending)
            
            result = [
                {
                    'fraction': str(fraction),
                    'decimal': round(fraction.to_decimal(), 6)
                }
                for fraction in sorted_fractions
            ]
            
            return JsonResponse({
                'success': True,
                'sorted_fractions': result,
                'order': 'ascendente' if ascending else 'descendente'
            })
            
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)

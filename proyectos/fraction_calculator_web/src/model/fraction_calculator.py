# ============= ARCHIVO: src/model/fraction_calculator.py =============
import math
from typing import List, Tuple
from src.model.fraction import Fraction


class FractionCalculator:
    """Clase para realizar operaciones con fracciones"""

    @staticmethod
    def calculate(fraction1: Fraction, operation: str, fraction2: Fraction) -> Fraction:
        """Realiza una operación entre dos fracciones"""
        operations = {
            '+': fraction1.add,
            '-': fraction1.subtract,
            '*': fraction1.multiply,
            '/': fraction1.divide
        }

        if operation not in operations:
            raise ValueError(f"Operación '{operation}' no válida")

        return operations[operation](fraction2)

    @staticmethod
    def compare_fractions(fractions: List[Fraction]) -> List[Tuple[Fraction, str]]:
        """Compara múltiples fracciones y devuelve información de comparación"""
        if len(fractions) < 2:
            return [(fractions[0], "única fracción")] if fractions else []

        sorted_fractions = sorted(fractions)
        result = []

        for i, fraction in enumerate(sorted_fractions):
            if i == 0:
                result.append((fraction, "menor"))
            elif i == len(sorted_fractions) - 1:
                result.append((fraction, "mayor"))
            else:
                result.append((fraction, "intermedia"))

        return result

    @staticmethod
    def sort_fractions(fractions: List[Fraction], ascending: bool = True) -> List[Fraction]:
        """Ordena una lista de fracciones"""
        return sorted(fractions, reverse=not ascending)

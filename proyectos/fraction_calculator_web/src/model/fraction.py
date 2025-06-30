# ============= ARCHIVO: src/model/fraction.py =============
import math
from typing import List, Tuple


class Fraction:
    """Clase para representar y operar con fracciones"""

    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("El denominador no puede ser cero")

        # Simplificar la fracción al crearla
        gcd = math.gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

        # Mantener el signo en el numerador
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def __str__(self) -> str:
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self) -> str:
        return f"Fraction({self.numerator}, {self.denominator})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Fraction):
            return False
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other) -> bool:
        if not isinstance(other, Fraction):
            raise TypeError("No se puede comparar Fraction con otro tipo")
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other) -> bool:
        return self < other or self == other

    def __gt__(self, other) -> bool:
        return not self <= other

    def __ge__(self, other) -> bool:
        return not self < other

    def add(self, other) -> 'Fraction':
        """Suma de fracciones"""
        if not isinstance(other, Fraction):
            raise TypeError("Solo se pueden sumar fracciones")

        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def subtract(self, other) -> 'Fraction':
        """Resta de fracciones"""
        if not isinstance(other, Fraction):
            raise TypeError("Solo se pueden restar fracciones")

        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def multiply(self, other) -> 'Fraction':
        """Multiplicación de fracciones"""
        if not isinstance(other, Fraction):
            raise TypeError("Solo se pueden multiplicar fracciones")

        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def divide(self, other) -> 'Fraction':
        """División de fracciones"""
        if not isinstance(other, Fraction):
            raise TypeError("Solo se pueden dividir fracciones")

        if other.numerator == 0:
            raise ValueError("No se puede dividir por cero")

        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        return Fraction(new_num, new_den)

    def to_decimal(self) -> float:
        """Convierte la fracción a decimal"""
        return self.numerator / self.denominator

    @classmethod
    def from_string(cls, fraction_str: str) -> 'Fraction':
        """Crea una fracción desde un string formato 'numerador/denominador'"""
        try:
            if '/' in fraction_str:
                parts = fraction_str.split('/')
                if len(parts) != 2:
                    raise ValueError("Formato inválido")
                num = int(parts[0].strip())
                den = int(parts[1].strip())
            else:
                num = int(fraction_str.strip())
                den = 1
            return cls(num, den)
        except (ValueError, IndexError):
            raise ValueError(
                f"No se pudo convertir '{fraction_str}' a fracción")

# calculator/urls.py

from django.urls import path
from .views import CalculatorView,CheckPalindromeView,PatternView

urlpatterns = [
    path('calculate/', CalculatorView.as_view(), name='calculate'),
    path('palindrome/', CheckPalindromeView.as_view(), name='palindrome'),
    path('patt/', PatternView.as_view(), name='pattern'),
    
]

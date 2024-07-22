from django.urls import path
from .views import create_appbancouios, export_to_excel

urlpatterns = [
    path('appbancouios/', create_appbancouios, name='appbancouios'),
    path('relatorio/', export_to_excel, name='export_to_excel'),  # Nova URL para exportação

    # Adicione outras URLs aqui
]

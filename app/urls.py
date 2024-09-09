from django.urls import path
from .views import create_appbancouios, export_to_excel
from . import views

urlpatterns = [
    path('appbancouios/', create_appbancouios, name='appbancouios'),
    path('relatorio/', export_to_excel, name='export_to_excel'),  # Nova URL para exportação
    path('send_message/', views.send_message, name='send_message'),
    path('success/', views.success_page, name='success_page'),  # Adicionando a URL para a página de sucesso
    
    # Adicione outras URLs aqui
]

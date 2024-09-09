from django.urls import path
from .views import create_appbancouios, export_to_excel, import_to_excel
from . import views

urlpatterns = [
    path('appbancouios/', create_appbancouios, name='appbancouios'),
    path('relatorio/', export_to_excel, name='export_to_excel'),  # Nova URL para exportação
    path('import/', import_to_excel, name='import_to_excel'),  # Nova URL para exportação
    path('send_message/', views.send_message, name='send_message'),
    path('success/', views.success_page, name='success_page'),  # Adicionando a URL para a página de sucesso
    path('success_import/', views.import_success, name='import_success_page'),  # Adicionando a URL para a página de sucesso
    path('error/', views.error_page, name='error_page'),
    
    # Adicione outras URLs aqui
]

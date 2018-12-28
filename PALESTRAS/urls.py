from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^Login/', views.Login, name='Login'),
    url(r'^Inscrição/', views.Cadastro, name='Cadastro'),
    url(r'^Inscrição1/', views.Inserir, name='Inserir'),
    url(r'^Autenticar/', views.Autenticar, name='Autenticar'),
    url(r'^Adicionar_Curso/', views.AddCurso, name='AddCurso'),
    url(r'^Modificar_Curso/', views.ModCurso, name='ModCurso'),
    url(r'^Sucesso_Curso/', views.Inserir1, name='Inserir1'),
    url(r'^Autenticar1/', views.Retornar, name='Retornar'),
    url(r'^InscreverCurso/', views.InCurso, name='InCurso'),
    url(r'^Matricular/', views.Matricular, name='Matricular'),
    url(r'^Modificar/', views.Modificar, name='Modificar'),
    url(r'^Deletar/', views.DelCurso, name='DelCurso'),
    url(r'^Deletar1/', views.Excluir, name='Excluir'),
    url(r'^Autenticar2/', views.Voltar, name='Voltar'),
]
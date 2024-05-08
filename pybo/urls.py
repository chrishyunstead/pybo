from django.urls import path
from . import views

app_name='pybo' # 네임스페이스 적용하기(각각의 앱이 관리하는 독립된 이름 공간)

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    ]
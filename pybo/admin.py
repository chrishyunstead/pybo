from django.contrib import admin
from .models import Question

# admin에 데이터 검색기능 추가
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin) # admin에서 모델 관리하기

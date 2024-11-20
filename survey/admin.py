from django.contrib import admin
from .models import Question, Choice, Response, Certificate

# Inline model for Choices within the Question model
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1  # Number of empty forms to show

# Register the Question model along with its related choices
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'type', 'required', 'multiple')
    search_fields = ('text',)
    list_filter = ('type', 'required')
    inlines = [ChoiceInline]  # Add Choice inline to the Question form

# Register the Choice model
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'option_text')
    search_fields = ('option_text',)
    list_filter = ('question',)

# Register the Response model
@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('question', 'response_text', 'created_at')
    search_fields = ('response_text',)
    list_filter = ('question',)

# Register the Certificate model
@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('response', 'file_name', 'uploaded_at')
    search_fields = ('file_name',)
    list_filter = ('response',)

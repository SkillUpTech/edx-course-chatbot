from django.contrib import admin

from course_chatbot.models import CourseChatbot

class CourseChatbotAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'chatbot_url']

admin.site.register(CourseChatbot, CourseChatbotAdmin)

from django.urls import path

from course_chatbot.views import ChatbotView
from django.contrib.auth.decorators import login_required

urlpatterns = [
  path('', login_required(ChatbotView.as_view()), name='course_chatbot_dashboard')
]

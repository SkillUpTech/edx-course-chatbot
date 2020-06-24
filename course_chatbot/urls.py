from django.conf.urls import url

from course_chatbot.views import ChatbotView

urlpatterns = [
  url(
        r'^$',
        ChatbotView.as_view(),
        name='course_chatbot'
    ),
]

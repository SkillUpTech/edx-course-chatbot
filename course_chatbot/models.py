from django.db import models

class CourseChatbot(models.Model):
    course_id = models.CharField(max_length=100, blank=True, verbose_name='Course ID')
    chatbot_url = models.CharField(max_length=300, blank=True, verbose_name='Chatbot URL')
    
    def __str__(self):
        return self.course_id

    class Meta:
        app_label = "course_chatbot"
        verbose_name = ('Course Chatbot')
        verbose_name_plural = ('Course Chatbots')

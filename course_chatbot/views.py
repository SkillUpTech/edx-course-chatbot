import logging
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from opaque_keys.edx.keys import CourseKey
from lms.djangoapps.courseware.courses import get_course_with_access, has_access
from course_chatbot.models import CourseChatbot

log = logging.getLogger(__name__)

class ChatbotView(GenericAPIView):
    def get(self, request, course_id):
        course_key = CourseKey.from_string(course_id)
        course = get_course_with_access(request.user, "load", course_key)
        chatbot_obj = None
        try:
            chatbot_obj = CourseChatbot.objects.get(course_id = course_id)
        except:
            pass

        context = {
            "course": course,
            "chatbot": chatbot_obj,
        }
        
        return render(request, 'chatbot/chatbot.html', context)

    def post(self, request, course_id):
        action = request.POST['action']
        chatbot_url = request.POST['chatbot_url']
        course_key = CourseKey.from_string(course_id)
        course = get_course_with_access(request.user, "load", course_key)

        context = {
            "course": course,
        }
 
        if action == "create_chatbot":
            try:
                chatbot_obj, created = CourseChatbot.objects.get_or_create(course_id=course_id)
                if created:
                    chatbot_obj.chatbot_url = chatbot_url
                    chatbot_obj.save()
                else:
                    chatbot_obj.chatbot_url = chatbot_url
                    chatbot_obj.save()
                context.update({"chatbot": chatbot_obj }) 
            except:
                pass

        if action == "del_chatbot":
            try:
                chatbot_obj = CourseChatbot.objects.get(course_id = course_id)
                chatbot_obj.delete()
                context.update({"chatbot": None})
            except:
                pass 
        return render(request, 'chatbot/chatbot.html', context)

from django import template
from course_chatbot.models import CourseChatbot
import requests
import waffle

register = template.Library()

@register.filter
def get_chatbot_url(course_id):
    """
    Get chatbot url for the course
    """
    if "/courses/course-v1" in course_id and waffle.switch_is_active('Chatbot_Switch'):
        cid = course_id.split("/courses/")[1].split("/")[0]
        try:
            course_chatbot = CourseChatbot.objects.get(course_id=cid)
            res = requests.get(course_chatbot.chatbot_url)
            if str(res.status_code) == "200":
                return course_chatbot.chatbot_url
            else:
                return ""
        except CourseChatbot.DoesNotExist:
            return ""
    else:
        return ""



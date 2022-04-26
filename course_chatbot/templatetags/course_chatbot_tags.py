from openedx.core.djangoapps.enrollments.api import get_enrollments
from django import template
from course_chatbot.models import CourseChatbot
import requests
import waffle
import logging

log = logging.getLogger()

register = template.Library()

@register.filter
def get_chatbot_url(data):
    """
    Get chatbot url for the course
    """
    info = data.split(",")
    course_id = info[0]
    username = info[1]
    if "/courses/course-v1" in course_id and "about" not in course_id and waffle.switch_is_active('Chatbot_Switch'):
        cid = course_id.split("/courses/")[1].split("/")[0]
        course_enrollment = get_enrollments(username,cid)
        if not course_enrollment:
            return ""
        try:
            course_chatbot = CourseChatbot.objects.get(course_id=cid)
            #res = requests.get(course_chatbot.chatbot_url)
            #if str(res.status_code) == "200":
            return course_chatbot.chatbot_url
            #else:
            #    return ""
        except CourseChatbot.DoesNotExist:
            return ""
    else:
        return ""



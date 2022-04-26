from django.conf import settings
from django.utils.translation import ugettext_noop
from lms.djangoapps.courseware.tabs import EnrolledTab
from lms.djangoapps.courseware.access import has_access
import waffle

class ChatbotTab(EnrolledTab):
    """
    Defines the Wiki view type that is shown as a course tab.
    """
    
    if waffle.switch_is_active('Chatbot_Switch'): 
        """
        This Tab will be visible only when the Chatbot_Switch is active in Waffle Switches
        """
        type = "chatbot"
        title = ugettext_noop('Chatbot')
        view_name = "course_chatbot_dashboard"
        is_dynamic = True

        @classmethod
        def is_enabled(cls, course, user=None):
            """
            Returns true if the wiki is enabled and the specified user is enrolled or has staff access.
            """
            return bool(user and has_access(user, 'staff', course, course.id))


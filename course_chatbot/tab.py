from django.conf import settings
from django.utils.translation import ugettext_noop

from courseware.tabs import EnrolledTab
from courseware.access import has_access

class ChatbotTab(EnrolledTab):
    """
    Defines the Wiki view type that is shown as a course tab.
    """

    type = "chatbot"
    title = ugettext_noop('Chatbot')
    view_name = "course_chatbot"
    is_dynamic = True

    @classmethod
    def is_enabled(cls, course, user=None):
        """
        Returns true if the wiki is enabled and the specified user is enrolled or has staff access.
        """
        return bool(user and has_access(user, 'staff', course, course.id))

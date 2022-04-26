# edx-course-chatbot

Installation
------------

To get the latest commit from GitHub
    
    sudo su -s /bin/bash edxapp
    cd
    source edxapp_env
    cd /var/tmp
    git clone https://github.com/SkillUpTech/edx-maple-course-level-chatbot.git
    cd edx-maple-course-level-chatbot
    pip install .
     
Add ``course_chatbot`` to your ``INSTALLED_APPS``


    INSTALLED_APPS = (
        ...,
        'course_chatbot',
    )

Add ``course_chatbot`` url to your lms's url.py

    #chatbot urls
    urlpatterns += [
      re_path(
         r'^courses/{}/chatbot/'.format(
             settings.COURSE_ID_PATTERN,
         ),
         include('course_chatbot.urls'),
         name='course_chatbot_endpoints',
      ),
    ]       

Add chatbot placeholder in your theme's footer.html

    
    <%!
      from course_chatbot.templatetags.course_chatbot_tags import get_chatbot_url
    %>
    
    
    % if request.user.is_authenticated:
      ${ request.path+','+request.user.username | get_chatbot_url}
    % endif
    
    
Migrate LMS and Restart lms


    Logout from bash as edxapp user
    Crtl+d
    Run migrate command
    /edx/bin/edxapp-migrate-lms course_chatbot
    Restart lms
    /edx/bin/supervisorctl restart lms

To Enable the Chatbot make a entry in Django admin 


    Goto https://<YOUR-LMS-URL>/admin/waffle/switch/ 
    Click on ADD SWITCH button
    Enter name as ``Chatbot_Switch`` 
    Check the active checkbox to enable the chatbot
    Add a Note
    Click Save



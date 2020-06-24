# edx-course-chatbot

Installation
------------

To get the latest commit from GitHub

.. code-block:: bash
    
    sudo su -s /bin/bash edxapp
    cd
    source edxapp_env
    cd /var/tmp
    git clone https://github.com/SkillUpTech/edx-course-chatbot.git
    pip install .
     
Add ``course_chatbot`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'course_chatbot',
    )

Add ``course_chatbot`` url to your lms's url.py

.. code-block:: python

    #chatbot urls
    urlpatterns += [
        url(
            r'^courses/{}/chatbot/'.format(
                settings.COURSE_ID_PATTERN,
            ),
            include('course_chatbot.urls'),
        ),
    ]

Add chatbot placeholder in your theme's footer.html

.. code-block:: python 

    <%!
      from course_chatbot.templatetags.course_chatbot_tags import get_chatbot_url
    %>

    <iframe name="guido" align="right" style="position: fixed;bottom: 5px;right: 10px;height: 570px;width: 320px;z-index: 99999;overflow: hidden;" frameborder="0" scrolling="no"  class="frame-area" src= ${ request.path | get_chatbot_url}></iframe>

Restart lms


from setuptools import setup, find_packages

setup(
    name="course_chatbot",
    version="0.1",
    install_requires=["setuptools"],
    requires=[],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "openedx.course_tab": [
            "course_chatbot = course_chatbot.tab:ChatbotTab"
        ]
    }
)

# Generated by Django 3.2.13 on 2022-04-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseChatbot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(blank=True, max_length=100, verbose_name='Course ID')),
                ('chatbot_url', models.TextField(blank=True, verbose_name='Chatbot Integration Script')),
            ],
            options={
                'verbose_name': 'Course Chatbot',
                'verbose_name_plural': 'Course Chatbots',
            },
        ),
    ]
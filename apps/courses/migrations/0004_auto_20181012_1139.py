# Generated by Django 2.0.1 on 2018-10-12 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(default='Python开发', max_length=20, verbose_name='课程类别'),
        ),
        migrations.AddField(
            model_name='course',
            name='is_banner',
            field=models.BooleanField(default=False, verbose_name='是否轮播'),
        ),
        migrations.AddField(
            model_name='course',
            name='tag',
            field=models.CharField(default='', max_length=15, verbose_name='课程标签'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_tell',
            field=models.CharField(default='什么都可以学到，按时交作业，不然叫家长', max_length=300, verbose_name='老师告诉你'),
        ),
        migrations.AddField(
            model_name='course',
            name='you_need_know',
            field=models.CharField(default='一颗勤学的心是本课程必要的前提', max_length=300, verbose_name='课程须知'),
        ),
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.CharField(default='http://baidu.com/', max_length=200, verbose_name='访问地址'),
        ),
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('cj', '初级'), ('zj', '中级'), ('gj', '高级')], max_length=2, verbose_name='难度'),
        ),
    ]
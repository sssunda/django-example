# Generated by Django 2.0.13 on 2019-04-17 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='region',
            field=models.CharField(choices=[('Africa', '아프리카'), ('Europe', '유럽'), ('Oceania', '오세아니아'), ('Asia', '아시아'), ('North America', '북아메리카'), ('South America', '남아메리카')], default='Asia', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(help_text='포스팅 제목을 입력해주세요. 최대 100자 내외', max_length=100, verbose_name='제목'),
        ),
    ]

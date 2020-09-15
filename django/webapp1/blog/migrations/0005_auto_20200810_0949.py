# Generated by Django 3.0.9 on 2020-08-10 09:49

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_read_cnt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='CONTENT'),
        ),
        migrations.AlterField(
            model_name='post',
            name='modify_dt',
            field=models.DateTimeField(verbose_name='MODIFY DATE'),
        ),
        migrations.CreateModel(
            name='PostAttachFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(blank=True, null=True, upload_to='%Y/%m/%d', verbose_name='파일')),
                ('filename', models.CharField(max_length=64, null=True, verbose_name='첨부파일명')),
                ('content_type', models.CharField(max_length=128, null=True, verbose_name='MIME TYPE')),
                ('size', models.IntegerField(verbose_name='파일 크기')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='blog.Post', verbose_name='Post')),
            ],
        ),
    ]

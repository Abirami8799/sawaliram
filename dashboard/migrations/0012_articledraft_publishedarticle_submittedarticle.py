# Generated by Django 2.2.4 on 2020-01-08 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_consolidate_article_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleDraft',
            fields=[
            ],
            options={
                'db_table': 'articles',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('dashboard.article',),
        ),
        migrations.CreateModel(
            name='PublishedArticle',
            fields=[
            ],
            options={
                'db_table': 'articles',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('dashboard.article',),
        ),
        migrations.CreateModel(
            name='SubmittedArticle',
            fields=[
            ],
            options={
                'db_table': 'articles',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('dashboard.article',),
        ),
    ]
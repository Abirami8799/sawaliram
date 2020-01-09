# Generated by Django 2.2.3 on 2020-01-08 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_answercredit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answered_by',
            new_name='submitted_by',
        ),
        migrations.AddField(
            model_name='answer',
            name='status',
            field=models.CharField(default='submitted', max_length=50),
        ),
        migrations.DeleteModel(
            name='AnswerDraft',
        ),
    ]

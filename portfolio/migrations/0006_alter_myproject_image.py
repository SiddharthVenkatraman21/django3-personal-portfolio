# Generated by Django 3.2.3 on 2022-01-16 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myproject',
            name='image',
            field=models.ImageField(upload_to='portfolio/images/myProjectImages'),
        ),
    ]

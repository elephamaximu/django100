# Generated by Django 2.1.7 on 2019-03-06 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modeltest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AddField(
            model_name='article',
            name='publications',
            field=models.ManyToManyField(to='modeltest.Publication'),
        ),
    ]

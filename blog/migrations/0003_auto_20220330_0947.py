# Generated by Django 3.2.8 on 2022-03-30 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fallowers', '0001_initial'),
        ('blog', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.CharField(blank=True, help_text='dssdf sdjdsjfskdfsdfs dshfj', max_length=355, verbose_name='MAQOLA NOMI'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(default="Text yo'q", max_length=8000),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=55),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fallowers.fallower')),
            ],
        ),
    ]

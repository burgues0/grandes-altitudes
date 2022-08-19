# Generated by Django 4.0.5 on 2022-08-07 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_ong', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='id_review',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='materials',
            name='id_material',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='user_login',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_ong.userlogin'),
        ),
    ]

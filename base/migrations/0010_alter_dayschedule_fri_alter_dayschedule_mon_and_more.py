# Generated by Django 4.0.1 on 2022-02-10 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_dayschedule_timeschedule_delete_friday_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayschedule',
            name='fri',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='fri', to='base.timeschedule'),
        ),
        migrations.AlterField(
            model_name='dayschedule',
            name='mon',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon', to='base.timeschedule'),
        ),
        migrations.AlterField(
            model_name='dayschedule',
            name='sat',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sat', to='base.timeschedule'),
        ),
        migrations.AlterField(
            model_name='dayschedule',
            name='sun',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='sun', to='base.timeschedule'),
        ),
        migrations.AlterField(
            model_name='dayschedule',
            name='thr',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='thr', to='base.timeschedule'),
        ),
        migrations.AlterField(
            model_name='dayschedule',
            name='tue',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='tue', to='base.timeschedule'),
        ),
        migrations.AlterField(
            model_name='dayschedule',
            name='wed',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='wed', to='base.timeschedule'),
        ),
    ]
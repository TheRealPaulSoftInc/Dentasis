# Generated by Django 3.2.10 on 2022-05-07 14:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiagnosisSummaryDental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('dental_image', models.ImageField(max_length=1000, upload_to=None)),
                ('is_favorite', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DiagnosisSummaryTeeth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teeth_name', models.CharField(default='', max_length=255)),
                ('teeth_number', models.PositiveSmallIntegerField()),
                ('diangosis_summary_dental', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diagnosis.diagnosissummarydental')),
            ],
        ),
        migrations.CreateModel(
            name='DiagnosisSummaryCaries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caries_type', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('accuracy', models.DecimalField(blank=True, decimal_places=4, default=None, max_digits=7, null=True)),
                ('x_pos', models.DecimalField(blank=True, decimal_places=4, default=None, max_digits=7, null=True)),
                ('y_pos', models.DecimalField(blank=True, decimal_places=4, default=None, max_digits=7, null=True)),
                ('diangosis_summary_teeth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diagnosis.diagnosissummaryteeth')),
            ],
        ),
    ]

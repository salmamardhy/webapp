# Generated by Django 5.1.3 on 2024-11-15 05:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=100)),
                ('event_url', models.URLField(blank=True, null=True)),
                ('event_photo', models.ImageField(blank=True, null=True, upload_to='program_photos/')),
                ('event_time', models.DateTimeField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='DraftBooking',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('bookingid', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('whatsapp', models.BooleanField(default=False)),
                ('referral_name', models.CharField(blank=True, editable=False, max_length=100)),
                ('bookingstatus', models.CharField(choices=[('active', 'Active'), ('expired', 'Expired')], default='active', max_length=10)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('expires_at', models.DateTimeField(blank=True, null=True)),
                ('memberstatus', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member_bookings', to='account.member')),
                ('referralid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.member')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.event')),
            ],
            options={
                'verbose_name': 'Draft Booking',
                'verbose_name_plural': 'Draft Bookings',
                'db_table': 'draftbooking',
                'unique_together': {('bookingid', 'id')},
            },
        ),
    ]

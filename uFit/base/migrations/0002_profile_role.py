from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Student', 'Student'), ('Trainer', 'Trainer'), ('Wellness Organization', 'Wellness Organization')], default='Student', max_length=50),
        ),
    ]

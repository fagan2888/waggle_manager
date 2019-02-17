# Generated by Django 2.1.7 on 2019-02-16 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hardware', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeprecatesSoftware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'software_deprecates',
            },
        ),
        migrations.CreateModel(
            name='ImageIncludes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'image_icludes_software',
            },
        ),
        migrations.CreateModel(
            name='NeedsHardware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hardware.Component')),
            ],
            options={
                'db_table': 'software_needs_hardware',
            },
        ),
        migrations.CreateModel(
            name='ProvidesHardware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hardware.Component')),
            ],
            options={
                'db_table': 'software_provides_hardware',
            },
        ),
        migrations.CreateModel(
            name='RecognizesHardware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hardware.Component')),
            ],
            options={
                'db_table': 'software_recognizes_hardware',
            },
        ),
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('version', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('image', 'image'), ('firmware', 'firmware'), ('driver', 'driver'), ('plugin', 'plugin')], max_length=255)),
                ('source_url', models.CharField(max_length=255)),
                ('documentation', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('description', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Software',
                'db_table': 'software_software',
            },
        ),
        migrations.CreateModel(
            name='SoftwareRequires',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required_software', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='required_set', to='software.Software')),
                ('software', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='software_requirements_set', to='software.Software')),
            ],
            options={
                'db_table': 'software_requires_software',
            },
        ),
        migrations.AlterUniqueTogether(
            name='software',
            unique_together={('name', 'version', 'type')},
        ),
        migrations.AddField(
            model_name='recognizeshardware',
            name='software',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software.Software'),
        ),
        migrations.AddField(
            model_name='provideshardware',
            name='software',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software.Software'),
        ),
        migrations.AddField(
            model_name='needshardware',
            name='software',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='software.Software'),
        ),
        migrations.AddField(
            model_name='imageincludes',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='includes_set', to='software.Software'),
        ),
        migrations.AddField(
            model_name='imageincludes',
            name='included_software',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='included_in_image_set', to='software.Software'),
        ),
        migrations.AddField(
            model_name='deprecatessoftware',
            name='deprecates',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='deprecated_set', to='software.Software'),
        ),
        migrations.AddField(
            model_name='deprecatessoftware',
            name='software',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deprecates_set', to='software.Software'),
        ),
        migrations.AlterUniqueTogether(
            name='softwarerequires',
            unique_together={('software', 'required_software')},
        ),
        migrations.AlterUniqueTogether(
            name='recognizeshardware',
            unique_together={('software', 'component')},
        ),
        migrations.AlterUniqueTogether(
            name='provideshardware',
            unique_together={('software', 'component')},
        ),
        migrations.AlterUniqueTogether(
            name='needshardware',
            unique_together={('software', 'component')},
        ),
        migrations.AlterUniqueTogether(
            name='imageincludes',
            unique_together={('image', 'included_software')},
        ),
        migrations.AlterUniqueTogether(
            name='deprecatessoftware',
            unique_together={('software', 'deprecates')},
        ),
    ]
# Generated by Django 3.2.16 on 2023-01-11 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='logo',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.vendor'),
        ),
        migrations.AlterField(
            model_name='prod_review',
            name='rating',
            field=models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], default=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('process', 'Processing'), ('rejected', 'Rejected'), ('in_review', 'In_review'), ('published', 'Published')], default='in_review', max_length=20),
        ),
    ]

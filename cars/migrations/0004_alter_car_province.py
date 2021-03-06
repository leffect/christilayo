# Generated by Django 4.0.5 on 2022-07-07 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_rename_milage_car_mileage_rename_state_car_province_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='province',
            field=models.CharField(choices=[('AB', 'Alberta'), ('BC', 'British Columbia'), ('MB', 'Manitoba'), ('NB', 'New Brunswick'), ('NL', 'Newfoundland and Labrador'), ('NT', 'Northwest Territories'), ('NS', 'Nova Scotia'), ('NU', 'Nunavut'), ('ON', 'Ontario'), ('PE', 'Prince Edward Island'), ('QC', 'Quebec'), ('SK', 'Saskatchewan'), ('YT', 'Yukon'), ('AL', 'Alabama USA'), ('AK', 'Alaska USA'), ('AZ', 'Arizona USA'), ('AR', 'Arkansas USA'), ('CA', 'California USA'), ('CO', 'Colorado, USA'), ('CT', 'Connecticut, USA'), ('DE', 'Delaware, USA'), ('DC', 'District Of Columbia, USA'), ('FL', 'Florida, USA'), ('GA', 'Georgia, USA'), ('HI', 'Hawaii, USA'), ('ID', 'Idaho, USA'), ('IL', 'Illinois, USA'), ('IN', 'Indiana, USA'), ('IA', 'Iowa, USA'), ('KS', 'Kansas, USA'), ('KY', 'Kentucky, USA'), ('LA', 'Louisiana, USA'), ('ME', 'Maine, USA'), ('MD', 'Maryland, USA'), ('MA', 'Massachusetts, USA'), ('MI', 'Michigan, USA'), ('MN', 'Minnesota, USA'), ('MS', 'Mississippi, USA'), ('MO', 'Missouri, USA'), ('MT', 'Montana, USA'), ('NE', 'Nebraska, USA'), ('NV', 'Nevada, USA'), ('NH', 'New Hampshire, USA'), ('NJ', 'New Jersey, USA'), ('NM', 'New Mexico, USA'), ('NY', 'New York, USA'), ('NC', 'North Carolina, USA'), ('ND', 'North Dakota, USA'), ('OH', 'Ohio, USA'), ('OK', 'Oklahoma, USA'), ('OR', 'Oregon, USA'), ('PA', 'Pennsylvania, USA'), ('RI', 'Rhode Island, USA'), ('SC', 'South Carolina, USA'), ('SD', 'South Dakota, USA'), ('TN', 'Tennessee, USA'), ('TX', 'Texas, USA'), ('UT', 'Utah, USA'), ('VT', 'Vermont, USA'), ('VA', 'Virginia, USA'), ('WA', 'Washington, USA'), ('WV', 'West Virginia, USA'), ('WI', 'Wisconsin, USA'), ('WY', 'Wyoming, USA'), ('LOS', 'Lagos, Nigeria')], max_length=100),
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-13 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('feedid', models.IntegerField(primary_key=True, serialize=False)),
                ('partnerid', models.IntegerField()),
                ('feedurl', models.CharField(max_length=255)),
                ('lastretrievedtimestamp', models.DateTimeField(blank=True, null=True)),
                ('feedtype', models.CharField(blank=True, max_length=50, null=True)),
                ('laststatus', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('partnerid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('integrationdetails', models.CharField(blank=True, max_length=1000, null=True)),
                ('lastdatasenttimestamp', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('priceid', models.IntegerField(primary_key=True, serialize=False)),
                ('productid', models.IntegerField()),
                ('originalprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('saleprice', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('shippingprice', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('pricetimestamp', models.DateTimeField()),
                ('pricedate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PriceTrendSummary',
            fields=[
                ('pricetrendsummaryid', models.IntegerField(primary_key=True, serialize=False)),
                ('productid', models.IntegerField()),
                ('partnerid', models.IntegerField()),
                ('averageoriginalprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('averagesaleprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('minprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('maxprice', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('productid', models.IntegerField(primary_key=True, serialize=False)),
                ('partnerid', models.IntegerField(blank=True, null=True)),
                ('ean', models.CharField(max_length=13)),
                ('producttitle', models.CharField(max_length=255)),
                ('producturl', models.CharField(max_length=1000)),
                ('sellername', models.CharField(blank=True, max_length=255, null=True)),
                ('lastscrapedtimestamp', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('productspecificationid', models.IntegerField(primary_key=True, serialize=False)),
                ('productid', models.IntegerField()),
                ('specification', models.CharField(max_length=1000)),
                ('specificationtimestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='ScrapeErrorLog',
            fields=[
                ('scrapeerrorlogid', models.IntegerField(primary_key=True, serialize=False)),
                ('scrapesessionid', models.CharField(max_length=10)),
                ('errormessage', models.CharField(max_length=255)),
                ('errortimestamp', models.DateTimeField()),
                ('errortype', models.CharField(blank=True, max_length=50, null=True)),
                ('errorseverity', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScraperConfig',
            fields=[
                ('scraperconfigid', models.IntegerField(primary_key=True, serialize=False)),
                ('configsettings', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=2)),
                ('lastupdatedtimestamp', models.DateTimeField()),
                ('version', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScrapeSession',
            fields=[
                ('scrapesessionid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('scraperconfigid', models.IntegerField(blank=True, null=True)),
                ('starttime', models.DateTimeField()),
                ('endtime', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(max_length=50)),
                ('numberofproductsscraped', models.IntegerField()),
                ('sessionduration', models.DurationField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScrapeSummary',
            fields=[
                ('scrapesummaryid', models.IntegerField(primary_key=True, serialize=False)),
                ('productid', models.IntegerField()),
                ('partnerid', models.IntegerField()),
                ('averageduration', models.DurationField()),
                ('successrate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('totalerrors', models.IntegerField()),
            ],
        ),
    ]

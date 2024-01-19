from django.db import models
from django.db.models import JSONField


class ScraperConfig(models.Model):
    scraper_config_id = models.AutoField(primary_key=True)
    config_settings = models.CharField(max_length=100)
    country = models.CharField(max_length=2)
    last_updated_timestamp = models.DateTimeField()
    version = models.CharField(max_length=50)


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    scraper_config = models.ForeignKey(ScraperConfig, on_delete=models.CASCADE)
    ean = models.CharField(max_length=13)
    details = JSONField(blank=True, null=True)
    product_title = models.CharField(max_length=255)
    product_url = models.URLField(max_length=1000)
    last_scraped_timestamp = models.DateTimeField()

    class Meta:
        # If you're using a custom table name
        db_table = 'product'


# Create Price table
class Price(models.Model):
    PriceID = models.AutoField(primary_key=True)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    OriginalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    SalePrice = models.DecimalField(max_digits=10, decimal_places=2)
    ShippingPrice = models.DecimalField(max_digits=10, decimal_places=2)
    PriceTimestamp = models.DateTimeField()
    PriceDate = models.DateField()


# Create ProductSpecification table
class ProductSpecification(models.Model):
    ProductSpecificationID = models.AutoField(primary_key=True)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    SpecificationTimestamp = models.DateTimeField()


# Create Feeds table
class Feeds(models.Model):
    FeedID = models.AutoField(primary_key=True)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    FeedURL = models.CharField(max_length=255)
    LastRetrievedTimestamp = models.DateTimeField()
    FeedType = models.CharField(max_length=50)
    LastStatus = models.CharField(max_length=50)


# Create Partner table
class Partner(models.Model):
    PartnerID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    IntegrationDetails = models.JSONField()
    LastDataSentTimestamp = models.DateTimeField()


# Create ProductPartner junction table
class ProductPartner(models.Model):
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    PartnerID = models.ForeignKey(Partner, on_delete=models.CASCADE)
    IntegrationDetails = models.JSONField()
    LastDataSentTimestamp = models.DateTimeField()

    class Meta:
        unique_together = ('ProductID', 'PartnerID')
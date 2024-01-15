from django.db import models


# Create ScraperConfig table
class ScraperConfig(models.Model):
    ScraperConfigID = models.AutoField(primary_key=True)
    ConfigSettings = models.CharField(max_length=100)
    Country = models.CharField(max_length=2)
    LastUpdatedTimestamp = models.DateTimeField()
    Version = models.CharField(max_length=50)


# Create Product table
class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ScraperConfigID = models.ForeignKey(ScraperConfig, on_delete=models.CASCADE)
    EAN = models.CharField(max_length=13)
    ProductTitle = models.CharField(max_length=255)
    ProductURL = models.URLField(max_length=1000)
    LastScrapedTimestamp = models.DateTimeField()


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

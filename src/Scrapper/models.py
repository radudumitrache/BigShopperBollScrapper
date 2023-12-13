from django.db import models


class Feed(models.Model):
    feedid = models.IntegerField(primary_key=True)
    partnerid = models.IntegerField()
    feedurl = models.CharField(max_length=255)
    lastretrievedtimestamp = models.DateTimeField(null=True, blank=True)
    feedtype = models.CharField(max_length=50, null=True, blank=True)
    laststatus = models.CharField(max_length=50, null=True, blank=True)


class Partner(models.Model):
    partnerid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    integrationdetails = models.CharField(max_length=1000, null=True, blank=True)
    lastdatasenttimestamp = models.DateTimeField(null=True, blank=True)


class Price(models.Model):
    priceid = models.IntegerField(primary_key=True)
    productid = models.IntegerField()
    originalprice = models.DecimalField(max_digits=10, decimal_places=2)
    saleprice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    shippingprice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pricetimestamp = models.DateTimeField()
    pricedate = models.DateField()


class PriceTrendSummary(models.Model):
    pricetrendsummaryid = models.IntegerField(primary_key=True)
    productid = models.IntegerField()
    partnerid = models.IntegerField()
    averageoriginalprice = models.DecimalField(max_digits=10, decimal_places=2)
    averagesaleprice = models.DecimalField(max_digits=10, decimal_places=2)
    minprice = models.DecimalField(max_digits=10, decimal_places=2)
    maxprice = models.DecimalField(max_digits=10, decimal_places=2)


class Product(models.Model):
    productid = models.IntegerField(primary_key=True)
    partnerid = models.IntegerField(null=True, blank=True)
    ean = models.CharField(max_length=13)
    producttitle = models.CharField(max_length=255)
    producturl = models.CharField(max_length=1000)
    sellername = models.CharField(max_length=255, null=True, blank=True)
    lastscrapedtimestamp = models.DateTimeField(null=True, blank=True)


class ProductSpecification(models.Model):
    productspecificationid = models.IntegerField(primary_key=True)
    productid = models.IntegerField()
    specification = models.CharField(max_length=1000)
    specificationtimestamp = models.DateTimeField()


class ScrapeErrorLog(models.Model):
    scrapeerrorlogid = models.IntegerField(primary_key=True)
    scrapesessionid = models.CharField(max_length=10)
    errormessage = models.CharField(max_length=255)
    errortimestamp = models.DateTimeField()
    errortype = models.CharField(max_length=50, null=True, blank=True)
    errorseverity = models.CharField(max_length=50, null=True, blank=True)


class ScraperConfig(models.Model):
    scraperconfigid = models.IntegerField(primary_key=True)
    configsettings = models.CharField(max_length=25)
    country = models.CharField(max_length=2)
    lastupdatedtimestamp = models.DateTimeField()
    version = models.CharField(max_length=50, null=True, blank=True)


class ScrapeSession(models.Model):
    scrapesessionid = models.CharField(max_length=10, primary_key=True)
    scraperconfigid = models.IntegerField(null=True, blank=True)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50)
    numberofproductsscraped = models.IntegerField()
    sessionduration = models.DurationField(null=True, blank=True)


class ScrapeSummary(models.Model):
    scrapesummaryid = models.IntegerField(primary_key=True)
    productid = models.IntegerField()
    partnerid = models.IntegerField()
    averageduration = models.DurationField()
    successrate = models.DecimalField(max_digits=5, decimal_places=2)
    totalerrors = models.IntegerField()

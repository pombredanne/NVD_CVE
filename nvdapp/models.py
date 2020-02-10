from django.db import models
from django.contrib.postgres.fields import ArrayField

class CPE_NAME(models.Model):
    cpe_22uri = models.CharField(max_length=50,blank=True, default='')
    cpe_23uri = models.CharField(max_length=50)
    last_modified_date = models.DateTimeField('date last modified',blank=True)
    def __str__(self):
        return self.cpe_23uri

class CPE_MATCH(models.Model):
    vulnerable = models.BooleanField()
    versionStartExcluding = models.CharField(max_length=10, blank=True, default='') 
    versionStartIncluding = models.CharField(max_length=10, blank=True, default='') 
    versionEndExcluding = models.CharField(max_length=10, blank=True, default='') 
    versionEndIncluding = models.CharField(max_length=10, blank=True, default='') 
    cpe_name = models.ManyToManyField(CPE_NAME)
    
    def __str__(self):
        return self.cpe_23uri

class CPE_NODE(models.Model):
    operator = models.CharField(max_length=5, blank=True) 
    negate = models.BooleanField(blank=True)
    children = models.ManyToManyField('self')
    cpe_match = models.ManyToManyField(CPE_MATCH)
    
class CPE_CONFIGURATION(models.Model):
    cve_dataversion = models.CharField(max_length=5)
    nodes = models.ManyToManyField(CPE_NODE)
 
class CPE_BASE_METRICV3(models.Model):
    cvssv3_version = models.CharField(max_length=5)
    vectorString = models.CharField(max_length=50)
    attackVector = models.CharField(max_length=10)
    attackComplexity = models.CharField(max_length=10)
    privilegesRequired = models.CharField(max_length=10)
    userInteraction = models.CharField(max_length=10)
    scope = models.CharField(max_length=10)
    confidentialityImpact = models.CharField(max_length=10)
    integrityImpact = models.CharField(max_length=10)
    availabilityImpact = models.CharField(max_length=10)
    baseScore = models.IntegerField()
    baseSeverity = models.CharField(max_length=10)
    exploitabilityScore = models.IntegerField(default=0)
    impactScore = models.IntegerField(default=0)
    
class CPE_BASE_METRICV2(models.Model):
    cvssv2_version = models.CharField(max_length=5, default='')
    vectorString = models.CharField(max_length=50, default='')
    accessVector  = models.CharField(max_length=10, default='')
    accessComplexity  = models.CharField(max_length=10, default='')
    authentication = models.CharField(max_length=10,default='')
    confidentialityImpact = models.CharField(max_length=10, default='')
    integrityImpact  = models.CharField(max_length=10, default='')
    availabilityImpact  = models.CharField(max_length=10, default='')
    baseScore = models.IntegerField(default=0)
    severity = models.CharField(max_length=10, default='')
    exploitabilityScore = models.IntegerField(default=0)
    impactScore = models.IntegerField(default=0)
    acInsufInfo = models.BooleanField()
    obtainAllPrivilege = models.BooleanField()
    obtainUserPrivilege = models.BooleanField()
    obtainOtherPrivilege = models.BooleanField()
    userInteractionRequired = models.BooleanField()

class CPE_IMPACT(models.Model):
    baseMetricV3 = models.ForeignKey(CPE_BASE_METRICV3, on_delete=models.CASCADE)
    baseMetricV2 = models.ForeignKey(CPE_BASE_METRICV2, on_delete=models.CASCADE)

class CVE_ITEM(models.Model):
    cve = models.CharField(max_length=100,default='')
    configurations = models.ForeignKey(CPE_CONFIGURATION, on_delete=models.CASCADE)
    impact = models.ForeignKey(CPE_IMPACT, on_delete=models.CASCADE)
    published_date = models.DateTimeField('date published', blank=True, default='')
    last_modified_date = models.DateTimeField('date last modified',blank=True, default='')
    
class CPE(models.Model):
    cve_data_type = models.CharField(max_length=50)
    cve_data_format = models.CharField(max_length=50)
    cve_data_version = models.CharField(max_length=50)
    cve_data_numberOfCVEs = models.CharField(max_length=50,blank=True, default='')
    cve_data_timestamp = models.DateTimeField(blank=True)
    cve_items = models.ManyToManyField(CVE_ITEM)
from django.shortcuts import render
from django.http import HttpResponse
import django.db.models.query
import os,json,datetime

from .models import (
    CPE_NAME,
    CPE_MATCH,
    CPE_NODE,
    CPE_CONFIGURATION,
    CPE_BASE_METRICV2,
    CPE_BASE_METRICV3,
    CPE_IMPACT,
    CVE_ITEM,
    CPE
)

def index(request):
    return HttpResponse("Hello")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NVD_JSON_DIR = (
    os.path.join(
        BASE_DIR, "nvdapp", "resources"),
)

def get_data(json_file):
    json_data = json.load(json_file)
    data = json.dumps(json_data)
    json_file.close()
    return data

json_file = open(NVD_JSON_DIR[0]+"/nvdcve-1.1-2020.json")
data = get_data(json_file)

# Use the below Django ORM queries to fetch the information for the data model requested.
'''
cpeName = CPE_NAME.objects.get_all()
versionStartExcluding = cpeName.CPE_MATCH.filter('versionStartExcluding')
versionStartIncluding = cpeName.CPE_MATCH.filter('versionStartIncluding')
versionEndExcluding = cpeName.CPE_MATCH.filter('versionEndExcluding')
versionEndIncluding = cpeName.CPE_MATCH.filter('versionEndIncluding')
cve_item = CVE_ITEM.objects.get_all()
cve_id = cve_item.objects.filter(cve_item.cve_id)
cve_data_version = cve_item.objects.filter(cve_item.data_version)
published_date = cve_item.objects.filter(cve_item.pubished_date)
lastModifiedDate = cve_item.objects.filter(cve_item.lastModifiedDate)
cpe_base_v3 = CPE_BASE_METRICV3.objects.get_all()
base_cvss_v3_exp_score = cpe_base_v3.objects.filter('exploitabilityScore')
base_cvss_v3_impact_score = cpe_base_v3.objects.filter('impactScore')
cpe_base_v2 = CPE_BASE_METRICV2.objects.get_all()
base_cvss_v2_exp_score = cpe_base_v2.objects.filter('exploitabilityScore')
base_cvss_v2_impact_score = cpe_base_v2.objects.filter('impactScore')
'''



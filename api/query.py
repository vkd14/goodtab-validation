import os
from goodtables import validate
from django.http import HttpResponse


def upload_resource(resource_file):
    resource_validation(resource_file)


def resource_validation(file):
    report = validate(file, checks=[
        'blank-row',
        'duplicate-row',
        'extra-value',
        'missing-value',
    ])
    if report['tables']['errors'][0]:
        return report['tables']['errors']
    else:
        return HttpResponse("No errors detected")

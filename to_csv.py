import os
import csv

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from university.models import *
from susi.models import *
from jeongsi.models import *
from suneung.models import *


with open('csv/university.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'logo', 'region']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for univ in University.objects.all():
        writer.writerow({'name': univ.name, 'logo': univ.logo, 'region': univ.region})

with open('csv/college.csv', 'w', newline='') as csvfile:
    fieldnames = ['university', 'name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for col in College.objects.all():
        writer.writerow({'university': col.university, 'name': col.name})

with open('csv/major.csv', 'w', newline='') as csvfile:
    fieldnames = ['college', 'name', 'moonigwa']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for maj in Major.objects.all():
        writer.writerow({'college': maj.college, 'name': maj.name, 'moonigwa': maj.moonigwa})

with open('csv/susi.csv', 'w', newline='') as csvfile:
    fieldnames = ['university', 'name', 'year', 'susi_type']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for susi in Susi.objects.all():
        writer.writerow({'university': susi.university, 'name': susi.name, 'year': susi.year, 'susi_type': susi.susi_type})

with open('csv/susi_detail.csv', 'w', newline='') as csvfile:
    fieldnames = ['susi', 'major', 'min_grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for detail in SusiDetail.objects.all():
        writer.writerow({'susi': detail.susi, 'major': str(detail.major.first()) + ' 외', 'min_grade': detail.min_grade})

with open('csv/susi_schedule.csv', 'w', newline='') as csvfile:
    fieldnames = ['susi_detail', 'description', 'start_date', 'end_date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for schedule in SusiSchedule.objects.all():
        writer.writerow({'susi_detail': str(schedule.susi_detail.first()) + ' 외', 'description': schedule.description, 'start_date': schedule.start_date, 'end_date': schedule.end_date})

with open('csv/jeongsi.csv', 'w', newline='') as csvfile:
    fieldnames = ['university', 'year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for jeongsi in Jeongsi.objects.all():
        writer.writerow({'university': jeongsi.university, 'year': jeongsi.year})

with open('csv/jeongsi_detail.csv', 'w', newline='') as csvfile:
    fieldnames = ['jeongsi', 'major', 'gun']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for detail in JeongsiDetail.objects.all():
        writer.writerow({'jeongsi': detail.jeongsi, 'major': detail.major, 'gun': detail.gun})

with open('csv/jeongsi_schedule.csv', 'w', newline='') as csvfile:
    fieldnames = ['jeongsi_detail', 'description', 'start_date', 'end_date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for schedule in JeongsiSchedule.objects.all():
        writer.writerow({'jeongsi_detail': schedule.jeongsi_detail, 'description': schedule.description, 'start_date': schedule.start_date, 'end_date': schedule.end_date})

with open('csv/suneung.csv', 'w', newline='') as csvfile:
    fieldnames = ['description', 'start_date', 'end_date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for schedule in Suneung.objects.all():
        writer.writerow({'description': schedule.description, 'start_date': schedule.start_date, 'end_date': schedule.end_date})


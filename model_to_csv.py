import os
import csv

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from university.models import *
from susi.models import *
from jeongsi.models import *
from suneung.models import *


# university
with open('csv/university.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'logo', 'review_url']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for univ in University.objects.all():
        writer.writerow({'name': univ.name, 'logo': univ.logo})

with open('csv/susi_major_block.csv', 'w', newline='') as csvfile:
    fieldnames = ['university', 'name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for major_block in SusiMajorBlock.objects.all():
        writer.writerow({'university': major_block.university, 'name': major_block.name})

with open('csv/jeongsi_major_block.csv', 'w', newline='') as csvfile:
    fieldnames = ['university', 'name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for major_block in JeongsiMajorBlock.objects.all():
        writer.writerow({'university': major_block.university, 'name': major_block.name})


# susi
with open('csv/susi.csv', 'w', newline='') as csvfile:
    fieldnames = ['university', 'name', 'year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for susi in Susi.objects.all():
        writer.writerow({'university': susi.university, 'name': susi.name, 'year': susi.year})

with open('csv/susi_schedule.csv', 'w', newline='') as csvfile:
    fieldnames = ['susi', 'major_block', 'description', 'start_date', 'end_date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for schedule in SusiSchedule.objects.all():
        writer.writerow({'susi': schedule.susi, 'major_block': schedule.major_block, 'description': schedule.description, 'start_date': schedule.start_date, 'end_date': schedule.end_date})


# jeongsi
with open('csv/jeongsi.csv', 'w', newline='') as csvfile:
    fieldnames = ['university', 'gun', 'year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for jeongsi in Jeongsi.objects.all():
        writer.writerow({'university': jeongsi.university, 'year': jeongsi.year, 'gun': jeongsi.gun})

with open('csv/jeongsi_schedule.csv', 'w', newline='') as csvfile:
    fieldnames = ['jeongsi', 'major_block', 'description', 'start_date', 'end_date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for schedule in JeongsiSchedule.objects.all():
        writer.writerow({'jeongsi': schedule.jeongsi, 'major_block': schedule.major_block, 'description': schedule.description, 'start_date': schedule.start_date, 'end_date': schedule.end_date})


# suneung
with open('csv/suneung.csv', 'w', newline='') as csvfile:
    fieldnames = ['description', 'start_date', 'end_date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for suneung in Suneung.objects.all():
        writer.writerow({'description': suneung.description, 'start_date': suneung.start_date, 'end_date': suneung.end_date})


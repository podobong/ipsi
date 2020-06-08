import os
import csv

import django
from django.db.models import Q
from django.utils.dateparse import parse_datetime
from django.utils.timezone import make_aware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from university.models import *
from susi.models import *
from jeongsi.models import *
from suneung.models import *


# add universities
with open('csv/university.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if not University.objects.filter(name=row[0]):
            University(name=row[0], logo=row[1], review_url=row[2]).save()


# for each university, add susis / susi major blocks / susi schedules
for univ in University.objects.all(): 
    susi_file = 'csv/' + univ.name + '/susi.csv'
    susi_major_block_file = 'csv/' + univ.name + '/susi_major_block.csv'
    susi_schedule_file = 'csv/' + univ.name + '/susi_schedule.csv'

    if os.path.isfile(susi_file):
        with open(susi_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if not Susi.objects.filter(Q(university__name=row[0]) & Q(name=row[1]) & Q(year=row[2])):
                    university = University.objects.get(name=row[0])
                    Susi(university=university, name=row[1], year=row[2]).save()
    
    if os.path.isfile(susi_major_block_file):
        with open(susi_major_block_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if not SusiMajorBlock.objects.filter(Q(university__name=row[0]) & Q(name=row[1])):
                    university = University.objects.get(name=row[0])
                    SusiMajorBlock(university=university, name=row[1]).save()

    if os.path.isfile(susi_schedule_file):
        with open(susi_schedule_file, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                # susi_infos[0]: year, [1]: univ_name, [2]: susi, [3]: susi_name
                susi_infos = row[0].split('/')
                susi = Susi.objects.get(Q(university__name=susi_infos[1]) & Q(name=susi_infos[3]) & Q(year=susi_infos[0]))
                
                # major_block_infos[0]: univ, [1]: major_block_name
                major_block_infos = row[1].split('/')
                major_block = SusiMajorBlock.objects.get(Q(university__name=major_block_infos[0]) & Q(name=major_block_infos[1]))
                
                # save schedule
                if not SusiSchedule.objects.filter(susi=susi).filter(major_block=major_block).filter(description=row[2]):
                    start_date = make_aware(parse_datetime(row[3]))
                    end_date = make_aware(parse_datetime(row[4]))
                    SusiSchedule(susi=susi, major_block=major_block, description=row[2], start_date=start_date, end_date=end_date).save()


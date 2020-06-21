from rest_framework.views import APIView
from rest_framework.response import Response

from susi.models import SusiSchedule


class SusiScheduleList(APIView):
    def get(self, request):
        schedules = SusiSchedule.objects.all()
        schedule_list = []
        for schedule in schedules:
            schedule_info = {
                'university': schedule.susi.university.name,
                'sj': '수시',
                'jh': schedule.susi.name,
                'major_block': schedule.major_block.name,
                'description': schedule.description,
                'start_date': schedule.start_date,
                'end_date': schedule.end_date,
            }
            # TODO: add 'favorite'
            schedule_list.append(schedule_info)
        return Response(schedule_list)


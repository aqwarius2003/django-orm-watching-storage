from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
import datetime
from django.utils.timezone import localtime

# def get_duration(visit):
#        if visit.leaved_at:
#          time_duration = visit.leaved_at - visit.entered_at
#        else:
#          time_duration = localtime() - visit.entered_at
#        return time_duration
# def format_duration(duration):
#     return datetime.timedelta(seconds=int(duration.total_seconds()))



def storage_information_view(request):
    # Программируем здесь
    visit_no_closed = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []
    for visit_no_close in visit_no_closed:
        duration = get_duration(visit_no_close)
        non_closed_visits.append(
        {   'who_entered': visit_no_close.passcard,
            'entered_at': visit_no_close.entered_at,
            'duration': format_duration(duration),
            'is_strange': is_visit_long(duration),
        })

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)

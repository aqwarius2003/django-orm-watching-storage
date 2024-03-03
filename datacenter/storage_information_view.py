from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import format_duration, get_duration, is_visit_long


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []

    for visit in visits:

        duration = get_duration(visit)
        who_entered = visit.passcard
        entered_at = visit.entered_at
        duration = format_duration(duration)
        is_strange = is_visit_long(duration)

        non_closed_visits.append({
            'who_entered': who_entered,
            'entered_at': entered_at,
            'duration': duration,
            'is_strange': is_strange,
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import format_duration, get_duration, is_visit_long
from django.shortcuts import get_object_or_404


# Программируем здесь
def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in visits:
        delta_time = get_duration(visit)
        duration = format_duration(delta_time)
        is_strange = is_visit_long(delta_time)

        this_passcard_visits.append({
                'entered_at': visit.entered_at,
                'duration': duration,
                'is_strange': is_strange,
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

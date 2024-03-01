from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import format_duration, get_duration, is_visit_long
from django.shortcuts import get_object_or_404


    # Программируем здесь
def passcard_info_view(request, passcode):
    # passcard = Passcard.objects.get(passcode=passcode) - работало, проверяем Get 404....вроде работает
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    # get_object_or_404(visits)           # почему то с этой строкой сервер отвечает кодом 500?

    this_passcard_visits = []

    for visit in visits:
        delta_time = get_duration(visit)
        duration = format_duration(delta_time)
        is_strangе = is_visit_long(delta_time)

        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': duration,
                'is_strange': is_strangе
            }
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

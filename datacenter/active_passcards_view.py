from datacenter.models import Passcard
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
def active_passcards_view(request):
    # Программируем здесь

    # all_passcards = Passcard.objects.all()
    active_passcards = Passcard.objects.filter(is_active=True)
    # get_object_or_404(active_passcards)
    context = {
        'active_passcards': active_passcards,  # люди с активными пропусками
    }
    return render(request, 'active_passcards.html', context)



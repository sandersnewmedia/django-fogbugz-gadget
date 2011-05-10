from django.core import mail
from forms import TicketForm
import utils

def forms(request):
    try:
        choices, initial = utils.get_priorities()
        form = TicketForm(choices, initial)
    except utils.GadgetError as e:
        mail.mail_admins('FogBugz Gadget Error', e.msg)
        form = TicketForm()

    return {'ticket_form': form}

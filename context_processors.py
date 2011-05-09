from django.core import mail
from forms import TicketForm
import utils

def forms(request):
    try:
        choices, initial = utils.get_priorities()
        form = TicketForm(choices, initial)
    except utils.FogBugzError as error:
        mail.mail_admins('FogBugzError', error.msg)
        form = TicketForm()

    return {'ticket_form': form}

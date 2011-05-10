from django.http import HttpResponse
from django.core import mail
from pyquery import PyQuery as pq
from forms import TicketForm
import utils

def submit_bug(request):
    response = pq('<response></response>')

    if request.method == 'POST':
        try:
            choices, initial = utils.get_priorities()
            form = TicketForm(choices, initial, request.POST) 
        except utils.FogBugzError as error:
            mail.mail_admins('FogBugzError', error.msg)
            form = TicketForm(data=request.POST) 

        if form.is_valid():
            try:
                case = utils.submit_ticket(form.cleaned_data)
            except utils.FogBugzError as error:
                mail.mail_admins('FogBugzError', error.msg)
                raise RuntimeError(error.msg)

            response.attr('type', 'success').html(case)
        else:
            response.attr('type', 'invalid')

            # include validation errors in response
            for field, errors in form.errors.items():
                for error in errors:
                    response.append('<error field="%s">%s</error>' % (field, error))

    return HttpResponse(response.outerHtml())

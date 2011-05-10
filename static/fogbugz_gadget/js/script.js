FogBugz = {}

FogBugz.setup = function() {
    $('#fogbugz_ticket_form').submit(function() {
        FogBugz.submit_ticket();
        $('.error').remove();
        $('#fogbugz_message').html('Submitting...'); 
        return false;
    });
}

FogBugz.submit_ticket = function() {
    var fields = $('#fogbugz_ticket_form :input').filter(function() {
        if ($(this).attr('type') !== 'submit') {
            return true;
        }
    });

    var form_data = {}
    fields.each(function() {
        if ($(this).val()) {
            form_data[$(this).attr('name')] = $(this).val();
        }
    });

    var msg = $('#fogbugz_message');

    $.ajax({
        type: 'POST',
        url: $('#fogbugz_ticket_form').attr('action'),
        data: form_data, 
        success: function(response) {
            switch($(response).attr('type')) {
                case 'invalid':
                    msg.html('Form failed to validate.');
                    $(response).children('error').each(function() {
                        $('<span class="error">' + $(this).html() + '</span>').insertAfter($('label[for="id_'+$(this).attr('field')+'"]'));
                    });
                    break;
                case 'success':
                    msg.html('Case submitted: ' + $(response).html());
                    break;
            }
        },
        error: function(response) {
           msg.html('Ticket failed to submit.'); 
        }
    });
}

$(FogBugz.setup);

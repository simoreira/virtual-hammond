$(document).ready(function() {
    $('#add').on('click', function(e) {
        e.preventDefault();

        var rtttl_string = $('#rtttl').val();

        $.ajax({
            method: 'POST',
            url: '/api/create_song',
            data: { rtttl: rtttl_string }
        }).done(function(data) {
            if(data.success)
            {
                console.log(data);
                window.location = '/songs';
            }
            else
            {
                $('.form').prepend('<div class="alert alert-danger" role="alert"><i class="fa fa-exclamation-triangle"></i>Error<p>Invalid RTTTL string.</p></div>');
            }
        });
    });
});

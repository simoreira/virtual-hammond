$(document).ready(function() {
    $('#add').on('click', function(e) {
        e.preventDefault();

        var rtttl_string = $('#rtttl').val();

        $.ajax({
            method: 'POST',
            url: '/api/create_song',
            data: { rtttl: rtttl_string }
        })
        .done(function(data) {
            console.log(data);

            if(data.success)
            {
                $('.form').prepend('<div class="alert alert-success" role="alert"><i class="fa fa-check-circle"></i>Success<p>Song added successfully!</p></div>');
            }
            else
            {
                $('.form').prepend('<div class="alert alert-danger" role="alert"><i class="fa fa-exclamation-triangle"></i>Error<p>Invalid song information.</p></div>');
            }
        });
    });
});

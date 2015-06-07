$(document).ready(function() {
    $('#add').on('click', function(e) {
        e.preventDefault();

        var rtttl_string = $('#rtttl').val();
        var song_id;

        $.ajax({
            method: 'POST',
            url: '/api/create_song',
            data: { rtttl: rtttl_string }
        })
        .done(function(data) {
            console.log(data);

            if(data.success)
            {
                song_id = data.data.id;
            }
            else
            {
                $('.form').prepend('<div class="alert alert-danger" role="alert"><i class="fa fa-exclamation-triangle"></i>Error<p>Invalid song information.</p></div>');
            }
        });

        var registry = $('#registry').val();
        var effects = [];

        $("input:checkbox:checked").each(function() {
            effects.push($(this).val());
        });

        // Prepare array into CSV for AJAX request
        effects = effects.join(',');

        $.ajax({
            method: 'POST',
            url: '/api/create_interpretation',
            data: { song_id: song_id, registry: registry, effects: effects }
        })
        .done(function(data) {
            console.log(data);

            if(data.success)
            {
                window.location = '/songs';
            }
            else
            {
                $('.form').prepend('<div class="alert alert-danger" role="alert"><i class="fa fa-exclamation-triangle"></i>Error<p>Invalid song information.</p></div>');
            }
        });
    });
});

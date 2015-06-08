var interpret = function(id) {
    $('#song__interpret--'+id).show();
    $('#song__interpretations--'+id).hide();

    $('#interpret--'+id).on('click', function() {
        var registry = $('#registry').val();
        var effects = [];

        $("input:checkbox:checked").each(function()
        {
            effects.push($(this).val());
        });

        // Prepare effects array to CSV for AJAX request
        effects = effects.join(',');
        console.log(effects);

        $.ajax({
            method: 'POST',
            url: '/api/create_interpretation',
            data: { song_id: id, registry: registry, effects: effects }
        }).done(function(data) {
            console.log(data);

            if(data.success)
            {
                $('#song__interpret__alert--'+id).html('<div class="alert alert-success" style="clear:both" role="alert"><i class="fa fa-check-circle"></i>Success<p>Interpretation created successfuly!</p></div>');
            }
            else
            {
                $('#song__interpret__alert--'+id).html('<div class="alert alert-danger" style="clear:both" role="alert"><i class="fa fa-exclamation-triangle"></i>Error<p>Something went wrong.</p></div>');
            }
        });
    });

    $('#interpret--'+id+'--close').on('click', function() {
        $('#song__interpret--'+id).hide();
    });
};

var getInterpretations = function(id) {
    var waveFilesList = [];
    $('#song__interpretations--'+id).show();

    $.ajax({
        method: 'GET',
        url: '/api/list_song_files',
        async: false,
        data: { id: id }
    }).done(function(data) {
        if(data.success)
        {
            $('#song__interpretation--' + id).show();
            $('#song__interpret--' + id).hide();

            waveFilesList = data.data.wave_files;
        }
        else
        {
            $('#song__interpretation--' + id).append('<div class="alert alert-danger" role="alert"><i class="fa fa-exclamation-triangle"></i>Error<p>No interpretations for this song.</p></div>');
        }
    });

    console.log(waveFilesList);
    var htmlstring = '';

    if(!waveFilesList.length == 0)
    {
        waveFilesList.forEach(function(waveFile) {
            htmlstring += '<div class="panel panel-default" style="clear:both">';
                htmlstring += '<div class="panel-heading"> Effects: ' + (waveFile['effects'] ? waveFile['effects'].replace(',', ', ') : 'none') + '</div>';
                htmlstring += '<div class="panel-body">';
                    htmlstring += '<div><audio controls><source src="' + waveFile['wave_file'] + '" type="audio/wav"></audio></div>';
                    htmlstring += '<button class="btn btn-primary btn-fork" onclick="forkInterpretation(' + waveFile['id'] + ', "' + waveFile['registry'] + '", "' + waveFile['effects'] + '")"><i class="fa fa-code-fork"></i>Fork</button>';
                    htmlstring += '<div class="btn-group">';
                        htmlstring += '<button class="btn btn-success" onclick="voteForInterpretation(' + waveFile['id'] + ', 1)"><i class="fa fa-thumbs-up"></i></button>';
                        htmlstring += '<button class="btn btn-danger" onclick="voteForInterpretation(' + waveFile['id'] + ', -1)"><i class="fa fa-thumbs-down"></i></button>';
                    htmlstring += '</div>';
                    htmlstring += '<button class="btn btn-default" style="margin-left: 10px">' + waveFile['votes'] + ' votes </button>';
                    htmlstring += '<div id="song__votes__alert--' + waveFile['id'] + '"></div>';
                htmlstring += '</div>';
            htmlstring += '</div>';
        });
    }
    else
    {
        htmlstring = '<div class="alert alert-danger" style="clear:both" role="alert"><i class="fa fa-exclamation-triangle"></i>Error<p>There are no interpretations for this song.</p></div>';
    }

    $('#song__interpretation--' + id + '').html(htmlstring);
};

var forkInterpretation = function(id, registry, effects) {
    $('#song__interpret--'+id).show();

    console.log(id);
    console.log(registry);
    console.log(effects);
};

var voteForInterpretation = function(id, vote) {
    $.ajax({
        method: 'GET',
        url: '/api/submit_vote',
        data: { id: id,     vote: vote }
    }).done(function(data) {
        if(data.success)
        {
            $('#song__votes__alert--'+id).append('<div class="alert alert-success" style="margin-top: 20px" role="alert" style="clear:both"><i class="fa fa-exclamation-triangle"></i>Success<p>Vote was sent successfuly.</p></div>');
        }
        else
        {
            $('#song__votes__alert--'+id).append('<div class="alert alert-error" style="margin-top: 20px" role="alert" style="clear:both"><i class="fa fa-exclamation-triangle"></i>Error<p>Vote was not sent due to an error.</p></div>');
        }
    });
};

$(document).ready(function() {
    $.ajax({
        method: 'GET',
        url: '/api/list_songs'
    }).done(function(data) {
        var songs = data.data.songs;

        if(songs == null)
        {
            $('#songs').append('<div class="alert alert-danger" role="alert"><i class="fa fa-exclamation-triangle"></i>Error<p>There are no songs in the database yet.</p></div>');
        }

        new Vue({
            el: '#song',
            data: {
                songs: songs
            }
        });

    });
});

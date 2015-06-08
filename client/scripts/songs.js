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
                $('#song__interpret--'+id +' .form' + id).append('<div class="alert alert-success" role="alert"><i class="fa fa-exclamation-check-circle"></i>Success<p>Interpretation created successfuly!</p></div>');
            }
            else
            {
                $('#song__interpret--'+id +' .form' + id).append('<div class="alert alert-danger" role="alert"><i class="fa fa-exclamation-triangle"></i>Error<p>Something went wrong.</p></div>');
            }
        });
    });

    $('#interpret--'+id+'--close').on('click', function() {
        $('#song__interpret--'+id).hide();
    });
};

var getInterpretations = function(id) {
    var waveFilesList = [];

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

    waveFilesList.forEach(function(waveFile) {
        htmlstring += '<div class="well" style="clear:both">';
            htmlstring += '<div><audio controls><source src="' + waveFile['wave_file'] + '" type="audio/wav"></audio></div>';
            htmlstring += '<button class="btn btn-primary btn-fork" onclick="forkInterpretation(' + waveFile['id'] + ')"><i class="fa fa-code-fork"></i>Fork</button>';
            htmlstring += '<div class="btn-group">';
                htmlstring += '<button class="btn btn-success" onclick="voteForInterpretation(' + waveFile['id'] + ', 1)"><i class="fa fa-thumbs-up"></i></button>';
                htmlstring += '<button class="btn btn-danger" onclick="voteForInterpretation(' + waveFile['id'] + ', -1)"><i class="fa fa-thumbs-down"></i></button>';
            htmlstring += '</div>';
            htmlstring += '<btn class="btn btn-default" style="margin-left: 10px">' + waveFile['votes'] + ' votes </span>';
        htmlstring += '</div>';
    });

    $('#song__interpretation--' + id + '').html(htmlstring);
};

var forkInterpretation = function(id) {

};


var voteForInterpretation = function(id) {

};

$(document).ready(function() {
    $.ajax({
        method: 'GET',
        url: '/api/list_songs'
    }).done(function(data) {
        var songs = data.data.songs;

        new Vue({
            el: '#song',
            data: {
                songs: songs
            }
        });
    });
});

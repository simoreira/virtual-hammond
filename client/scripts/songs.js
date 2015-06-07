var interpret = function(id) {
    $('.song__interpret--' + id).show();

    $.ajax({
        method: 'POST',
        url: '/api/create_interpretation',
        data: {song_id: id, registry: registry, effects: effects}
    }).done(function(data) {
        console.log(data);
    });
};

var getInterpretations = function(id) {
    $.ajax({
        method: 'GET',
        url: '/api/list_song_files',
        data: { id: id }
    }).done(function(data) {
        if(data.success && data.length > 0)
        {
            $('.song__interpretations--' + id).show();

            console.log(data);
            var wave_files = data.data.wave_files;

            wave_files.forEach(function(wave_file) {
                $('#song__interpretation').append('<div><audio controls><source src="' + wave_file['wave_file'] + '" type="audio/wav"></audio></div>');
            });
        }
        else
        {
            $('#song__interpretation--' + id).append('<div class="alert alert-danger" role="alert"><i class="fa fa-exclamation-triangle"></i>Error<p>No interpretations for this song.</p></div>');
        }
    });
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

    var interpret = function(song_id) {
        if($('.song__interpret--'+song_id).is(":visible"))
        {
            $('.song__interpret--'+song_id).show();
        }
        else
        {
            $('.song__interpret--'+song_id).hide();
        }

        $('/api/create_interpretation', {song_id: song_id, registry: registry, effects: effects}, function(data) {
            console.log(data);
        });

        console.log(id)
    }

    $('#interpret').on('click', function(e) {
        e.preventDefault();

        console.log('banana');

        window.location = '/interpret';
    });

    $('#interpretations').on('click', function(e) {
        e.preventDefault();

        window.location = '/interpret';
    });
});

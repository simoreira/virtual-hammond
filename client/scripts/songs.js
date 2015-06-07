$(document).ready(function() {
    $.ajax({
        method: 'GET',
        url: '/api/list_songs'
    }).done(function(data) {
        console.log(data.data.songs);

        var songs = data.data.songs;

        new Vue({
            el: '#song',
            data: {
                songs: songs
            }
        });
    });

    $('#interpret').on('click', function(e) {
        e.preventDefault();

        window.location = '/interpret';
    });
});

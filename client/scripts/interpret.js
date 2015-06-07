$(document).ready(function() {
    $('#interpret').on('click', function(e) {
        e.preventDefault();

        var song_id = $('#song_id').val();
        var registry = $('#registry').val();
        var effects = [];

        $("input:checkbox:checked").each(function()
        {
            effects.push($(this).val());
        });

        $('/api/create_interpretation', {song_id: song_id, registry: registry, effects: effects}, function(data) {
            console.log(data);
        });
    });
});

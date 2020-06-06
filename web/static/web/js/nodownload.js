$(document).ready(function() {
    audios = $('audio');
    $.each(audios, function(_, _) {
        $(this).prop("controlsList", "nodownload");
    }); 
});
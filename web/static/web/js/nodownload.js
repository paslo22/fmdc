$(document).ready(function() {
    document.addEventListener('contextmenu', event => event.preventDefault());
    audios = $('audio');
    $.each(audios, function(_, _) {
        $(this).prop("controlsList", "nodownload");
    }); 
});
$(document).ready(function($) {
	var supportsAudio = !!document.createElement('audio').canPlayType;

	var getAudio = function(index,tracks) {
		return tracks[index];
	}

	var player = function(albumId) {
		if (supportsAudio) {
			var index = 0,
				playing = false,
				tracks = $('#'+albumId+'>audio'),
				trackCount = tracks.length;
			$.each(tracks, function(index, val) {
				$(this).unbind('play').unbind('pause').unbind('ended');
				$(this).bind('play', function() {
					playing = true;
				}).bind('pause', function() {
					playing = false;
				}).bind('ended', function() {
					if ((index + 1) < trackCount) {
						index++;
						audio = getAudio(index,tracks);
						audio.play();
					} else {
						playing = false;
						index = 0;
					}
				});
			});
			audio = getAudio(index,tracks);
			audio.play();		
		}else{
			console.log('No se puede reproducir')
		}		
	}
	$('.playAll').click(function(e) {
		e.preventDefault();
		var albumId = $(this).attr('data-albumid');
		player(albumId);
	});
});

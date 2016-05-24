$(document).ready(function($) {
	(function() {
		var galeria = $('.img')
		var alturaLoading = galeria.height();
		var anchoLoading = galeria.width();
		$('.loading').height(alturaLoading - 123);
		$('.loading').width(anchoLoading);
	})()
});

$(window).load(function() {
	$('.loading').hide('slow');
});
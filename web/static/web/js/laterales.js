$(document).ready(function() {
	(function() {

		var images = []

		var crearImagenes = function(url) {
			var newImg = new Image();
			newImg.src = url;
			newImg.className = 'lateral hidden-xs';
			return newImg;
		}

		var ubicarImagenes = function(img1,img2,top,lado) {
			img1.style.top = top+'px';
			img2.style.top = top+'px';
			if (lado=='left') {
				img1.className = 'lateral lateral-left visible-lg-block lateral-active';
				img2.className = 'lateral lateral-left visible-lg-block lateral-delay';
			} else {
				img1.className = 'lateral lateral-right visible-lg-block lateral-active';
				img2.className = 'lateral lateral-right visible-lg-block lateral-delay';
			}
			$('body>.container').prepend(img1);
			$('body>.container').prepend(img2);
		}

		$.ajax({
			url: '/imagenesLaterales/',
			type: 'GET',
		})
		.done(function(data) {
			$.each(JSON.parse(data), function(index, val) {
				images.push(crearImagenes(val));
			});
			for (var i = 0; i < 3; i++) {
				ubicarImagenes(images.pop(),images.pop(),200*i,'left')
			}
			for (var i = 0; i < 3; i++) {
				ubicarImagenes(images.pop(),images.pop(),200*i,'right')
			}
		})		
	})()
});
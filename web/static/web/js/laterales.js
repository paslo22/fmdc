function hideAllImages() {
	let images = document.getElementsByClassName('lateral');
	for (i = 0; i < images.length;i++ ) {
		images[i].style.display = "none";
	}
}

function loadLaterales() {
	let images = []
	
	function crearImagenes(url) {
		var newImg = new Image();
		newImg.src = url;
		newImg.className = 'lateral';
		newImg.style.display = "none"
		return newImg;
	}

	function ubicarImagenes(img1, top, lado) {
		img1.style.top = top + 'px';
		img1.className = `lateral lateral-${lado}`
		img1.style.display = "block"
		$('body>.container').prepend(img1);
	}

	$.ajax({
		url: '/imagenesLaterales/',
		type: 'GET',
	})
	.done(function(data) {
		hideAllImages()
		$.each(JSON.parse(data), function(_, val) {
			images.push(crearImagenes(val));
		});
		for (var i = 0; i < 3; i++) {
			ubicarImagenes(images.pop(), 200*i,'left')
		}
		for (var i = 0; i < 3; i++) {
			ubicarImagenes(images.pop(), 200*i,'right')
		}
	})	
	.fail(function(err){
		console.log(err)
	})	
}



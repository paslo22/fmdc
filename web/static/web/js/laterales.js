function loadLaterales() {
	let images = []
	
	function crearImagenes(url) {
		var newImg = new Image();
		newImg.src = url;
		newImg.className = 'lateral hidden-xs';
		console.log(newImg)
		return newImg;
	}

	function ubicarImagenes(img1, img2, top, lado) {
		img1.style.top = top + 'px';
		img2.style.top = top + 'px';
		
		img1.className = `lateral lateral-${lado} visible-lg-block`
		img2.className = `lateral lateral-${lado} visible-lg-block`
		$('body>.container').prepend(img1);
		$('body>.container').prepend(img2);
	}

	$.ajax({
		url: '/imagenesLaterales/',
		type: 'GET',
	})
	.done(function(data) {
		console.log(data)
		$.each(JSON.parse(data), function(_, val) {
			images.push(crearImagenes(val));
			console.log(images)
		});
		console.log(images.length)
		for (var i = 0; i < 3; i++) {
			ubicarImagenes(images.pop(),images.pop(),200*i,'left')
		}
		for (var i = 0; i < 3; i++) {
			ubicarImagenes(images.pop(),images.pop(),200*i,'right')
		}
	})	
	.fail(function(err){
		console.log(err)
	})	
}



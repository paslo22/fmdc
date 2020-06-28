function loadLaterales() {
	let images = []

	function clearImages() {
		let imagesToDelete = document.getElementsByClassName('lateral')
		for (let index = 0; index < imagesToDelete.length; index++) {
			imagesToDelete[index].style.visibility = 'hidden'
		}
	}
	
	function crearImagenes(url) {
		var newImg = new Image();
		newImg.src = url;
		newImg.className = 'lateral hidden-xs';
		return newImg;
	}

	function ubicarImagenes(img1, top, lado) {
		img1.style.top = top + 'px';
		img1.className = `lateral lateral-${lado} visible-lg-block`
		$('body>.container').prepend(img1);
	}

	$.ajax({
		url: '/imagenesLaterales/',
		type: 'GET',
	})
	.done(function(data) {
		clearImages()
		$.each(JSON.parse(data), function(_, val) {
			images.push(crearImagenes(val));
		});
		for (var i = 0; i < 3; i++) {
			ubicarImagenes(images.pop(),200*i,'left')
		}
		for (var i = 0; i < 3; i++) {
			ubicarImagenes(images.pop(),200*i,'right')
		}
	})	
	.fail(function(err){
		console.log(err)
	})	
}



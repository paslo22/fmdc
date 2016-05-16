$(document).ready(function() {
	searchsForms = $('.searchForm');
	$.each(searchsForms, function(index, val) {
		$(this).submit(function(event) {
			event.preventDefault();
			var where = $(this).attr('data-source');
			var data = $(this).serializeArray()[0].value;
			if (data) {
				window.location.pathname = where+'/' +  data+'/';
			}
		});
	});
});
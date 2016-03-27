$(document).ready(function() {
	$('#buscar').click(function(event) {
		event.preventDefault();
		var nameSearch= $('#name');
		window.location.pathname = 'web/'+nameSearch.attr('data-source')+'/' +  nameSearch.val();
	});
});
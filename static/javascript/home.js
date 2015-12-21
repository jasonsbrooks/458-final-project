$(document).ready(function(){
	setTimeout(function(){
        $('#preloader').fadeOut('slow',function(){$(this).remove();});
    }, 1000);
});

$(window).ready(function() {
	var left, width, cont = "#q-cont";
	$('span').click(function() {
		$(this).css("background", "#5a6");
		$('.re').css("background", "#d90");
		next();
	});
	$('.re').click(function() {
		$(".op").css("background", "#d90");
		$('.re').css("background", "#5a6");
		$(cont).css("left", "0px");
	});

	function next() {
		width = $(cont).width() / 4;
		left = $(cont).css("left").slice(0, -2) * 1;
		left -= width;
		$(cont).css("left", left + "px");
	}
});
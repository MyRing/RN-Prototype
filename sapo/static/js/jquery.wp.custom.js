$(document).ready(function() {
	//Carousels
	$('.carousel').carousel({
		interval: 5000,
		pause	: 'hover'
	});
	// Sortable list
	$('#ulSorList').mixitup();
	// Fancybox
	$(".theater").fancybox();
	// Fancybox	
	$(".ext-source").fancybox({
		'transitionIn'		: 'none',
		'transitionOut'		: 'none',
		'autoScale'     	: false,
		'type'				: 'iframe',
		'width'				: '50%',
		'height'			: '60%',
		'scrolling'   		: 'no'
	});
	// Scroll to top
	$().UItoTop({ easingType: 'easeOutQuart' });
	// Inview animations
	$.fn.waypoint.defaults = {
		context: window,
		continuous: true,
		enabled: true,
		horizontal: false,
		offset: 300,
		triggerOnce: false
	}
	$('.animate-in-view, .chart').waypoint(function(direction) {
		var barColor;
		// Easy Pie Chart
		$(".chart").easyPieChart({
			size:150,
			easing: 'easeOutBounce',
			onStep: function(from, to, percent) {
				$(this.el).find('.percent').text(Math.round(percent));
			},
			barColor:'#FFF',
			delay: 3000,
			trackColor:'rgba(255,255,255,0.2)',
			scaleColor:false,
			lineWidth:16,
			lineCap:'butt'
		});
	});
	$("#btnSignIn").click(function(){
		$("#dropdownForm").hide();
		$("#dropdownProfile").fadeIn(300);	
		return false;
	});
	// Search function
	$("#cmdSearch, #cmdSearchCollapse").click(function(){
		$("#divSearch").fadeIn(300);
		return false;	
	});
	$("#cmdCloseSearch").click(function(){
		$("#divSearch").fadeOut(300);	
	});
});

$(window).resize(function(){

});
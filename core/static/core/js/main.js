/*
	Main JS for Gislaine Teles Engenharia
*/

(function($) {

	var	$window = $(window),
		$body = $('body'),
		$header = $('#header'),
		$banner = $('#banner');

	// Breakpoints.
		breakpoints({
			wide:      [ '1281px',  '1680px' ],
			normal:    [ '981px',   '1280px' ],
			narrow:    [ '737px',   '980px'  ],
			narrower:  [ '737px',   '840px'  ],
			mobile:    [ '481px',   '736px'  ],
			mobilep:   [ null,      '480px'  ]
		});

	// Play initial animations on page load.
		$window.on('load', function() {
			window.setTimeout(function() {
				$body.removeClass('is-preload');
			}, 100);
		});

	// Header.
		$banner.each(function() {

			var $this = $(this),
				$header = $('#header');

			if ($header.hasClass('alt')) {
				$window.on('resize', function() { $window.trigger('scroll'); });

				$this.scrollex({
					bottom:		$header.outerHeight(),
					terminate:	function() { $header.removeClass('alt'); },
					enter:		function() { $header.addClass('alt'); },
					leave:		function() { $header.removeClass('alt'); }
				});
			}

		});

	// Smooth scroll for internal links
	$('a[href*="#"]').not('[href="#"]').not('[href="#0"]').click(function(event) {
		if (
			location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && 
			location.hostname == this.hostname
		) {
			var target = $(this.hash);
			target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
			if (target.length) {
				event.preventDefault();
				$('html, body').animate({
					scrollTop: target.offset().top - 70
				}, 1000);
			}
		}
	});

	// Mobile menu toggle
	$('.mobile-menu-toggle').on('click', function() {
		$('#nav').toggleClass('nav-visible');
	});

	// Form validation enhancement
	$('form').on('submit', function() {
		var valid = true;
		$(this).find('input[required], textarea[required]').each(function() {
			if (!$(this).val()) {
				valid = false;
				$(this).addClass('error-input');
			} else {
				$(this).removeClass('error-input');
			}
		});
		
		if (!valid) {
			alert('Por favor, preencha todos os campos obrigatórios.');
			return false;
		}
		return true;
	});

	// Input focus effects
	$('input, textarea').focus(function() {
		$(this).parent().addClass('input-focused');
	}).blur(function() {
		if (!$(this).val()) {
			$(this).parent().removeClass('input-focused');
		}
	});

	// WhatsApp button pulse animation
	$('.logo-float').hover(
		function() {
			$(this).css('animation', 'none');
		},
		function() {
			$(this).css('animation', 'pulse 2s infinite');
		}
	);

})(jQuery);

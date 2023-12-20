$(document).ready(function() {
	// Sets Colour Of Submit Button
	$('#submitButton').css('background-color', 'grey');

	// When Hovering Over Submit Button Change Colour
	$('#submitButton').hover(
		function() {
			// When Mouse Is On Submit Button Colour Changes To Green
			$(this).css('background-color', 'green');
		},
		function() {
			// When Mouse Is On Submit Button Colour Changes To Grey
			$(this).css('background-color', 'grey');
		}
	);
});
document.addEventListener('DOMContentLoaded', function() {

	// Find ID 'contactForm'
	var form = document.getElementById('contactForm');

	form.addEventListener('submit', function(event) {
		event.preventDefault(); 

		// Hides Forms
		form.style.display = 'none';

		// Displays Thank You Message
		var thankYouMessage = document.createElement('p');
		thankYouMessage.textContent = 'Thank you for writing to us. We will get back to you as soon as possible.';
		form.parentNode.insertBefore(thankYouMessage, form.nextSibling);
	});

});
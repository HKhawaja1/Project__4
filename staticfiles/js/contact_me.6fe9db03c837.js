$(function() {

	$("#contactForm input,#contactForm textarea").jqBootstrapValidation({
		preventSubmit: true,
		submitError: function($form, event, errors) {
			// Additional Error Messages
		},
		submitSuccess: function($form, event) {
			event.preventDefault();
			// Get Values From FORM
			var name = $("input#name").val();
			var email = $("input#email").val();
			var phone = $("input#phone").val();
			var message = $("textarea#message").val();
			var firstName = name; // For Success/Failure Message
			// Check For Any Whitespaces In Name For Success/Fail message
			if (firstName.indexOf(' ') >= 0) {
				firstName = name.split(' ').slice(0, -1).join(' ');
			}
			$this = $("#sendMessageButton");
			$this.prop("disabled", true); // Disable Submit Until AJAX Is Finished
			$.ajax({
				url: "././mail/contact_me.php",
				type: "POST",
				data: {
					name: name,
					phone: phone,
					email: email,
					message: message
				},
				cache: false,
				success: function() {
					// Success Message
					$('#success').html("<div class='alert alert-success'>");
					$('#success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
						.append("</button>");
					$('#success > .alert-success')
						.append("<strong>Your message has been sent. </strong>");
					$('#success > .alert-success')
						.append('</div>');
					//Clear Fields
					$('#contactForm').trigger("reset");
				},
				error: function() {
					// Fail Message
					$('#success').html("<div class='alert alert-danger'>");
					$('#success > .alert-danger').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
						.append("</button>");
					$('#success > .alert-danger').append($("<strong>").text("Sorry " + firstName + ", it seems that my mail server is not responding. Please try again later!"));
					$('#success > .alert-danger').append('</div>');
					//Clear Fields
					$('#contactForm').trigger("reset");
				},
				complete: function() {
					setTimeout(function() {
						$this.prop("disabled", false); // Turn Submit Button Back On When AJAX Is Finished
					}, 1000);
				}
			});
		},
		filter: function() {
			return $(this).is(":visible");
		},
	});

	$("a[data-toggle=\"tab\"]").click(function(e) {
		e.preventDefault();
		$(this).tab("show");
	});
});

$('#name').focus(function() {
	$('#success').html('');
});
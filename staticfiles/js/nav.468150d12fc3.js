document.addEventListener("DOMContentLoaded", function() {
	// Checks If User Is Logged In Or Out
	var isAuthenticated = document.getElementById('user-auth-status').value === 'True';

	// Navigation
	var loginItem = document.getElementById('nav-login');
	var logoutItem = document.getElementById('nav-logout');
	var registerItem = document.getElementById('nav-register');

	// Change Navigation Depending On If User Is Logged In Or Not
	if (isAuthenticated) {
		if (loginItem) loginItem.style.display = 'none';
		if (logoutItem) logoutItem.style.display = 'block';
		if (registerItem) registerItem.style.display = 'none'; // Hide Register Link
	} else {
		if (loginItem) loginItem.style.display = 'block';
		if (logoutItem) logoutItem.style.display = 'none';
		if (registerItem) registerItem.style.display = 'block'; // Shows Register Link
	}
});
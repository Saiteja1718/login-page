
const isAuthenticated = localStorage.getItem('authenticated') === 'true';

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    const loginData = {
        email: email,
        password: password
    };

    fetch('http://127.0.0.1:8000/users/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(loginData)
    })
    .then(response => {
        if (response.ok) {
            return response.json(); 
        } else if (response.status === 401) {
            alert('Login failed. Unauthenticated.');
            return Promise.reject('Unauthenticated');
        } else {
            alert('Login failed. Please check your username and password.');
            return Promise.reject('Login failed');
        }
    })
    .then(data => {
        if (data.authenticated) {
            localStorage.setItem('authenticated', 'true'); 
            window.location.href = './nav8.html'; 
           
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});


document.addEventListener('DOMContentLoaded', function() {
    
    if (isAuthenticated) {
        console.log('User is authenticated'); 
    } else {
        console.log('User is not authenticated');
    }
});

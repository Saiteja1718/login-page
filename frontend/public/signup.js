


document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('signupEmail').value;
    const password = document.getElementById('signupPassword').value;

    const signupData = {
        email: email,
        password: password
    };

    fetch('http://127.0.0.1:8000/users/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(signupData)
    })
    .then(response => {
        if (response.ok) {
            alert('User created');
            return response.json(); 
        } else if (response.status === 400) {
            localStorage.setItem('authenticated', 'false'); 
            alert('Email already exisit');
            return Promise.reject('Unauthenticated');
        } else {
            localStorage.setItem('authenticated', 'false'); 
            alert('Signup failed. Please check your username and password.');
            return Promise.reject('Login failed');
        }
    })
    .then(data => {
        if (data.authenticated) {
            localStorage.setItem('authenticated', 'true'); 
            
            //window.location.href = '/'; 
           
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

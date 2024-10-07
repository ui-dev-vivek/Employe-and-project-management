const usernameFields = document.getElementById('email');
const passwordFields = document.getElementById('password');

const loginWithAdmin = document.getElementById('loginWithAdmin');
const loginWithEmployee = document.getElementById('loginWithEmployee')
const loginWithClient = document.getElementById('loginWithClient')

loginWithAdmin.addEventListener('click', function () {
    usernameFields.value = 'admin';
    passwordFields.value = 'admin@1234';
});
loginWithEmployee.addEventListener('click', function () {
    usernameFields.value = 'employee';
    passwordFields.value = 'employee@1234';
});
loginWithClient.addEventListener('click', function () {
    usernameFields.value = 'client';
    passwordFields.value = 'client@1234';
});
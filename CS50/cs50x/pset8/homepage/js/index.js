document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('form').addEventListener('submit', function(event){
        let email = document.querySelector('#email').value;
        alert('test process ' + email);
        event.preventDefault();
    });
});
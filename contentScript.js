let url = 'http://localhost:5000/1lm4Wlpy2wU'

fetch(url).then(function(response){
    response.json().then(function(data) {
        console.log(data);
    });
    }).catch(function(error) {
        console.log('Fetch Error:', error);
    });



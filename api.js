var websiteURL;
var list;
var id;



// document.getElementById("btn").onclick = function() {get_api()};

// var get_id = getID();
// var url = "localhost:5000/summarize/api/v1.0/" + getID();

// function to make API request
// function get_api(url) {
//   fetch(url).then(function(response){
//     response.json().then(function(data) {
//         console.log(data);
//     });
//     }).catch(function(error) {
//         console.log('Fetch Error:', error);
//     });
//   }

function getID() {
    chrome.tabs.query({active : true, currentWindow : true}, (tabs)=>{
        websiteURL = tabs[0].url
        list = websiteURL.split("v=")
        list1 = list[1].split("&t=")
        if (list1[0] == "undefined"){
          id = list[1]
        }else{
          id = list1[0]
        }
    
        document.getElementById("text-box").value = id;
      })
}


function fetchSummary(url)
{
  // fetch method returns a promise.
  fetch(url).then(function(response){
    response.json().then(function(data) {
      console.log(response.status);
      console.log(response.ok);
      console.log(data);
      document.getElementById("transcript").innerHTML = "Transcript length is : " + data[2] + " words<br>";
      document.getElementById("summary").innerHTML = "Summary length is : " + data[3] + " words";
      document.getElementById("text").style.color = 'white';
      document.getElementById("text").innerHTML = "Summary is : \n" + data[1];
    });
    }).catch(function(error) {
        console.log('Fetch Error:', error);
        document.getElementById("text").innerHTML = "Transcript is not available";
        document.getElementById("text").style.color = 'red';
    });
}

getID();

setTimeout(()=> {
  fetchSummary("http://localhost:5000/"+ document.getElementById("text-box").value );
}, 2000);
const requestUrl = "url of whatever you want to make a request to";
fetch(requestUrl)
.then(response => response.json())
.then(data => {
// do something with the data the API has returned
})
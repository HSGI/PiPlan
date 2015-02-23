var data;

function loadResources() {
    var request = getXmlHttpRequest();
    request.onreadystatechange = function() {
        if(request.readyState == 4 && request.status == 200) {
            data = JSON.parse(request.responseText);
            handleData();
        }
    };
    request.open("GET", "data.json");
    request.send();
}

function handleData() {
    var date = document.querySelector("#date");
    date.textContent = data.header.weekday + " der " + data.header.date;
}

function  getXmlHttpRequest() {
	if(window.XMLHttpRequest) {
		try {
			return new XMLHttpRequest();
		} catch(e) {
		}
	} else if(window.ActiveXObject) {
		try {
			return new ActiveXObject("Msxm2.XMLTTP");
		} catch(e) {
		}
		try {
			return new ActiveXObject("Microsoft.XMLHTTP");
		} catch(e) {
		}
	}
	return null;
}
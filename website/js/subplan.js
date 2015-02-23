var data;

function loadResources() {
    loadFile("data.json", handleData);
}

function loadFile(name, callback) {
    var request = getXmlHttpRequest();
    request.onreadystatechange = function() {
        if(request.readyState == 4 && request.status == 200) {
            data = JSON.parse(request.responseText);
            callback();
        }
    };
    request.open("GET", name);
    request.send();
}

function handleData() {
    var date = document.querySelector("#date");
    date.textContent = data.header.weekday + " der " + data.header.date;
    var table = document.querySelector(".content table");
    for(var index in data.substitutes) {
        var substitute = data.substitutes[index];
        var row = document.createElement("tr");
        for(var key in substitute) {
            var cell = document.createElement("td");
            cell.textContent = substitute[key];
            row.appendChild(cell);
        }
        table.appendChild(row);
    }
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
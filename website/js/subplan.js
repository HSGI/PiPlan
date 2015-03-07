function loadResources() {
    loadFile("resources/data.json", handleData);
    loadFile("resources/ticker.txt", handleTicker);
}

function loadFile(name, callback) {
    var request = getXmlHttpRequest();
    request.onreadystatechange = function() {
        if(request.readyState == 4 && request.status == 200) {
            var data = request.responseText;
            callback(data);
        }
    };
    request.open("GET", name);
    request.send();
}

function handleData(data) {
    data = JSON.parse(data);
    var date = document.querySelector("#date");
    date.textContent = data.header.weekday + ", " + data.header.date;
    var table = document.querySelector(".content table");
    for(var index in data.substitutes) {
        var substitute = data.substitutes[index];
        var row = document.createElement("tr");
        for(var key in {"id", "lesson", "grade", "room", "description"}) {
            var cell = document.createElement("td");
            cell.textContent = substitute[key];
            row.appendChild(cell);
        }
        table.appendChild(row);
    }
}

function handleTicker(ticker) {
    var tickerElement = document.querySelector("#ticker");
	var tickerLines = ticker.split("\n");
	var ulElement = document.createElement("ul");
	ulElement.id = "newsTicker";
	for(line in tickerLines) {
		var el = document.createElement("li");
		el.textContent = tickerLines[line];
		ulElement.appendChild(el);
	}
	tickerElement.appendChild(ulElement);
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
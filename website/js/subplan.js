function loadResources() {
    loadFile("resources/plan0.json", handleData);
    //loadFile("resources/ticker.txt", handleTicker);
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
    var tableLeft = document.querySelector(".content table.left");
    var tableRight = document.querySelector(".content table.right");
    for(var index in data.substitutes) {
        var substitute = data.substitutes[index];
        var row = document.createElement("tr");
        ["id", "lesson", "grade", "room", "description"].forEach(function(key) {
            var cell = document.createElement("td");
            cell.textContent = substitute[key];
            row.appendChild(cell);
        });
        tableLeft.appendChild(row);
        tableRight.appendChild(row.cloneNode(true));
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
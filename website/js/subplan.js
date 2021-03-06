function loadResources() {
    loadFile("resources/plan0.json", handleDataForLeftTable);
    loadFile("resources/plan1.json", handleDataForRightTable);
}

function loadFile(name, callback) {
    var request = getXmlHttpRequest();
    request.onreadystatechange = function () {
        if (request.readyState == 4 && request.status == 200) {
            var data = request.responseText;
            callback(data);
        }
    };
    request.open("GET", name);
    request.send();
}

function handleDataForLeftTable(data) {
    data = JSON.parse(data);
    var date = document.querySelector("#date_left");
    date.textContent = data.header.weekday + ", " + data.header.date;
    var leftTable = document.querySelector(".content .left");
    handleDataForTable(data, leftTable);
}

function handleDataForRightTable(data) {
    data = JSON.parse(data);
    var date = document.querySelector("#date_right");
    date.textContent = data.header.weekday + ", " + data.header.date;
    var rightTable = document.querySelector(".content .right");
    handleDataForTable(data, rightTable);
}

function handleDataForTable(data, table) {
    for (var index in data.substitutes) {
        var substitute = data.substitutes[index];
        var row = document.createElement("tr");
        ["id", "lesson", "grade", "room", "description"].forEach(function (key) {
            var cell = document.createElement("td");
            cell.textContent = substitute[key];
            row.appendChild(cell);
        });
        table.appendChild(row);
    }
}

function getXmlHttpRequest() {
    if (window.XMLHttpRequest) {
        try {
            return new XMLHttpRequest();
        } catch (e) {}
    } else if (window.ActiveXObject) {
        try {
            return new ActiveXObject("Msxm2.XMLTTP");
        } catch (e) {}
        try {
            return new ActiveXObject("Microsoft.XMLHTTP");
        } catch (e) {}
    }
    return null;
}
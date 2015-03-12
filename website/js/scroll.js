var y = 0;
var maxTableHeight = 0;

function scrollToBottom() {
    window.scrollBy(0, 1);
    y += 1;

    if (y <= maxTableHeight - document.documentElement.clientHeight + overflowHeight) {
        setTimeout("scrollToBottom()", 30);
    } else {
        setTimeout("scrollToTop()", 3000);
    }
}

function scrollToTop() {
    window.scrollBy(0, -1);
    y += -1;

    if (y > 0) {
        setTimeout("scrollToTop()", 30);
    } else {
        setTimeout("scrollToBottom()", 3000);
    }
}

function setMaxTableHeight() {
    if (document.getElementsByTagName("table")[0].offsetHeight <= document.getElementsByTagName("table")[1].offsetHeight) maxTableHeight = document.getElementsByTagName("table")[0].offsetHeight
    else maxTableHeight = document.getElementsByTagName("table")[1].offsetHeight;
}
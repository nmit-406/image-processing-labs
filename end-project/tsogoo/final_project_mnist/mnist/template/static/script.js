function save() {
    var dataURL = canvas.toDataURL();
    var fd = new FormData();//dataURL);
    fd.append('img', dataURL);
    // fd.append('text', 'text');
    // console.log(dataURL);
    $.ajax({
        type: "POST",
        url: "/mnist",
        
        data: fd,
        processData: false,
        contentType: false,
        cache: false,
    }).done(function(response) {
        sendCorrectOrWrong(confirm('you wrote ' + response.prediction + '?'), response)
    });
}

function sendCorrectOrWrong(confirming, response) {
    var fd = new FormData();
    fd.append('correct_or_wrong', confirming);
    fd.append('timestamp', response.timestamp);
    fd.append('prediction', response.prediction);
    $.ajax({
        type: "POST",
        url: "/correct_or_wrong",
        
        data: fd,
        processData: false,
        contentType: false,
        cache: false,
    })
    if(confirming){console.log('correct')}
    else {console.log('wrong')}
}

var canvas, ctx, flag = false,
      prevX = 0,
      currX = 0,
      prevY = 0,
      currY = 0,
      dot_flag = false;

var x = "black",
    y = 20;

function init() {
    canvas = document.getElementById('can');
    ctx = canvas.getContext("2d");
    w = canvas.width;
    h = canvas.height;

    canvas.addEventListener("mousemove", function (e) {
        findxy('move', e)
    }, false);
    canvas.addEventListener("mousedown", function (e) {
        findxy('down', e)
    }, false);
    canvas.addEventListener("mouseup", function (e) {
        findxy('up', e)
    }, false);
    canvas.addEventListener("mouseout", function (e) {
        findxy('out', e)
    }, false);
}

function draw() {
    ctx.beginPath();
    ctx.moveTo(prevX, prevY);
    ctx.lineTo(currX, currY);
    ctx.strokeStyle = x;
    ctx.lineWidth = y;
    ctx.stroke();
    ctx.closePath();
} 

function findxy(res, e) {
    if (res == 'down') {
        prevX = currX;
        prevY = currY;
        currX = e.clientX - canvas.offsetLeft;
        currY = e.clientY - canvas.offsetTop;

        flag = true;
        dot_flag = true;
        if (dot_flag) {
            ctx.beginPath();
            ctx.fillStyle = x;
            ctx.fillRect(currX, currY, 5, 5);
            ctx.closePath();
            dot_flag = false;
        }
    }
    if (res == 'up' || res == "out") {
        flag = false;
    }
    if (res == 'move') {
        if (flag) {
            prevX = currX;
            prevY = currY;
            currX = e.clientX - canvas.offsetLeft;
            currY = e.clientY - canvas.offsetTop;
            draw();
        }
    }
}
function erase() {
    var m = confirm("Want to clear");
    if (m) {
        ctx.clearRect(0, 0, w, h);
        // document.getElementById("canvasimg").style.display = "none";
    }
}

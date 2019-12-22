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
        sendCorrectOrWrong(confirm('Та ' + response.prediction + ' гэж бичсэн үү?'), response)
        erase();
    });
}

function sendCorrectOrWrong(confirming, response) {
    
    var correction = response.prediction
    if(confirming){console.log('correct')}
    else {
        console.log('wrong')
        correction = prompt('Ямар цифр байсан юм бэ?', "");
    }

    var fd = new FormData();
    fd.append('correct_or_wrong', confirming);
    fd.append('timestamp', response.timestamp);
    fd.append('correction', correction);
    $.ajax({
        type: "POST",
        url: "/correct_or_wrong",
        
        data: fd,
        processData: false,
        contentType: false,
        cache: false,
    })
}

function disableSubmission() {
    var submit_btn = document.getElementById('btn');
    submit_btn.disabled = true;
}

function enableSubmission() {
    var submit_btn = document.getElementById('btn');
    submit_btn.disabled = false;
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

    disableSubmission();
    console.log('button disabled');
}

function draw() {
    ctx.beginPath();
    // ctx.moveTo(prevX, prevY);
    // ctx.lineTo(currX, currY);
    // ctx.strokeStyle = x;
    // ctx.lineWidth = y;
    // ctx.stroke();
    // ctx.fillRect(currX - y/2, currY - y/2, y, y);
    ctx.fillStyle = x
    ctx.arc(currX - y/4, currY - y/4, y/2, 0, 2 * Math.PI);
    ctx.fill();
    
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
            // ctx.fillRect(currX, currY, 2, 2);
            // ctx.fillRect(currX - y/2, currY - y/2, y, y);
            ctx.arc(currX - y/4, currY - y/4, y/2, 0, 2 * Math.PI);
            ctx.fill();
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
            enableSubmission();
        }
    }
}
function erase() {
    // var m = confirm("Want to clear");
    // if (m) {
        ctx.clearRect(0, 0, w, h);
        disableSubmission();
        // document.getElementById("canvasimg").style.display = "none";
    // }
}

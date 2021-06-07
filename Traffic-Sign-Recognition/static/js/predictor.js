/*const ImageInpEl = document.getElementById("imageUpload");

const PredictButton = document.getElementById("predict");

function sendToServer(file) {
    fetch('/predictor',{
        method: "POST",
        body: file
    }).then(res => {
        console.log(res);
    }).catch(console.error);
}

function onPredict() {
    let file = ImageInpEl.files[0];
    if (!file) return;
    sendToServer(file);
}

PredictButton.addEventListener("click",onPredict);*/

const ImageInpEl = document.getElementById("imageUpload");
const ImageEl = document.getElementById("preview");

function onChange(ev) {
    let file = ImageInpEl.files[0];
    if (file) {
        ImageEl.src = URL.createObjectURL(file);
    }else {
        ImageEl.src = 'some default image here';
    }
}

ImageInpEl.addEventListener("change", onChange);

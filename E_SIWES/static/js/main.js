console.log("in main gan");

var message = document.getElementById("messages");
console.log(message);
if (message) {
  console.log("in message");
  setTimeout(function () {
    message.style.display = "none";
  }, 5000);
}

const img = document.getElementById("log_img");
if (img) {
  console.log("there's image");
  img.addEventListener("change", function (event) {
    var file = event.target.files[0];
    console.log(file.name, "name");
    var fileInfo = `
  <span>File Name: ${file.name}</span>

  `;
    document.getElementById("fileInfo").innerHTML = fileInfo;
  });
}

console.log("in main gan");

var message = document.getElementById("messages");
console.log(message);
if (message) {
  console.log("in message");
  setTimeout(function () {
    message.style.display = "none";
  }, 2000);
}

const img = document.querySelector("container-fluid");
if (img) {
  console.log("there's image");
  img.addEventListener("change", function (event) {
    var file = event.target.files[0];
    console.log(file.name, "name");
    var fileInfo = `
  <p>File Name: ${file.name}</p>
  <p>File Size: ${file.size} bytes</p>
  <p>File Type: ${file.type}</p>
  `;
    document.querySelector("fileInfo").innerHTML = fileInfo;
  });
}

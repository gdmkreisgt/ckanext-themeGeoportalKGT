window.addEventListener('load', function () {
    let iframe = frames[0].document;
    let cssLink = document.createElement("link");
    cssLink.href = "/layerstack.css"; 
    cssLink.rel = "stylesheet"; 
    cssLink.type = "text/css"; 
    iframe.head.appendChild(cssLink);
})
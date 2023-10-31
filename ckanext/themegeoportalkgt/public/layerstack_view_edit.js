window.addEventListener('load', function () {
    let iframe = frames[0].document;
    let cssLink = document.createElement("link");
    cssLink.href = "/layerstack.css"; 
    cssLink.rel = "stylesheet"; 
    cssLink.type = "text/css"; 
    iframe.head.appendChild(cssLink);
    let stacked_layers = iframe.getElementsByClassName("stacked-layers");
    console.log(stacked_layers[0])
    stacked_layers[0].textContent = "";
    

    let layer1 = iframe.createElement("DIV");
    layer1.classList.add("layer-1");
    stacked_layers[0].appendChild(layer1);
})
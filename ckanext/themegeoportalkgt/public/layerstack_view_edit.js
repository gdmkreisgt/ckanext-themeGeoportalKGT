window.addEventListener('load', function () {
    let iframe = document.querySelector('[title="Data viewer"]');
    console.log(iframe)
    let innerDoc = iframe.contentDocument || iframe.contentWindow.document;
    console.log(innerDoc)

    let cssLink = document.createElement("link");
    cssLink.href = "/layerstack.css"; 
    cssLink.rel = "stylesheet"; 
    cssLink.type = "text/css"; 
    frames[0].document.head.appendChild(cssLink);
    let stacked_layers = innerDoc.getElementsByClassName("stacked-layers");
    stacked_layers[0].textContent = "";
    console.log(stacked_layers[0])

    let layer1 = innerDoc.createElement("DIV");
    layer1.classList.add("layer-1");
    stacked_layers[0].appendChild(layer1);
})
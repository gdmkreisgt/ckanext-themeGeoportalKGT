let iframe = document.querySelector('[title="Data Viewer"]');
let innerDoc = iframe.contentDocument || iframe.contentWindow.document;

let cssLink = innerDoc.createElement("link");
cssLink.href = "/layerstack.css"; 
cssLink.rel = "stylesheet"; 
cssLink.type = "text/css"; 
frames['iframe1'].innerDoc.head.appendChild(cssLink);

let stacked_layers = innerDoc.getElementsByClassName("stacked-layers");
stacked_layers.textContent = "";

let layer1 = innerDoc.createElement("DIV");
layer1.classList.add("layer-1");
stacked_layers.appendChild(layer1);
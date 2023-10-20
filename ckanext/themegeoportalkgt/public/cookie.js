function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    let expires = "expires="+d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
    let banner = document.getElementById("cookie-banner-main");
    banner.classList.remove("cookie-banner-bg-not-set");;
}
function getCookie(cname) {
    let name = cname + "=";
    let ca = document.cookie.split(';');
    for(let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
        c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
        }
    }
    return "";
}
function checkCookie(cname) {
    let cookie = getCookie(cname);
    if (cookie === "") {
        createCookieBanner();
    }
}
function createCookieBanner(){
    let main = document.getElementById("cookie-banner-main");
    main.classList.add("cookie-banner-bg-not-set")
    let banner = document.createElement("DIV");
    banner.classList.add("cookie-consent-banner");
    let inner = document.createElement("DIV");
    inner.classList.add("cookie-consent-banner__inner");
    let copy = document.createElement("DIV");
    copy.classList.add("cookie-consent-banner__copy");
    let header = document.createElement("DIV");
    header.classList.add("cookie-consent-banner__header");
    let headerContent = document.createTextNode("Diese Website verwendet Cookies");
    header.appendChild(headerContent)
    let description = document.createElement("DIV");
    description.classList.add("cookie-consent-banner__description");
    let descriptionContent = document.createTextNode("Wir verwenden Cookies, um eine reibungslose Funktionalität der Website garantieren zu können. Es werden keine Daten zu Marketing- oder Analysezwecken gesammelt und gespeichert.");
    description.appendChild(descriptionContent)
    let actions = document.createElement("DIV");
    actions.classList.add("cookie-consent-banner__actions");
    let btn = document.createElement("BUTTON");
    btn.classList.add("cookie-consent-banner__cta");
    btn.setAttribute("onclick", "setCookie('ODKGTCookie',true,30)");
    btn.textContent = "OK";
    actions.appendChild(btn);
    copy.appendChild(header);
    copy.appendChild(description);
    inner.appendChild(copy);
    inner.appendChild(actions);
    banner.appendChild(inner);
    main.appendChild(banner)
}
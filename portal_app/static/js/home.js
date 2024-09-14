const menu = document.querySelector(".menu");

menu.addEventListener("click", function () {
    expandSidebar();
});

function expandSidebar() {
    document.querySelector("body").classList.toggle("short");
    let keepSidebar = document.querySelectorAll("body.short");
    if (keepSidebar.length === 1) {
        localStorage.setItem("keepSidebar", "true");
    } else {
        localStorage.removeItem("keepSidebar");
    }
}

function showStoredSidebar() {
    if (localStorage.getItem("keepSidebar") === "true") {
        document.querySelector("body").classList.add("short");
        showHover();
        getSearch();
    }
}

showStoredSidebar();
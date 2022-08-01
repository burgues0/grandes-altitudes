/* caso a gente queira colocar algum js especifico para sobescrever o do bootstrap */
const primaryNav = document.querySelector(".nav_links");
const navToggle = document.querySelector(".mobile-nav-toggle");

navToggle.addEventListener("click", () => {
    const visibility = primaryNav.getAttribute("data-visible");
    if(visibility === "false"){
        primaryNav.setAttribute("data-visible", true);
        navToggle.setAttribute("aria-expanded", true);
    }
    if(visibility === "true"){
        primaryNav.setAttribute("data-visible", false);
        navToggle.setAttribute("aria-expanded", false);
    }
});
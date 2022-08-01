/* caso a gente queira colocar algum js especifico para sobescrever o do bootstrap */
const primaryNav = document.querySelector(".nav_links");
const navToggle = document.querySelector(".mobile-nav-toggle");
const navSignIn = document.querySelector(".redir_signup");

navToggle.addEventListener("click", () => {
    const visibility = primaryNav.getAttribute("data-visible");
    if(visibility === "false"){
        primaryNav.setAttribute("data-visible", true);
        navSignIn.setAttribute("data-visible", true);
        navToggle.setAttribute("aria-expanded", true);
    }
    if(visibility === "true"){
        primaryNav.setAttribute("data-visible", false);
        navSignIn.setAttribute("data-visible", false);
        navToggle.setAttribute("aria-expanded", false);
    }
});
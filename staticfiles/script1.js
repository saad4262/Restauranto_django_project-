
const navIcon = document.querySelector("[name='nav']");
const closeIcon = document.querySelector("[name='close']");
const navMenu = document.getElementById("navMenu");

// Function to check if the screen size is large (lg) and above
function isLargeScreen() {
    return window.matchMedia("(min-width: 1024px)").matches;
}

// Function to show or hide the nav menu based on screen size
function toggleNavMenu() {
    if (isLargeScreen()) {
        navMenu.classList.remove("hidden"); // Show the nav menu on large screens
    } else {
        navMenu.classList.add("hidden"); // Hide the nav menu on small screens
    }
}

// Initial toggle based on screen size
toggleNavMenu();

// Event listeners for the nav and close icons
navIcon.addEventListener("click", () => {
    navMenu.classList.toggle("hidden");
});

closeIcon.addEventListener("click", () => {
    navMenu.classList.add("hidden");
});

// Event listener for window resize to toggle nav menu visibility
window.addEventListener("resize", toggleNavMenu);




document.addEventListener("DOMContentLoaded", function() {
    const images = document.querySelectorAll('.half1 img');
    let index = 1;
    images[0].classList.add('active');
    function showImage() {
        images.forEach(img => img.classList.remove('active'));
        images[index].classList.add('active');
        index = (index + 1) % images.length;
    }

    setInterval(showImage, 3000); // Change image every 3 seconds
});




const service= document.querySelector(".full-con7");

 Array.from(service.children).forEach(item=>{
    const duplicateNode= item.cloneNode(true)
    duplicateNode.setAttribute("aria-hidden", true)
    service.appendChild(duplicateNode);
 });
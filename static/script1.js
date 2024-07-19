
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









//  let numbersApplied = false;

// function getRandomNumber() {
//     return Math.floor(Math.random() * 100); // Adjust the range of random numbers as needed
// }

// function applyRandomNumbers() {
//     if (!numbersApplied) {
//         let userElements = document.querySelectorAll('.user');
//         let subscribersElements = document.querySelectorAll('.subscribers');
//         let downloadsElements = document.querySelectorAll('.downloads');
//         let productsElements = document.querySelectorAll('.products');

//         userElements.forEach(element => {
//             let userRandomNumber = getRandomNumber();
//             element.textContent = `${userRandomNumber}K`;
//         });

//         subscribersElements.forEach(element => {
//             let subscribersRandomNumber = getRandomNumber();
//             element.textContent = `${subscribersRandomNumber}K`;
//         });

//         downloadsElements.forEach(element => {
//             let downloadsRandomNumber = getRandomNumber();
//             element.textContent = downloadsRandomNumber;
//         });

//         productsElements.forEach(element => {
//             let productsRandomNumber = getRandomNumber();
//             element.textContent = productsRandomNumber;
//         });

//         numbersApplied = true;
//     }
// }

// function handleScroll() {
//     let numbersSection = document.querySelector('.numbers-section');
//     let numbersSectionRect = numbersSection.getBoundingClientRect();
//     if (numbersSectionRect.top < window.innerHeight && numbersSectionRect.bottom >= 0) {
//         applyRandomNumbers();
//         window.removeEventListener('scroll', handleScroll);
//     }
// }


// window.addEventListener('scroll', handleScroll);

let valueDisplays = document.querySelectorAll(".num");
let interval = 4000;

function startNumberAnimation() {
  valueDisplays.forEach((valueDisplay) => {
    let startValue = 0;
    let endValue = parseInt(valueDisplay.getAttribute("data-val"));
    let duration = Math.floor(interval / endValue);
    let counter = setInterval(function () {
      startValue += 1;
      valueDisplay.textContent = startValue;
      if (startValue == endValue) {
        clearInterval(counter);
      }
    }, duration);
  });
}

function handleScroll() {
  let container = document.querySelector(".container"); // Change this selector to match your container
  let containerRect = container.getBoundingClientRect();
  if (
    containerRect.top < window.innerHeight &&
    containerRect.bottom >= 0
  ) {
    // Add a 1-second delay before starting the animation
    setTimeout(startNumberAnimation, 1000);
    window.removeEventListener("scroll", handleScroll);
  }
}

window.addEventListener("scroll", handleScroll);










    document.addEventListener("DOMContentLoaded", function() {
        // Get the button and Container 5 elements
        const scrollButton = document.getElementById("scrollButton");
        const container5 = document.getElementById("container5");

        // Add event listener to the button
        scrollButton.addEventListener("click", function() {
            // Scroll to Container 5
            container5.scrollIntoView({ behavior: "smooth" });
        });
    });





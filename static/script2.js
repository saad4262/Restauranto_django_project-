
    // --> admin panel js :-
// add hovered class to selected list item
// let list = document.querySelectorAll(".navigation li");
// console.log(list)

// function activeLink() {
//   list.forEach((item) => {
//     item.classList.remove("hovered");
//   });
//   this.classList.add("hovered");
// }

// list.forEach((item) => item.addEventListener("mouseover", activeLink));

// // Menu Toggle
// let toggle = document.querySelector(".toggle");
// let navigation = document.querySelector(".navigation");
// let main = document.querySelector(".main");
// console.log(main)

// toggle.onclick = function () {
//   navigation.classList.toggle("active");
//   main.classList.toggle("active");
// };



let list = document.querySelectorAll(".navigation li");

function activeLink() {
  list.forEach((item) => {
    item.classList.remove("hovered");
  });
  this.classList.add("hovered");
}

list.forEach((item) => item.addEventListener("mouseover", activeLink));

// Menu Toggle
let toggles = document.querySelectorAll(".toggle");
let navigation = document.querySelector(".navigation");
let mains = document.querySelectorAll(".main");

toggles.forEach((toggle) => {
  toggle.addEventListener("click", function () {
    navigation.classList.toggle("active");
    mains.forEach((main) => {
      main.classList.toggle("active");
    }); 
   });
});










document.addEventListener("DOMContentLoaded", function () {
  const navigationLinks = document.querySelectorAll(".navigation li a");
  const dashboardLink = document.querySelector("#main-dashboard");

  navigationLinks.forEach((link) => {
      // Exclude logout link from event listener
      if (!link.classList.contains('logout-link')) {
          link.addEventListener("click", function (event) {
              event.preventDefault();

              // Hide all main divs
              const allMainDivs = document.querySelectorAll(".main");
              allMainDivs.forEach((div) => {
                  div.style.display = "none";
              });

              // Show the corresponding main div based on ID
              const clickedId = link.id.replace("main-", "");
              const mainDiv = document.getElementById(`main-${clickedId}-data`);
              mainDiv.style.display = "block";
          });
      }
  });
  dashboardLink.click();
});


  
  $(document).ready(function(){
    // Activate tooltip
    $('[data-toggle="tooltip"]').tooltip();
    
    // Select/Deselect checkboxes
    var checkbox = $('table tbody input[type="checkbox"]');
    $("#selectAll").click(function(){
      if(this.checked){
        checkbox.each(function(){
          this.checked = true;                        
        });
      } else{
        checkbox.each(function(){
          this.checked = false;                        
        });
      } 
    });
    checkbox.click(function(){
      if(!this.checked){
        $("#selectAll").prop("checked", false);
      }
    });
  });



  


  function openModal() {
    document.getElementById('addChefModal').classList.remove('hidden');
}

function closeModal() {
    document.getElementById('addChefModal').classList.add('hidden');
}

function loadFile(event) {
    var reader = new FileReader();
    reader.onload = function() {
        var output = document.getElementById('preview_img');
        output.src = reader.result;
    };
    reader.readAsDataURL(event.target.files[0]);
}
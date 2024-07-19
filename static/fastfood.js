document.addEventListener('DOMContentLoaded', () => {
    let PopupTrigger = document.querySelectorAll('.card-button');
    let CloseTrigger = document.querySelectorAll('.closeTrigger');

    PopupTrigger.forEach(button => {
        button.addEventListener('click', (event) => {
            let id = event.target.id;
            let counter = id.split('-')[1];
            const popup = document.getElementById(`popupContainer-${counter}`);

            // Add 'open-popup' class to display the pop-up
            popup.classList.add('open-popup');

            // Call function to position the pop-up
            positionPopup(popup);
        });
    });

    CloseTrigger.forEach(button => {
        button.addEventListener('click', (event) => {
            let id = event.target.id;
            let counter = id.split('-')[1];
            let popup = document.getElementById(`popupContainer-${counter}`);

            // Remove 'open-popup' class to hide the pop-up
            popup.classList.remove('open-popup');
        });
    });

    // Function to position the pop-up centered in the viewport
    function positionPopup(popup) {
        const viewportHeight = window.innerHeight;
        const popupHeight = popup.offsetHeight;
        const scrollY = window.scrollY || window.pageYOffset; // Get current scroll position

        // Calculate top position to center the pop-up
        const topPosition = Math.max(0, scrollY + (viewportHeight - popupHeight) / 2);

        // Offset the top position to move the pop-up slightly lower
        const offsetTop = topPosition + 100; // Adjust this value as needed

        // Set the top position of the pop-up
        popup.style.top = `${offsetTop}px`;
    }

    
});

// let number=1;
// function countInc(){
//     number=number+1;
//     document.getElementById("countValue").innerHTML=number;
// }
// function countDec(){
//     number=number-1;
//     document.getElementById("countValue").innerHTML=number;
// }

 // Select the increment and decrement buttons
let incrementButtons = document.querySelectorAll('.CountBtn.positive');
let decrementButtons = document.querySelectorAll('.CountBtn.negative');

// Attach event listeners to the increment buttons
incrementButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Find the parent container of the button
        let container = button.closest('.counter');
        if (container) {
            // Find the count value within the container
            let countValue = container.querySelector('.CounterValue');
            if (countValue) {
                // Increment the count value
                let count = parseInt(countValue.textContent) + 1;
                countValue.textContent = count;
                updateQuantityDisplay(container, count);
            }
        }
    });
});

// Attach event listeners to the decrement buttons
decrementButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Find the parent container of the button
        let container = button.closest('.counter');
        if (container) {
            // Find the count value within the container
            let countValue = container.querySelector('.CounterValue');
            if (countValue) {
                // Decrement the count value
                let count = parseInt(countValue.textContent) - 1;
                countValue.textContent = count >= 0 ? count : 0;
                updateQuantityDisplay(container, count);
            }
        }
    });
});

   const linkCollapse =document.getElementsByClassName('collapse__link')
    var i

    for(i=0;i<linkCollapse.length;i++){
        linkCollapse[i].addEventListener('click', function(){
            const collapseMenu= this.nextElementSibling
            collapseMenu.classList.toggle('showCollapse')

            const rotate= collapseMenu.previousElementSibling
            rotate.classList.toggle('rotate')
        })
    }


 function updateUserOrder(productId, action){
     console.log("User is logged in, sending data...")
     var url= '/update_Item/'
     fetch(url, {
         method: "POST",
         headers:{
             "Content-Type": "application/json",
             'X-CSRFToken': csrftoken,
         },
         body:JSON.stringify({"productId": productId , "action" : action})
     })

     .then((response) =>{
         return response.json()
     })

     .then((data) =>{
        console.log('data:', data)
         location.reload()
     })
 }

 console.log("User:", user )


 var updateBtns = document.getElementsByClassName('update-cart')

 for (var i=0; i< updateBtns.length; i++ ) {
     updateBtns[i].addEventListener('click',function(){
         var productId = this.dataset.product
         var action = this.dataset.action
         console.log('productId:' , productId, 'action:' , action)



         updateUserOrder(productId, action)

     })

 }

 console.log('hello')


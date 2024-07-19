
let isUpdating = false; // To prevent multiple submissions

function updateUserOrder(productId, action) {
    if (isUpdating) return; // Exit if already updating
    isUpdating = true;

    console.log("User is logged in, sending data...");

    var url = '/update_Item/';
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({"productId": productId, "action": action})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log('data:', data);
        isUpdating = false;
        location.reload();
    })
    .catch((error) => {
        console.error('Error:', error);
        isUpdating = false;
    });
}

var updateBtns = document.getElementsByClassName('update-cart');

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('productId:', productId, 'action:', action);

        updateUserOrder(productId, action);
    });
}
let popup = document.getElementById("optionPopup");
function Popup(event) {
    event.preventDefault();
  
    // Get current scroll positions
    const scrollX = window.scrollX;
    const scrollY = window.scrollY;
  
    // Calculate adjusted click coordinates
    const adjustedX = event.clientX - scrollX;
    const adjustedY = event.clientY - scrollY;
  
    popup.style.visibility = 'visible';
    popup.style.display = 'flex';
  
    // Center the popup horizontally and vertically
    popup.style.top = adjustedY + 'px';
    popup.style.left = adjustedX + 'px';
    popup.style.transform = 'translate(-50%, -50%)';  // Centering using transform
  }

function ClosePopup() {
    popup.style.visibility = 'hidden';
    popup.style.display = 'none';
}

document.addEventListener("DOMContentLoaded", function () {
  // Get modal
  var modal = document.getElementById("changePasswordModal");

  // Get the button to open the modal
  var openModalBtn = document.getElementById("changePasswordBtn");

  // When the user clicks on the button, open the modal
  openModalBtn.onclick = function () {
    modal.style.display = "block";
  };

  // Get the element that closes the modal
  var closeModalBtn = document.getElementById("closeBtn");

  // When the user clicks on the close button, the modal closes
  closeModalBtn.onclick = function () {
    modal.style.display = "none";
  };

  // When the user clicks outside the modal, close the modal
  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  };
});

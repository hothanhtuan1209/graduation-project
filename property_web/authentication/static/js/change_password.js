document.addEventListener("DOMContentLoaded", function () {
  // Lấy modal
  var modal = document.getElementById("changePasswordModal");

  // Lấy nút mở modal
  var openModalBtn = document.getElementById("changePasswordBtn");

  // Khi người dùng click vào nút, mở modal
  openModalBtn.onclick = function () {
    modal.style.display = "block";
  };

  // Lấy phần tử đóng modal
  var closeModalBtn = document.getElementById("closeBtn");

  // Khi người dùng click vào nút đóng, đóng modal
  closeModalBtn.onclick = function () {
    modal.style.display = "none";
  };

  // Khi người dùng click bên ngoài modal, đóng modal
  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  };
});

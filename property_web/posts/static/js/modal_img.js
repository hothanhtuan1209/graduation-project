document.addEventListener("DOMContentLoaded", function () {
  const images = document.querySelectorAll(".posts-image");

  images.forEach(function (image) {
    image.addEventListener("click", function () {
      const overlay = document.createElement("div");
      overlay.className = "overlay";

      const imageList = document.createElement("div");
      imageList.className = "image-list";

      const allImages = document.querySelectorAll(".posts-image");
      allImages.forEach(function (img) {
        const imgItem = document.createElement("img");
        imgItem.src = img.src;
        imgItem.alt = img.alt;
        imageList.appendChild(imgItem);
      });

      overlay.appendChild(imageList);

      const closeButton = document.createElement("span");
      closeButton.className = "close-button";
      closeButton.innerHTML = "&times;";

      imageList.appendChild(closeButton);

      document.body.appendChild(overlay);

      closeButton.addEventListener("click", function () {
        overlay.remove();
      });

      overlay.addEventListener("click", function (event) {
        if (event.target === overlay) {
          overlay.remove();
        }
      });
    });
  });
});

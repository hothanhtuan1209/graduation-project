let FILES = {};
  const fileTempl = document.getElementById("file-template"),
    imageTempl = document.getElementById("image-template"),
    empty = document.getElementById("empty");
  // use to store pre selected files

  function addFile(target, file) {
    const isImage = file.type.match("image.*"),
      objectURL = URL.createObjectURL(file);

    const clone = isImage
      ? imageTempl.content.cloneNode(true)
      : fileTempl.content.cloneNode(true);

    clone.querySelector("h1").textContent = file.name;
    clone.querySelector("li").id = objectURL;
    clone.querySelector(".delete").dataset.target = objectURL;
    clone.querySelector(".size").textContent =
      file.size > 1024
        ? file.size > 1048576
          ? Math.round(file.size / 1048576) + "mb"
          : Math.round(file.size / 1024) + "kb"
        : file.size + "b";

    isImage &&
      Object.assign(clone.querySelector("img"), {
        src: objectURL,
        alt: file.name,
      });

    empty.classList.add("hidden");
    target.prepend(clone);
    FILES[objectURL] = file;
  }

  const gallery = document.getElementById("gallery"),
    overlay = document.getElementById("overlay");
  // click the hidden input of type file if the visible button is clicked
  // and capture the selected files
  const hidden = document.getElementById("hidden-input");
  document.getElementById("button").onclick = () => hidden.click();
  console.log(hidden);
  hidden.onchange = (e) => {
    const numberOfProperties = Object.keys(FILES).length;
    const sum = numberOfProperties + e.target.files.length;

    if (sum <= 12) {
      for (const file of Array.from(e.target.files).slice(0, 12)) {
        addFile(gallery, file);
      }
    } else {
      for (const file of Array.from(e.target.files).slice(
        0,
        12 - numberOfProperties
      )) {
        addFile(gallery, file);
      }
    }
  };
  // use to check if a file is being dragged
  const hasFiles = ({ dataTransfer: { types = [] } }) =>
    types.indexOf("Files") > -1;

  // use to drag dragenter and dragleave events.
  // this is to know if the outermost parent is dragged over
  // without issues due to drag events on its children
  let counter = 0;

  // reset counter and append file to gallery when file is dropped
  function dropHandler(ev) {
    ev.preventDefault();
    const numberOfProperties = Object.keys(FILES).length;
    const sum = numberOfProperties + ev.dataTransfer.files.length;

    if (numberOfProperties < 12 || sum <= 12) {
      for (const file of ev.dataTransfer.files) {
        addFile(gallery, file);
        overlay.classList.remove("draggedover");
        counter = 0;
      }
    } else {
      alert("Đã vượt quá số ảnh cho phép");
    }
  }

  // only react to actual files being dragged
  function dragEnterHandler(e) {
    e.preventDefault();
    if (!hasFiles(e)) {
      return;
    }
    ++counter && overlay.classList.add("draggedover");
  }

  function dragLeaveHandler(e) {
    1 > --counter && overlay.classList.remove("draggedover");
  }

  function dragOverHandler(e) {
    if (hasFiles(e)) {
      e.preventDefault();
    }
  }

  // event delegation to caputre delete events
  // fron the waste buckets in the file preview cards
  gallery.onclick = ({ target }) => {
    if (target.classList.contains("delete")) {
      const ou = target.dataset.target;
      document.getElementById(ou).remove(ou);
      gallery.children.length === 1 && empty.classList.remove("hidden");
      delete FILES[ou];
    }
  };

  document.addEventListener(
    "DOMContentLoaded",
    function () {
      // Fetch all the forms we want to apply custom Bootstrap validation styles to
      var forms = document.getElementsByClassName("needs-validation");
      // Loop over them and prevent submission
      var validation = Array.prototype.filter.call(forms, function (form) {
        form.addEventListener(
          "submit",
          function (event) {
            if (
              form.checkValidity() === false ||
              Object.keys(FILES).length === 0
            ) {
              event.preventDefault();
              event.stopPropagation();
            }
            form.classList.add("was-validated");
          },
          false
        );
      });
      console.log(document.getElementById("hidden-input").value);
      var fullAddressLoad = document.getElementById("id_fullAddress");
      if (fullAddressLoad) {
        var defaultFullAddress = JSON.parse(fullAddressLoad.value);
        // Fill in the default values ​​in the corresponding fields in the form
        document.getElementById("id_city").options[0].textContent =
          defaultFullAddress.city.name;
        document.getElementById("id_city").options[0].value =
          defaultFullAddress.city.id;
        document.getElementById("id_district").options[0].textContent =
          defaultFullAddress.district.name;
        document.getElementById("id_district").options[0].value =
          defaultFullAddress.district.id;
        document.getElementById("id_ward").options[0].textContent =
          defaultFullAddress.ward.name;
        document.getElementById("id_ward").options[0].value =
          defaultFullAddress.ward.code;

        document.getElementById("id_houseNumber").value =
          defaultFullAddress.houseNumber;
        document.getElementById("id_streetName").value =
          defaultFullAddress.streetName;
      }

      var addressForm = document.getElementById("addressForm");
      if (addressForm) {
        addressForm.addEventListener("submit", function (event) {
          // Values ​​from your input
          var city = {
            name: document.getElementById("id_city").selectedOptions[0]
              .textContent,
            id: document.getElementById("id_city").selectedOptions[0].value,
          };
          var district = {
            name: document.getElementById("id_district").selectedOptions[0]
              .textContent,
            id: document.getElementById("id_district").selectedOptions[0].value,
          };
          var ward = {
            name: document.getElementById("id_ward").selectedOptions[0]
              .textContent,
            code: document.getElementById("id_ward").selectedOptions[0].value,
          };
          var houseNumber = document.getElementById("id_houseNumber").value;
          var streetName = document.getElementById("id_streetName").value;

          console.log("submit: ", district);

          // Generate full address
          var fullAddress = { houseNumber, streetName, ward, district, city };

          // Assign value to hidden input field "fullAddress"
          var fullAddressField = document.getElementById("id_fullAddress");
          if (fullAddressField) {
            fullAddressField.value = JSON.stringify(fullAddress);
          } else {
            // In case the 'fullAddress' field is not found, an error should be displayed or other handling is required
            console.error(
              "Không tìm thấy trường input ẩn để gán địa chỉ đầy đủ."
            );
            event.preventDefault(); // Prevent the form from submitting if there are errors
          }
        });
      } else {
        console.error("Không tìm thấy form để gắn sự kiện submit.");
      }
    },
    false
  );

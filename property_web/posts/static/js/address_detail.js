document.addEventListener(
  "DOMContentLoaded",
  function () {
    const addressElement = document.getElementById("address-output");

    if (addressElement) { // Kiểm tra nếu phần tử và dữ liệu tồn tại
      addressElement.innerHTML = formatAddress(addressElement.innerHTML);; // Sử dụng innerHTML để hiển thị HTML
      addressElement.style.display = 'flex';
    } else {
      console.error("Dữ liệu địa chỉ không tồn tại hoặc phần tử không được tìm thấy.");
    }
  },
  false
);

function formatAddress(addressString) {
  if (!addressString) {
    return ""; // Xử lý địa chỉ trống
  }

  try {
    const address = JSON.parse(addressString);
    let formattedAddress = "";

    if (address.houseNumber) {
      formattedAddress += address.houseNumber + ", ";
    }
    if (address.streetName) {
      formattedAddress += address.streetName + ", ";
    }
    if (address.ward) { // Sử dụng address.ward thay vì obj.ward
      formattedAddress += address.ward.name + ", ";
    }
    if (address.district) { // Sử dụng address.district
      formattedAddress += address.district.name + ", ";
    }
    if (address.city) { // Sử dụng address.city
      formattedAddress += address.city.name;
    }
    return formattedAddress; // Loại bỏ dấu phẩy và khoảng trắng ở cuối
  } catch (error) {
    console.error("Lỗi phân tích JSON địa chỉ:", error);
    return ""; // Xử lý lỗi phân tích
  }
}

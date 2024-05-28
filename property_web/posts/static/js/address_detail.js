document.addEventListener(
  "DOMContentLoaded",
  function () {
    const addressElement = document.getElementById("address-detail");
    if (addressElement) { // Check if element and data exist
      addressElement.innerHTML = formatAddress(addressElement.innerHTML);; // Use innerHTML to display HTML
      addressElement.style.display = 'flex';
    } else {
      console.error("Dữ liệu địa chỉ không tồn tại hoặc phần tử không được tìm thấy.");
    }
  },
  false
);
function formatAddress(addressString) {
  if (!addressString) {
    return ""; //Handling empty addresses
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
    if (address.ward) { // Use address.ward instead of obj.ward
      formattedAddress += address.ward.name + ", ";
    }
    if (address.district) { // Use address.district
      formattedAddress += address.district.name + ", ";
    }
    if (address.city) { // Use address.city
      formattedAddress += address.city.name;
    }
    return formattedAddress; // Remove trailing commas and spaces
  } catch (error) {
    console.error("Lỗi phân tích JSON địa chỉ:", error);
    return ""; // Handle parsing errors
  }
}

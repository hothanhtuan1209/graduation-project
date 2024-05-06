document.addEventListener(
  "DOMContentLoaded",
  function () {
    const addressElements = document.getElementsByClassName("address-post");
    console.log("here: ", addressElements.length);
    if (addressElements.length > 0) {
      for (let index = 0; index < addressElements.length; index++) {
        const element = addressElements[index];
        element.innerHTML = formatAddress(element.innerHTML);
        element.style.display = 'flex';
        console.log("here: ", element.innerHTML);
      }
    }
  },
  false
);

function isJson(str) {
  try {
    JSON.parse(str);
    return true;
  } catch (e) {
    return false;
  }
}

// Function to format the address string
function formatAddress(address) {
  const obj = JSON.parse(address);
  let addressString = "";

  if (obj.houseNumber) {
    addressString += obj.houseNumber + ", ";
  }
  if (obj.streetName) {
    addressString += obj.streetName + ", ";
  }
  if (obj.ward.name) {
    addressString += obj.ward.name + ", ";
  }
  if (obj.district.name) {
    addressString += obj.district.name + ", ";
  }
  if (obj.city.name) {
    addressString += obj.city.name;
  }
  // Remove trailing comma and space if present
  return addressString;
}

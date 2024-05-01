const addressOutput = document.getElementById('address-output');
const addressData = post.address; // Assuming you have 'post' object in your JavaScript context

// Function to format the address string
function formatAddress(address) {
  let addressString = '';
  if (address.houseNumber) {
    addressString += address.houseNumber + ', ';
  }
  if (address.streetName) {
    addressString += address.streetName + ', ';
  }
  if (address.ward.name) {
    addressString += address.ward.name + ', ';
  }
  if (address.district.name) {
    addressString += address.district.name + ', ';
  }
  if (address.city.name) {
    addressString += address.city.name;
  }
  // Remove trailing comma and space if present
  return addressString.slice(0, -2);
}

const formattedAddress = formatAddress(addressData);
addressOutput.textContent = formattedAddress;

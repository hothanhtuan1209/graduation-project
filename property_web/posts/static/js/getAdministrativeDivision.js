let responseData = [];
  let responseDistrictData = [];
  let responseWardData = [];

  const selectCityElement = document.getElementById("id_city");
  fetch(
    "https://dev-online-gateway.ghn.vn/shiip/public-api/master-data/province",
    {
      method: "GET",
      headers: {
        Token: "f44f9dc5-05c9-11ef-b1d4-92b443b7a897",
      },
    }
  )
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      if (data.code === 200) {
        responseData = data.data;
      }
    })
    .then(() => {
      responseData.forEach((province) => {
        const option = document.createElement("option");
        option.value = province.ProvinceID;
        option.textContent = province.ProvinceName;
        selectCityElement.appendChild(option);
      });
    })
    .catch((error) => {
      console.error("There was a problem with the fetch operation:", error);
    });
  const selectDistrictElement = document.getElementById("id_district");
  const defaultDistrictOptionValue = selectDistrictElement.options[0].value;
  const defaultDistrictOptionText =
    selectDistrictElement.options[0].textContent;

  selectCityElement.onchange = (e) => {
    // Get select element from DOM
    console.log("change");
    // Get the value of province_id from the select element with id_city
    if (e.target.value) {
      // Call the API to get district data based on province_id
      fetch(
        "https://dev-online-gateway.ghn.vn/shiip/public-api/master-data/district",
        {
          method: "POST",
          headers: {
            token: "f44f9dc5-05c9-11ef-b1d4-92b443b7a897", // Token
            "Content-Type": "application/json", // Data format
          },
          // Pass data in body as JSON
          body: JSON.stringify({
            province_id: Number(e.target.value),
          }),
        }
      )
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json(); // Convert received data to JSON
        })
        .then((data) => {
          if (data.code === 200) {
            responseDistrictData = data.data;
          }
        })
        .then(() => {
          // Delete all existing options in the select element
          selectDistrictElement.innerHTML = "";
          const defaultOption = document.createElement("option");
          defaultOption.value = defaultDistrictOptionValue;
          defaultOption.textContent = defaultDistrictOptionText;
          selectDistrictElement.appendChild(defaultOption);
          // Loop through each object in the returned data and create new options for each object
          responseDistrictData.forEach((district) => {
            const option = document.createElement("option"); // Create an option element
            option.value = district.DistrictID; // Assign the value of the option to DistrictID
            option.textContent = district.DistrictName; // Assign the content of the option to DistrictName
            selectDistrictElement.appendChild(option); // Add options to the select element
          });
          console.log(responseWardData)
        })
        .catch((error) => {
          console.error("There was a problem with the fetch operation:", error);
        });
    } else {
      responseDistrictData = [];
    }
  };

  const selectWardElement = document.getElementById("id_ward");
  const defaultWardOptionValue = selectWardElement.options[0].value;
  const defaultWardOptionText = selectWardElement.options[0].textContent;
  // Catch the event when the selected district changes
  selectDistrictElement.onchange = (e) => {
    // Get the value of district_id from the select element
    const districtId = e.target.value;
    if (districtId) {
      fetch(
        "https://dev-online-gateway.ghn.vn/shiip/public-api/master-data/ward?district_id",
        {
          method: "POST", // POST method
          headers: {
            token: "f44f9dc5-05c9-11ef-b1d4-92b443b7a897", // Token
            "Content-Type": "application/json",
          },
          // Pass data in body as JSON
          body: JSON.stringify({
            district_id: Number(districtId),
          }),
        }
      )
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json(); // Convert received data to JSON
        })
        .then((data) => {
          if (data.code === 200) {
            responseWardData = data.data;
          }
        })
        .then(() => {
          // Delete all existing options in the select element
          selectWardElement.innerHTML = "";

          // Add the default option back to the top of the options list
          const defaultOption = document.createElement("option");
          defaultOption.value = defaultWardOptionValue;
          defaultOption.textContent = defaultWardOptionText;
          selectWardElement.appendChild(defaultOption);

          responseWardData.forEach((ward) => {
            const option = document.createElement("option"); // Create an option element
            option.value = ward.WardCode; // Assign the value of the option to WardID
            option.textContent = ward.WardName; // Assign the content of the option to WardName
            selectWardElement.appendChild(option); // Add options to the select element
          });

        })
        .catch((error) => {
          console.error("There was a problem with the fetch operation:", error);
        });

    } else {
      responseWardData = [];
    }
  };

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
    // Lấy select element từ DOM
    console.log("change");
    // Lấy giá trị của province_id từ select element với id_city
    if (e.target.value) {
      // Gọi API để lấy dữ liệu về quận/huyện dựa trên province_id
      fetch(
        "https://dev-online-gateway.ghn.vn/shiip/public-api/master-data/district",
        {
          method: "POST", // Phương thức GET
          headers: {
            token: "f44f9dc5-05c9-11ef-b1d4-92b443b7a897", // Token
            "Content-Type": "application/json", // Định dạng dữ liệu
          },
          // Truyền dữ liệu trong body dưới dạng JSON
          body: JSON.stringify({
            province_id: Number(e.target.value),
          }),
        }
      )
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json(); // Chuyển đổi dữ liệu nhận được thành JSON
        })
        .then((data) => {
          if (data.code === 200) {
            responseDistrictData = data.data;
          }
        })
        .then(() => {
          // Xóa tất cả các option hiện có trong select element
          selectDistrictElement.innerHTML = "";
          const defaultOption = document.createElement("option");
          defaultOption.value = defaultDistrictOptionValue;
          defaultOption.textContent = defaultDistrictOptionText;
          selectDistrictElement.appendChild(defaultOption);
          // Lặp qua mỗi object trong dữ liệu trả về và tạo option mới cho mỗi object
          responseDistrictData.forEach((district) => {
            const option = document.createElement("option"); // Tạo một option element
            option.value = district.DistrictID; // Gán giá trị của option là DistrictID
            option.textContent = district.DistrictName; // Gán nội dung của option là DistrictName
            selectDistrictElement.appendChild(option); // Thêm option vào select element
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
  // Bắt sự kiện khi select district thay đổi
  selectDistrictElement.onchange = (e) => {
    // Lấy giá trị của district_id từ select element
    const districtId = e.target.value;
    if (districtId) {
      fetch(
        "https://dev-online-gateway.ghn.vn/shiip/public-api/master-data/ward?district_id",
        {
          method: "POST", // Phương thức POST
          headers: {
            token: "f44f9dc5-05c9-11ef-b1d4-92b443b7a897", // Token
            "Content-Type": "application/json", // Định dạng dữ liệu
          },
          // Truyền dữ liệu trong body dưới dạng JSON
          body: JSON.stringify({
            district_id: Number(districtId),
          }),
        }
      )
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json(); // Chuyển đổi dữ liệu nhận được thành JSON
        })
        .then((data) => {
          if (data.code === 200) {
            responseWardData = data.data;
          }
        })
        .then(() => {
          // Xóa tất cả các option hiện có trong select element
          selectWardElement.innerHTML = "";

          // Thêm lại option mặc định vào đầu danh sách option
          const defaultOption = document.createElement("option");
          defaultOption.value = defaultWardOptionValue;
          defaultOption.textContent = defaultWardOptionText;
          selectWardElement.appendChild(defaultOption);

          responseWardData.forEach((ward) => {
            const option = document.createElement("option"); // Tạo một option element
            option.value = ward.WardCode; // Gán giá trị của option là WardID
            option.textContent = ward.WardName; // Gán nội dung của option là WardName
            selectWardElement.appendChild(option); // Thêm option vào select element
          });

        })
        .catch((error) => {
          console.error("There was a problem with the fetch operation:", error);
        });

    } else {
      responseWardData = [];
    }
  };

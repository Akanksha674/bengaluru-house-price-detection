const API_URL = "http://127.0.0.1:8000";

// Load locations when page opens

window.onload = function(){
    fetchLocations();
};

function fetchLocations(){
    fetch(`${API_URL}/locations`)
    .then(response => response.json())
    .then(data => {
        let locationDropdown =
        document.getElementById("location");

        data.forEach(location => {
            let option =
            document.createElement("option");
            option.value = location;
            option.text =
            location;

            locationDropdown.appendChild(option);
        });
    })
    .catch(error => {
        console.log(error);
    });
}

function predictPrice(){
    let location =
    document.getElementById("location").value;

    let sqft =
    document.getElementById("area").value;

    let bhk =
    document.getElementById("bhk").value;

    let bath =
    document.getElementById("bath").value;

    if(location==="" || sqft===""){
        alert("Please fill all details");
        return;
    }

    let requestData = {
        location:location,
        sqft:Number(sqft),
        bath:Number(bath),
        bhk:Number(bhk)
    };

    fetch(`${API_URL}/predict`,{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify(requestData)
    })
    .then(response=>response.json())

    .then(data=>{
        let price =
        data.estimated_price;
        document.getElementById("result").innerHTML =
        `
        Estimated Price:
        <br>
        ₹ ${price} Lakhs
        `;
    })

    .catch(error=>{
        console.log(error);

        document.getElementById("result").innerHTML =
        "Error predicting price";
    });
}
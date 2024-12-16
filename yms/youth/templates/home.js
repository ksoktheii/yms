let fileUpload = document.querySelectorAll("input");

fileUpload.forEach((e)=>{
  e.addEventListener("change",handleChange);
  function handleChange(files){
    if(this.type ==="file"){
      let name = this.files[0].name;
      console.log(name);
      let check =name.includes(".txt") || name.includes(".pdf") ;
      if(check){
        console.log("check passed");
      }else{
        this.files[0].reset;
        console.log("Not passed");
      }
    };
  };
});

document.getElementById('youthForm').addEventListener('submit', function (e) {
    e.preventDefault();
  
    // Get form values
    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const subCounty = document.getElementById('subCounty').value;
    const ward = document.getElementById('ward').value;
    const village = document.getElementById('village').value;
    const profession = document.getElementById('profession').value;
    
    // Add data to the table
    const tableBody = document.querySelector('#youthTable tbody');
    const row = document.createElement('tr');
  
    row.innerHTML = `
      <td>${name}</td>
      <td>${age}</td>
      <td>${subCounty}</td>
      <td>${ward}</td>
      <td>${village}</td>
      <td>${profession}</td>
    `;
    tableBody.appendChild(row);
    // Clear the form
    document.getElementById('youthForm').reset();
  });
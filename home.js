document.getElementById('youthForm').addEventListener('submit', function (e) {
    e.preventDefault();
  
    // Get form values
    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const subCounty = document.getElementById('subCounty').value;
    const ward = document.getElementById('ward').value;
    const village = document.getElementById('village').value;
    const profession = document.getElementById('profession').value;
    const academics = document.getElementById('academics').value;
  
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
      <td>${academics}</td>
    `;
  
    tableBody.appendChild(row);
  
    // Clear the form
    document.getElementById('youthForm').reset();
  });
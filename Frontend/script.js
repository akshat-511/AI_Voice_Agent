async function showAlert(){

      try {
        const response = await fetch("http://localhost:8000/");
        const data = await response.json();
        console.log("Received from backend:", data);
        alert(`Project: ${data.project} (Day ${data.day})`);
      } catch (err) {
        console.error("Error fetching data:", err);
      };
}




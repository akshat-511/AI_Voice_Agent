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


async function textToSpeech(){

    const userText =  document.getElementById("user_input").value;

    document.getElementById("user_input").value= "";

    try {
        const response = await fetch("http://localhost:8000/getTTS" , {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: userText }),
        }
            
        );

        const data = await response.json();

        if(data){
            let audio_is = document.getElementById("audio")

            audio_is.src = data.audio_url;

            audio_is.style.display = "block"
        }
        else{
            alert("failed to convert text to voice");
        }
        
    } catch (error) {
        console.log("Can't make request to TTS")
    }
}



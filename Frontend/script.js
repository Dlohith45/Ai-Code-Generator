async function generateCode() {
    let prompt = document.getElementById("prompt").value;
    let language = document.getElementById("language").value;
    let output = document.getElementById("output");

    if (prompt === "" || language === "") {
        alert("Please enter prompt and select language");
        return;
    }

    output.innerText = "Generating code...";
    

    try {
        const response = await fetch("http://127.0.0.1:5000/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                prompt: prompt,
                language: language
            })
        });

        const data = await response.json();

        output.innerText = data.code;
     
       

    } catch (error) {
        output.innerText = "Error: Unable to connect to backend.";
        console.error(error);
    }
}


function copyCode() {

    const code =
    document.getElementById("output").innerText;

    navigator.clipboard.writeText(code)
        .then(() => {
            alert("Code Copied!");
        })
        .catch(err => {
            console.error(err);
            alert("Copy Failed");
        });
}

function downloadCode() {

    const code =
    document.getElementById("output").innerText;

    const blob =
    new Blob([code], {type:"text/plain"});

    const a =
    document.createElement("a");

    a.href = URL.createObjectURL(blob);
    a.download = "generated_code.txt";
    a.click();
}
function clearFields() {
    document.getElementById("prompt").value = "";
    document.getElementById("output").innerText = "";
}
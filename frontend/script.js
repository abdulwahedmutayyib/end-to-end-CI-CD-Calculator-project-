function appendValue(value) {

    document.getElementById("display").value += value;
}


function clearDisplay() {

    document.getElementById("display").value = "";
}


async function calculateResult() {

    const expression = document.getElementById("display").value;

    if (!expression) {
        return;
    }

    try {

        const response = await fetch(
            "/api/calculate?expr=" + encodeURIComponent(expression)
        );

        const data = await response.json();

        if (data.result !== undefined) {

            document.getElementById("display").value = data.result;

        } else {

            document.getElementById("display").value = "Error";
        }

    } catch (error) {

        console.error(error);

        document.getElementById("display").value = "Server Error";
    }
}

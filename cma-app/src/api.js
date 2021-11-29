export const getAllTransactions = async (month, year) => {
    const response = await fetch(`http://localhost:5000/transactions?month=${month + 1}&year=${year}`);
    if (response.ok) { // if HTTP-status is 200-299
        // get the response body (the method explained below)
        return response.json()
    } else {
        alert("HTTP-Error: " + response.status);
    }
    return null
}

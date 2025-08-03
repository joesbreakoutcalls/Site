
async function loadPredictions() {
    const res = await fetch("http://localhost:8000/top-breakouts");
    const data = await res.json();
    const container = document.getElementById("predictions");
    container.innerHTML = "";
    data.predictions.forEach(item => {
        const el = document.createElement("div");
        el.innerHTML = `<strong>${item.name} (${item.symbol})</strong> - Score: ${item.score}<br/><i>${item.reason}</i>`;
        container.appendChild(el);
    });
}
setInterval(loadPredictions, 120000);
loadPredictions();

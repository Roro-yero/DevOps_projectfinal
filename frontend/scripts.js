document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("search-input");
    const searchButton = document.getElementById("searchBtn");
    const resultsContainer = document.getElementById("results");

    async function search() {
        let query = searchInput.value.trim();

        if (!query) {
            alert("Veuillez entrer un terme de recherche !");
            return;
        }

        console.log("🔍 Recherche en cours pour :", query); // Debugging

        try {
            let response = await fetch(`http://localhost:8000/search/?query=${query}`);

            if (!response.ok) {
                throw new Error(`Erreur serveur : ${response.status}`);
            }

            let data = await response.json();
            console.log("📊 Résultats reçus du backend :", data); // Vérifier si l'API retourne des données

            resultsContainer.innerHTML = ""; // On vide les anciens résultats

            if (!Array.isArray(data) || data.length === 0) {
                resultsContainer.innerHTML = "<p>Aucun résultat trouvé.</p>";
                return;
            }

            // Affichage des résultats
            data.forEach(item => {
                let div = document.createElement("div");
                div.classList.add("result-item");
                div.innerHTML = `<strong>${item.name} ${item.fam_name}</strong><br>
                                 📅 Naissance : ${item.birth}<br>
                                 🎓 École : ${item.school}`;
                resultsContainer.appendChild(div);
            });

        } catch (error) {
            console.error("❌ Erreur lors de la requête API :", error);
            alert("Erreur lors de la récupération des résultats. Vérifiez la console.");
        }
    }

    // Attacher l'événement au bouton
    searchButton.addEventListener("click", search);

    // Permettre la recherche en appuyant sur "Entrée"
    searchInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            search();
        }
    });
});

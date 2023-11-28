document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("search-input");
    const searchButton = document.getElementById("search-button");
    const squareCurvedBlocks = document.querySelectorAll(".square-curved-block");

    document.getElementById("search-form").addEventListener("submit", function (event) {
        event.preventDefault();

        const searchTerm = searchInput.value.toLowerCase();

        squareCurvedBlocks.forEach(function (block) {
            const categoryName = block.querySelector(".category-name").innerText.toLowerCase();

            if (categoryName.includes(searchTerm)) {
                block.style.display = "block";
            } else {
                block.style.display = "none";
            }
        });
    });
});

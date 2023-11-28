document.addEventListener('DOMContentLoaded', function () {
    const searchForm = document.getElementById('search-form');
    const searchInput = document.getElementById('search-input');
    const searchResultsContainer = document.getElementById('search-results');
    const squareCurvedBlocks = document.querySelectorAll(".square-curved-block");

    // Check if the containers exist
    if (!searchForm || !searchInput || !searchResultsContainer) {
        console.error('Search form, input, or results container not found.');
        return;
    }

    searchForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const searchTerm = searchInput.value.toLowerCase();

        // Clear previous search results
        searchResultsContainer.innerHTML = '';

        // Filter square curved blocks based on the search term
        squareCurvedBlocks.forEach(function (block) {
            const categoryName = block.querySelector(".category-name").innerText.toLowerCase();
            if (categoryName.includes(searchTerm)) {
                block.style.display = "block";
            } else {
                block.style.display = "none";
            }
        });

        // Fetch search results
        fetch(`/search?query=${searchTerm}`)
            .then(response => response.json())
            .then(results => {
                // Handle the search results, e.g., display them on the page
                results.forEach(function (result) {
                    // Create a div for each result
                    var resultDiv = document.createElement('div');
                    resultDiv.className = 'category-block';

                    // Create an image element
                    var imageElement = document.createElement('img');
                    imageElement.src = result.image;
                    imageElement.className = 'category-img';
                    resultDiv.appendChild(imageElement);

                    // Create a link element
                    var linkElement = document.createElement('a');
                    linkElement.href = result.url;
                    linkElement.textContent = result.title;
                    resultDiv.appendChild(linkElement);

                    // Append the result div to the container
                    searchResultsContainer.appendChild(resultDiv);
                });
            })
            .catch(error => {
                console.error('Error fetching search results:', error);
            });
    });
});

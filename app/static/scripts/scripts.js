// document.addEventListener('DOMContentLoaded', function() {
//     const searchInput = document.getElementById('search-input');
//     const searchResults = document.getElementById('search-results');

//     searchInput.addEventListener('input', function() {
//         const query = searchInput.value;

//         if (query.length === 0) {
//             searchResults.innerHTML = '';
//             return;
//         }

//         fetch(`{{ url_for('search') }}?query=${encodeURIComponent(query)}`)
//             .then(response => response.json())
//             .then(data => {
//                 let html = '<h3>Products</h3>';

//                 if (data.products.length > 0) {
//                     html += '<div class="overflow-auto"><div class="d-flex flex-wrap">';
//                     data.products.forEach(product => {
//                         html += `
//                             <div class="card border-light shadow-sm me-3 mb-4" style="flex: 0 0 auto; width: 18rem;">
//                                 <a href="/product/${product.id}">
//                                     <img src="${product.image_url || '/static/default_product_image.jpg'}" class="card-img-top" alt="${product.name}">
//                                 </a>
//                                 <div class="card-body">
//                                     <a href="/product/${product.id}" class="text-decoration-none text-dark">
//                                         <h5 class="card-title">${product.name}</h5>
//                                     </a>
//                                     <p class="card-text">$${product.price}</p>
//                                     <div class="d-flex">
//                                         <form action="/add_to_cart/${product.id}" method="post" class="me-2">
//                                             <button type="submit" class="btn btn-primary"><i class="fas fa-cart-plus"></i> Add to Cart</button>
//                                         </form>
//                                         <form action="/add_to_favorites/${product.id}" method="post">
//                                             <button type="submit" class="btn btn-secondary"><i class="fas fa-heart"></i> Add to Favorites</button>
//                                         </form>
//                                     </div>
//                                 </div>
//                             </div>
//                         `;
//                     });
//                     html += '</div></div>';
//                 } else {
//                     html += '<p>No products found.</p>';
//                 }

//                 html += '<h3>Categories</h3>';

//                 if (data.categories.length > 0) {
//                     html += '<div class="overflow-auto"><div class="d-flex flex-wrap">';
//                     data.categories.forEach(category => {
//                         html += `
//                             <div class="card border-light shadow-sm me-3 mb-4" style="flex: 0 0 auto; width: 18rem;">
//                                 <a href="/category/${category.id}">
//                                     <img src="${category.image_url || '/static/default_category_image.jpg'}" class="card-img-top" alt="${category.name}">
//                                 </a>
//                                 <div class="card-body">
//                                     <a href="/category/${category.id}" class="text-decoration-none text-dark">
//                                         <h5 class="card-title">${category.name}</h5>
//                                     </a>
//                                     <p class="card-text">${category.description}</p>
//                                 </div>
//                             </div>
//                         `;
//                     });
//                     html += '</div></div>';
//                 } else {
//                     html += '<p>No categories found.</p>';
//                 }

//                 searchResults.innerHTML = html;
//             });
//     });
// });

document.addEventListener('DOMContentLoaded', function() {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function() {
            const productId = this.getAttribute('data-product-id');
            const url = `/add_to_cart/${productId}`;

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(response => response.json())
            .then(data => {
                displayFlashMessage(data.status, data.message);
            })
            .catch(error => console.error('Error:', error));
        });
    });
});

function displayFlashMessage(status, message) {
    // Affiche un message pop-up en utilisant alert (ou une autre méthode comme sweetalert)
    alert(message);
    
    // Optionnel : Ajouter le message à un conteneur HTML
    const flashContainer = document.getElementById('flash-messages');
    const flashMessage = document.createElement('div');
    flashMessage.className = `alert alert-${status}`;
    flashMessage.textContent = message;

    flashContainer.appendChild(flashMessage);

    // Efface le message après quelques secondes
    setTimeout(() => {
        flashMessage.remove();
    }, 3000);
}

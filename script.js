document.getElementById('searchBox').addEventListener('keyup', function() {
    var searchQuery = this.value.toLowerCase();
    var results = document.querySelectorAll('.search-results .result h3');
    var noResults = document.getElementById('no-result');
    var message = noResults.querySelector('h3')

    message.textContent = `No results for, "${this.value}"`;

    

    
    var zero_results = true;

    
    
    
    results.forEach(function(h3) {
        var textContent = h3.textContent.toLowerCase();

        if (textContent.includes(searchQuery)) {
            h3.parentElement.classList.remove('hidden');
            zero_results = false;
        
        } else {
            h3.parentElement.classList.add('hidden');
        }
    });

    

    noResults.style.display = zero_results ? 'block' : 'none';


});
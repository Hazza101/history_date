document.querySelectorAll('.accordion-button').forEach(button => {
    button.addEventListener('click', () => {

        const accordionContent = button.nextElementSibling;
        button.classList.toggle('active');

        if (button.classList.contains('active')) {
            accordionContent.style.display = 'block';
        } else {
            accordionContent.style.display = 'none';
        }

    });

});
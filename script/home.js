// script.js
document.addEventListener('DOMContentLoaded', function() {
    const scrollImages = document.querySelectorAll('.song');
    const popupWrappers = document.querySelectorAll('.popup-wrapper');

    scrollImages.forEach(function(scrollImage) {
        const index = scrollImage.getAttribute('data-index');
        const popupWrapper = document.querySelector(`.popup-wrapper[data-index="${index}"]`);

        scrollImage.addEventListener('mouseover', function() {
            popupWrappers.forEach(wrapper => wrapper.style.display = 'none');
            popupWrapper.style.display = 'block';
        });

        scrollImage.addEventListener('mouseout', function() {
            popupWrapper.style.display = 'none';
        });
    });
});

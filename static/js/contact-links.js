document.addEventListener('DOMContentLoaded', function() {

    const links = document.querySelectorAll('.contact-link');

    links.forEach(function(link) {
        const type = link.getAttribute('type');
        const content = link.getAttribute('content');
        let href = '#';

        switch(type) {
            case 'email': href=`mailto:${content}`; break;
            case 'phone': href=`tel:${content}`; break;
            case 'github': href = `https://github.com/${content}`; break;
            case 'instagram': href= `https://www.instagram.com/${content}`; break;
        }

        link.href = href;
    });
});
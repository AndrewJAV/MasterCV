document.addEventListener('DOMContentLoaded', function() {

    const contactSection = document.getElementById('contact-section');
    
    const links = contactSection.querySelectorAll('.contact-link');

    links.forEach(function(link) {
        const type = link.getAttribute('type');
        const content = link.getAttribute('content');
        let href = '#';

        print(type);
        print(content);
        switch(type) {
            case 'Email': href=`https://mail.google.com/mail/?view=cm&fs=1&to=${content}`; break;
            case 'Phone': href=`tel:${content}`; break;
            case 'Github': href = `https://github.com/${content}`; break;
            case 'Instagram': href= `https://www.instagram.com/${content}`; break;
            case 'LinkedIn': href = `https://www.linkedin.com/in/${content}`; break;
            case 'Facebook': href = `https://www.facebook.com/${content}`; break;
            case 'Twitter': href = `https://twitter.com/${content}`; break;
        }

        link.href = href;
    });
});
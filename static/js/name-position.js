document.addEventListener("DOMContentLoaded", function() {

    function insertName() {
        var left_container = document.getElementById("left-container");
        var right_container = document.getElementById("right-container");

        var nameContainer = document.createElement("section");
        nameContainer.id = "name-container";
        nameContainer.innerHTML =  `<h1>${personName}<br>${personLastName}</h1>`;
        
        // Insertar como segundo elemento
        if (window.innerWidth < 650) {
            left_container.insertBefore(nameContainer, left_container.children[1])
        } else {
            right_container.insertBefore(nameContainer, right_container.children[0])
        }
    }

    insertName();
    window.addEventListener("resize", insertName);
});

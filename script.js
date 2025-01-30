document.addEventListener('DOMContentLoaded', function() {
    const photos = [
        { 
            id: 1, 
            src: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80', 
            title: 'Café de la Mañana', 
            description: 'Una taza de café recién hecho para empezar el día.' 
        },
        { 
            id: 2, 
            src: 'https://images.unsplash.com/photo-1511920170033-f8396924c348?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80', 
            title: 'Café con Leche', 
            description: 'Un delicioso café con leche espumosa.' 
        },
        { 
            id: 3, 
            src: 'https://images.unsplash.com/photo-1507133750040-4a8f57021571?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80', 
            title: 'Granos de Café', 
            description: 'Granos de café recién tostados y listos para moler.' 
        },
        { 
            id: 4, 
            src: 'https://images.unsplash.com/photo-1497935586351-b67a49e012bf?ixlib=rb-1.2.1&auto=format&fit=crop&w=1351&q=80', 
            title: 'Café Espresso', 
            description: 'Un espresso perfecto con una crema dorada.' 
        },
        { 
            id: 5, 
            src: 'https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?ixlib=rb-1.2.1&auto=format&fit=crop&w=1351&q=80', 
            title: 'Café en la Cafetería', 
            description: 'Un ambiente acogedor para disfrutar de un buen café.' 
        },
        { 
            id: 6, 
            src: 'https://images.unsplash.com/photo-1498804103079-a6351b050096?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80', 
            title: 'Café con Arte Latte', 
            description: 'Un café decorado con arte latte.' 
        },
        { 
            id: 7, 
            src: 'https://images.unsplash.com/photo-1524350876685-274059332603?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80', 
            title: 'Café en la Montaña', 
            description: 'Disfrutando de un café con vistas espectaculares.' 
        },
        { 
            id: 8, 
            src: 'https://images.unsplash.com/photo-1509042239860-f550ce710b93?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80', 
            title: 'Café y Libros', 
            description: 'Un café acompañado de un buen libro.' 
        },
        { 
            id: 9, 
            src: 'https://images.unsplash.com/photo-1506619216599-9d16d0903dfd?ixlib=rb-1.2.1&auto=format&fit=crop&w=1349&q=80', 
            title: 'Café de Especialidad', 
            description: 'Un café de especialidad preparado con cuidado.' 
        }
    ];

    const photoView = document.getElementById('photoView');
    const editForm = document.getElementById('editForm');
    const photoTitle = document.getElementById('photoTitle');
    const photoDescription = document.getElementById('photoDescription');

    // Cargar fotos en la vista
    photos.forEach(photo => {
        const col = document.createElement('div');
        col.className = 'col-md-4 mb-4';
        col.innerHTML = `
            <div class="card">
                <img src="${photo.src}" class="card-img-top" alt="${photo.title}">
                <div class="card-body">
                    <h5 class="card-title">${photo.title}</h5>
                    <p class="card-text">${photo.description}</p>
                    <button class="btn btn-secondary btn-sm" onclick="editPhoto(${photo.id})">Editar</button>
                </div>
            </div>
        `;
        photoView.appendChild(col);
    });

    // Función para editar una foto
    window.editPhoto = function(id) {
        const photo = photos.find(p => p.id === id);
        if (photo) {
            photoTitle.value = photo.title;
            photoDescription.value = photo.description;
        }
    };

    // Manejar el envío del formulario de edición
    editForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const title = photoTitle.value;
        const description = photoDescription.value;
        alert(`Cambios guardados:\nTítulo: ${title}\nDescripción: ${description}`);
    });
});
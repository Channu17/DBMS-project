// Assuming you have a MongoDB connection established

const movieList = document.getElementById('movie-list');

async function fetchMovies() {
    try {
        const response = await fetch('/api/movies'); // Replace with your API endpoint
        const movies = await response.json();

        movies.forEach(movie => {
            const card = document.createElement('div');
            card.classList.add('movie-card');

            const title = document.createElement('h2');
            
            title.textContent = movie.title;

            const details = document.createElement('div');
            details.classList.add('movie-details');

            const detailsList = Object.entries(movie)
                .filter(([key, value]) => key !== '_id' && key !== 'genre' && key !== 'actor_id' && key !== 'director_id' && key !== 'awards_id')
                .map(([key, value]) => `<p><strong>${key.charAt(0).toUpperCase() + key.slice(1)}:</strong> ${value}</p>`)
                .join('');

            details.innerHTML = detailsList;

            const genreList = document.createElement('p');
            genreList.textContent = `Genres: ${movie.genre.join(', ')}`;

            card.appendChild(title);
            card.appendChild(details);
            card.appendChild(genreList);

            movieList.appendChild(card);
        });
    } catch (error) {
        console.error('Error fetching movies:', error);
    }
}

fetchMovies();
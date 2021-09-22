const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (data) {
  const movies = data.results;
  for (const movie of movies) {
    const title = $('<li></li>').text(movie.title);
    $('#list_movies').append(title);
  }
});
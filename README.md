# Digital Library Project for Information Visualization
This project was developed for my coursework of Information Visualization. Main aspect of this project were, demonstrating data visualization with respect to subjects. I have shown 
search results and topic related related visualization in this project.
- Technologies used- Django , JavaScript, Bootstrap, HTML5
- API used: Open Library API: https://openlibrary.org/developers/api
- Hosted on heruko at: https://rocky-fortress-42855.herokuapp.com/
## Pages in the web app
- Homepage: shows featured subjects and related books. Other information such as number of books, ratings, book types are also shown.
- Book detail page: url: /document-details/book-id/

shows book cover, book type, ratings, and edition informations. Also shows subject related matchings graph. If you have previously gone through books of similar subjects,
you will be able to see a graph here showing that.
<img src="/media-resources/screenshot-subject-match-graph.PNG" width="550">


In addition you will be able to see books relevant to the particular book you are viewing, according to subject matching.
- My book reading pattern page: url: /get-my-viewings/

In this page you will see all the number of books you have viewed of different subjects. So, you will get an idea about your reading pattern.

<img src="/media-resources/screenshot-my-top-book-viewings.PNG" width="550">

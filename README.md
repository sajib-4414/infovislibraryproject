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

### Information visualization principles used:
- I have also implemented Schneiderman’s principle [1] of overview first,zoom and filter, and details on demand principle.
- I have followed the gestalt principle of proximity and closure in theinterface in document detail and home page
- The system maintained a good level of expressiveness by showing anadequate level of information on demand. 
- The system maintained the data-ink ratio by showing less importantdata with background colours.

#### References:
[1] B. Shneiderman. Ieee symposium on visual languages. InThe eyes have it:a task by data type taxonomy for information visualizations, pp. 336–343.IEEE, New York, NY, USA, 1996. doi: 10.1109/VL.1996.545307

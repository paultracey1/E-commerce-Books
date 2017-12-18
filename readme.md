# Shared Stories
E-commerce site for the buying and selling of second hand books; built using Python and Django Framework, and hosted on Heroku.
Also used were: HTML5, CSS3, Amazon S3 bucket, Stripe, Bootstrap, and Java Script.

For a live Demo: https://paultracey-e-commerce.herokuapp.com/

# Functionality

## Searching for books

Available Books can be viewed from the 'Books' page accessed through the tab. This displays a list of books with the most recently added appearing at the top; with details shown like author, genre, excerpt from the description, seller name, and price displayed.
Each book has it's own page with a full description, bigger preview of the coverart, and a comments section.

Users mostly search for books through their prefered genre, and so there's a handy side bar which lists all genres to filter the books shown.
If the user has a particualr book in mind they can use the case-indifferent searchbar and search for a particualr book's title, author or genre.
There are further ways of searching for books using the details of books shown. This inculdes but is not limited to, clicking the name of the book's seller to see what else they have availble on the store.

## Buying books

From the individual book pages or from the various searching pages there is the option to 'buy' or 'add to cart' books the user doesn't own. Users must be logged in to do either of these options and will be redirected to do so if they haven't already.
Both options lead to a page where credit card information can be entered to secure the hypothetical purchase.

## Selling Books

Users can choose the option "Add Book" at the bottom of any page of listed books inculding their own profile page which can be accessed by the tab.
The user is brought to a form page to fill in various details of the book, with the option of adding a image of the book which will otherwise have a default icon.
Users who own books have the options to "Edit" or "Delete" the books, instead of buying them.
# Shared Stories
This is a mock-up E-commerce site for the buying and selling of second hand books; built using Python & Django Framework, and hosted on Heroku.
Also used were: HTML5, CSS3, Amazon S3 bucket, Stripe, Bootstrap, and Java Script.

For a live Demo: https://paultracey-e-commerce.herokuapp.com/

# Functionality

## Searching for books

Available Books can be viewed from the 'Books' page accessed through the tab at the top of every page. This displays a list of books with the most recently added appearing at the top; with details shown like author, genre, an preview of the description, seller name, and price being displayed.
Each book has its own page with a full description, bigger preview of the cover art, and a comments section.

Users mostly search for books through their preferred genre, and so there's a handy side bar which lists all genres to filter the books shown.
If the user has a particular book in mind they can use the case-indifferent search bar, and search for a particular book's title, author or genre.
There are further ways of searching for books using the details of books shown. This includes but is not limited to, clicking the name of the book's seller to see what other books they're selling on the site.

## Buying books

From the individual book pages or from the various searching pages there is the option to 'Buy Now' or 'Add to Cart' with books the user doesn't own. Users must be logged in to do either of these options, and will be redirected to do so if they haven't already.
Both options lead to a page where credit card information can be entered to secure the hypothetical purchase. Purchases can be observed using the pseudo credit card number 4242 4242 4242 4242, and any 3 digit number for the CVV number.

## Selling Books

Users can choose the option "Add Book" at the bottom of any page of listed books including their own profile page which can be accessed by the tab.
The user is brought to a form page to fill in various details of the book, with the option of adding a image of the book which will otherwise have a default icon.
Users who own books have the option to "Edit" or "Delete" their books, instead of buying them.
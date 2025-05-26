Internet store project.

This is a Django based implementation

Project contains pages:

- Home page with product list
- Contact page of the website
- Blog page with posts

Pages are linked to each other you can press Contacts button, and you'll be redirected to contacts page.
On contacts page you can send a feedback through "contact us form":
when you click 'send' button you'll be redirected to the confirmation page and can move to main page then.

Products:

- Each product has a name, description, image, category, price and owner. For the Moderator there is a field to publish
  or unpublish the product.
- Product class has custom permission "can_unpublish_product" for Moderator.
- Management:
  - Main page, product list, contains management link, available for registered users and Moderators.
  - Owners of products can update and delete their products.
  - Moderators can update and delete any product.


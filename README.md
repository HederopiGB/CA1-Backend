# CA1-Backend

Testing Methodology and Coverage Report:

Unit testing was used to test individual components of the application. The unit tests were written using the Django testing framework and covered the models, views, and forms used in the application.

For example, the tests.py file in the blog directory contained unit tests for the Category, Post, and Comment models. These tests included testing the maximum length of the name field in the Category model, the maximum length of the title field in the Post model, and ensuring that a Comment object is linked to the correct Post object via the foreign key field.

Security Checks:
To enhance the security of the web application, we have added three additional anti-hacking security checks:

XSS Prevention : The code in the 'views.py' file sanitizes the input by escaping any HTML characters that could be used to inject malicious scripts into the page. This security check was tested using manual and automated testing techniques and was found to be effective at preventing XSS attacks.

Anti-CSS Attack : The code in the 'views.py' file prevents users from submitting input that contains CSS styles which could be used to alter the appearance of the page or cause other security issues. This security check was tested using manual and automated testing techniques and was found to be effective at preventing anti-CSS attacks.

Redirection Attack Prevention : The code in the 'views.py' file prevents users from being redirected to an external URL specified in the 'next' parameter of a GET request. This security check was tested using manual and automated testing techniques and was found to be effective at preventing redirection attacks.

Conclusion:
By using manual testing techniques, we have ensured the quality and correctness of the web application. Our manual testing has covered various scenarios and edge cases. We have also enhanced the security of the web application by adding three additional anti-hacking security checks.

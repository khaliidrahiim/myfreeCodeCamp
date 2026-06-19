# User Stories:

1. You should set the root font-size of your HTML document to 24px.
2. You should have an element with a class of newspaper that contains all your other elements.
3. Your .newspaper element should have a font-size of 16px and a font of Open Sans with a fallback font of sans-serif.
4. Within your .newspaper element, you should have at least seven more elements: one for the newspaper name that has a class of name, one for the date of the article with a class of date, one for the headline with a class of headline, one for the sub-headline with a class of sub-headline, one for the author with a class of author, and two paragraphs each with a class of text. All of these elements should be filled with your article information.
5. Your .name element should have a font-size that is twice the root element's font-size and should use the Times New Roman font, with a fallback font of serif.
6. Your .name and .author elements should use CSS to make all their characters uppercase.
7. Your .headline element should have a font-size that is twice its parent element's font-size and should be bold.
8. Your .sub-headline element should have a font-weight of 100, a font-size that is 1.5 times its parent element's font-size, and should be italicized.
9. Your .author should use CSS to make it bold.
10. Your .text elements should have a text-indent of 20px.
11. Your .text elements should have a line-height that is twice their parent element's font-size.
12. The first letter of your .text elements should be bold and twice the size of their parent element's font-size. Use the ::first-letter selector for this.

# Tests:

1. You should have an html selector that sets its font-size to 24px.
2. You should have an element with a class of newspaper.
3. You should have a .newspaper selector that sets its elements' font-size to 16px.
4. You should have a .newspaper selector that sets its elements' font-family to 'Open Sans', sans-serif.
5. You should have an element with a class of name within your .newspaper element.
6. Your .name element should have the name of your newspaper.
7. You should have an element with a class of date within your .newspaper element.
8. Your .date element should have the date.
9. You should have an element with a class of headline within your .newspaper element.
10. Your .headline element should have your article headline.
11. You should have an element with a class of sub-headline within your .newspaper element.
12. Your .sub-headline element should have your article sub-headline.
13. You should have an element with a class of author within your .newspaper element.
14. Your .author element should have your article author.
15. You should have at least two paragraph elements, each with a class of text, within your .newspaper element.
16. Your .text elements should have your article text.
17. You should have a .name selector that sets its elements' font-size to 2rem.
18. You should have a .name selector that sets its elements' font-family to 'Times New Roman', serif.
19. The .name element should have the text-transform property set to uppercase.
20. The .author element should have the text-transform property set to uppercase.
21. You should have a .headline selector that sets its elements' font-size to 2em.
22. You should have a .headline selector that sets its elements' font-weight to bold.
23. You should have a .sub-headline selector that sets its elements' font-weight to 100.
24. You should have a .sub-headline selector that sets its elements' font-size to 1.5em.
25. You should have a .sub-headline selector that sets its elements' font-style to italic.
26. You should have an .author selector that sets its elements' font-weight to bold.
27. You should have a .text selector that sets its elements' text-indent to 20px.
28. You should have a .text selector that sets its elements' line-height to 2em.
29. You should have a .text::first-letter selector that sets its elements' font-weight to bold.
30. You should have an .text::first-letter selector that sets its elements' font-size to 2em.
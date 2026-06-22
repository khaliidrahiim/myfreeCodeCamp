# User Stories:

1. Your tribute page should have a `main` element with a corresponding `id` of `main`, which contains all other elements.
2. You should see an element with an `id` of `title`, which contains a string (i.e. text), that describes the subject of the tribute page (e.g. "Dr. Norman Borlaug").
3. You should see either a `figure` or a `div` element with an `id` of `img-div`.
4. Within the `#img-div` element, you should see an `img` element with a corresponding `id="image"`.
5. Within the `#img-div` element, you should see an element with a corresponding `id="img-caption"` that contains textual content describing the image shown in `#img-div`.
6. You should see an element with a corresponding `id` of `tribute-info`, which contains textual content describing the subject of the tribute page.
7. You should see an `a` element with a corresponding `id` of `tribute-link`, which links to an outside site, that contains additional information about the subject of the tribute page. HINT: You must give your element an attribute of `target` and set it to `_blank` in order for your link to open in a new tab.
8. Your `#image` should use `max-width` and `height` properties to resize responsively, relative to the width of its parent element, without exceeding its original size.
9. Your `img` element should be centered within its parent element.

Note: Be sure to link your stylesheet in your HTML and apply your CSS.

# Tests:

- [x] You should have a `main` element with an `id` of `main`.
- [x] Your `#img-div`, `#image`, `#img-caption`, `#tribute-info`, and `#tribute-link` should all be descendants of `#main`.
- [x] You should have an element with an `id` of `title`.
- [x] Your `#title` should not be empty.
- [x] You should have a `figure` or `div` element with an `id` of `img-div`.
- [x] You should have an `img` element with an `id` of `image`.
- [x] Your `#image` should be a descendant of `#img-div`.
- [x] You should have a `figcaption` or `div` element with an `id` of `img-caption`.
- [x] Your `#img-caption` should be a descendant of `#img-div`.
- [x] Your `#img-caption` should not be empty.
- [x] You should have an element with an `id` of `tribute-info`.
- [x] Your `#tribute-info` should not be empty.
- [x] You should have an `a` element with an `id` of `tribute-link`.
- [x] Your `#tribute-link` should have an `href` attribute and value.
- [x] Your `#tribute-link` should have a `target` attribute set to `_blank`.
- [x] Your `img` element should have a display of `block`.
- [x] Your `#image` should have a max-width of `100%`.
- [x] Your `#image` should have a height of `auto`.
- [x] Your `#image` should be centered within its parent.
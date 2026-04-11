# arthur-stat.github.io Redirect

This repository is a redirect shell for the old GitHub Pages site.

- `/` is handled by `index.html`
- arbitrary old paths are handled by `404.html`
- both pages redirect to `https://iharee.github.io` while preserving path, query string, and hash in JavaScript

Important limitation:

GitHub Pages cannot issue a true wildcard server-side `301` for every old path. For non-root old URLs, GitHub Pages serves `404.html` first and the browser-side script redirects immediately after that.

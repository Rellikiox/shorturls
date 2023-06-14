# Link shortener

This is just a good-old simple link shortener service. It's a simple application that I want to use as a means to improve on my developer skills

## Release map

Here's an overview of which features are coming and their order

### v1.0: Generating short links

A single frontend that explains what the site does, it's got an input field where you can put in a URL and it will give you back a short URL.


## App structure

### Frontend

A single container that serves static HTML files.

### Backend

A backend container that handles all API requests + redirections

### Database

PostgreSQL running on a separate container

### Routing

Traefik
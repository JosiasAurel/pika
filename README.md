
## Octo 

A simple url shortener made with Python and flask

### Dependencies 

- TinyDB
- Python
- flask

## How it works
You can send a ```POST``` request to ```/short``` and the app will handle it by adding it to the database as well as a short url safe token using built-in ```secrets``` module.

The home route ```/``` handles dynamic ```GET``` request by sending a redirect response to a URL that matches that requested.
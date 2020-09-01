
## Pika

[![Run on Repl.it](https://repl.it/badge/github/JosiasAurel/octo)](https://repl.it/github/JosiasAurel/octo)

A simple url shortener made with Python and flask

### Dependencies 

- TinyDB
- Python
- flask

## How it works
You can send a ```POST``` request to ```/short``` and the app will handle it by adding it to the database as well as a short url safe token using built-in ```secrets``` module.

The home route ```/``` handles dynamic ```GET``` request by sending a redirect response to a URL that matches that requested.

## TODO :
- Add a fronend app
- Add functionality to save url clicks
- Add a db watcher to delete url after 24 hours
- More coming

# Decipherability Generator

Get all words matching a phoneme-grapheme list

## API Usage

```
/words?threshold=0.5&masteredRelations=a-a,b-b
```

## Get your refresh token from Google

First copy the sample environment file to `.env`

```
cp .env.example .env
```

Create an app to get your Client ID and Secret ID, you can do it from here https://developers.google.com/sheets/api/quickstart/python by clicking on "Enable the Google Sheets API". Fill up the corresponding variables in `.env`

Run `pipenv run bin/get_google_token.py` to get your refresh token, set it in `.env`.

You're all set!


## Deploy

```
serverless deploy
```

You can also test the API locally:

```
serverless invoke local -f find_mastered_words -p event.json
```

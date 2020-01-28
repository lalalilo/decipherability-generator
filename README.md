# Decipherability Generator

Get all words matching a phoneme-grapheme list

## API Usage

```
/words?threshold=0.5&masteredRelations=a-a,b-b
```

## Deploy

```
serverless deploy
```

You can also test the API locally:

```
serverless invoke local -f main -p event.json
```

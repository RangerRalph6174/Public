## Hides a secret message in a public message
Uses the API provided by [neatnik](https://neatnik.net/steganographr/)

## Usage
To hide a secret message inside a public message\
The public message will be copied to your clipboard.
```
./steganographr -p "A public message" -s "A secret message"
```

To hide the default secret message inside a public message\
The public message will be copied to your clipboard.
```
./steganographr -p "A public message"
```

To reveal the secret message.
for best results type (-p "") and then move cursor between the quotes and paste the secret message.
```
./steganographr -d -p "A public message"
```

You can also reveal the secret message by pasting the public message into the link above.


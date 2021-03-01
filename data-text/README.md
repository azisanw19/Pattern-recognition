# Belajar data text

## Preprocessing

- Parsing
- Lexical Analysis
- Stop-word Removal
- Stemming (Porter Algorithm)

## Representation

- Bag of Words 
- Term Frequency
- Inverse Document Frequency

## Library yang digunakan

1. re (Reguler Expresion/ RegEx)
2. math (Mathenatic)

## Function lexical analysis

Menggunakan Reguler Expresion untuk menghapus number dan punctuation.

## Function stop list removal

Untuk menghapus kata yang tidak merepresentasikan makna seperti adalah, dan, dsb.

## Function deteksi phrase

- format Phrase:

```json
{
  "first word": ["second word"],
  "sapu": ["tangan", "lidi"]
}
```

## Lemma Checker

- dict_word hanya kata yang beririsan dengan kata berimbuhan seperti makan -> beririsan dengan imbuhan kan.

- Format dict-word:

```json
{
  "kan$": ["makan"],
  "an$": ["jangan", "makan"]
}
```

## Porter Algorithm

- untuk melakukan stemming saya menggunakan porter algoritma dan saya tambahkan cara untuk menangani kata yang seperti imbuhan tetapi bukan imbuhan dengan menggunakan data imbuhan yang beririsan dengan kata dasar. Contohnya makan -> seperti ada imbuhan -kan tetapi bukan imbuhan.

- Format rule

```json
{
  "regex": "diubah ke",
  "^ber": "",
  "kan$": ""
}
```

## Bag of Word

- Format documents:

```
[["token", "adalah", "token"],
 ["token", "adalah", "token"]]
```

## Term Frequency

- Untuk setiap document


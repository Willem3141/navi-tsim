This is a database of [Na'vi](https://en.wikipedia.org/wiki/Na'vi_language) words and example sentences, to be used for creating dictionaries and tools. Most notably, it is the database used by [Reykunyu](https://reykunyu.wimiso.nl).

## Words

The words are stored in the directory `aylì'u`. Each word is stored in a separate JSON file, named `<word>-<type>.json` (where `<type>` is the word type; see below). Each file contains a single JSON object containing information about the word.

| Key | Meaning |
|:---:|---------|
| `na'vi` | *(string)* The Na'vi word itself. |
| `type` | *(string)* The word type (see below). |
| `translations` | *(object)* An object containing the translations of the word, with keys `"en"`, `"de"`, etc. for the various languages. Note that the English translation (`"en"`) is most likely to be up-to-date; the other translations were imported from Eana Eltu without being modified. |
| `pronunciation` | *(array of [string, number])* Pronunciations of the word, in which syllable breaks are indicated as dashes. Removing the dashes from the string does not always result in the original word: it differs if the spelling does not indicate the pronunciation. The number is the (1-based) index of the stressed syllable. Most words have only a single pronunciation, but some have several (`nìayoeng` -> `[["nì-ay-weng", 3], ["nay-weng", 2]]`). |
| `infixes` | *(string)* (for verbs only) String indicating the infix positions. The infixes are indicated with two dots. As a special case, `zenke` is given as `z.en.(e)ke`. |
| `etymology` | *(array of string)* (optional) List of words that this word is made up of (`tìkangkem` -> `["tìkan:n", "kem:n"]`). |
| `seeAlso` | *(array of string)* (optional) List of words that are related in meaning to this word (`tìkangkem` -> `["txintìn:n"]`). |

### Sources

The words were imported from Eana Eltu (the existing main word database) on 2018-12-30, using the scripts in `aysä'o/eana-eltu`, and manually modified to fix errors.

> **Note:** At this time, many errors still remain.

### Word types

| Type | Description |
|:----:|-------------|
| `n` | noun |
| `n:si` | *si*-verb (more precisely, noun that can be combined with `si` to make a *si*-verb) |
| `n:pr` | proper noun |
| `pn` | pronoun |
| `adj` | adjective |
| `adv` | adverb |
| `adp` | adposition |
| `num` | numeral |
| `intj` | interjection |
| `conj` | conjunction |
| `v:in` | verb, intransitive |
| `v:tr` | verb, transitive |
| `v:m` | verb, modal |
| `v:?` | verb, unknown transitivity |
| `phr` | phrase |

### Remarks

* We don't store IPA data, but this can be easily generated from the `pronunciation` value.

## Sentences

*These are not present yet.*

## License

All the data here is licensed under the CC-BY-SA-NC 3.0 (like [Eana Eltu](https://eanaeltu.learnnavi.org/dicts/NaviData.sql) itself).


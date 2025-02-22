# langtag module

Langtag is a module for working with language tag sets. A tag set is a set of
orthographically equivalent tags along with various information. The core data
for the database may be found here: [https://ldml.api.sil.org/langtags.json].

## Installatino

- pip install langtag

langtag is only dependent on python3 and its core libraries (including json).

## Example

```
from langtag import lookup, langtag
t = lookup('en-Latn')       # find a tagset returning a TagSet object
l = langtag('en-Latn')      # create an underling LangTag object
```

See pydoc for details

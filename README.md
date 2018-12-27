# determine archive filetype

determine an archive's filetype using common magic bytes (file signatures)

# requirements

Python v3.0+ because [unicode](https://nedbatchelder.com/text/unipain.html) is [~~hard~~](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/).

# status

development

# example

```
$ python3 ./determine_archive_filetype.py
directory: /users/josh/dev/python/determine-archive-filetype
file: test-doc.rtf, type: rich text format
file: .DS_Store, type: no match
file: tar-cjf.tar.gz, type: bz2
file: screenshot.png, type: png
file: test-doc.docx.lz, type: lzip
file: test.tar.xz, type: xz
file: test-zip.zip, type: zip
file: test-doc.docx.7z, type: 7z
file: test-doc.docx, type: zip
file: determine_archive_filetype.py, type: likely text
file: tar-zcvf.tar.gz, type: gz
```

# license

project license can be found [here](https://github.com/joshschmelzle/determine-archive-filetype/blob/master/LICENSE).

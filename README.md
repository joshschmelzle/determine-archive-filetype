# determine archive filetype

determine an archive's filetype using common magic bytes (file signatures)

this is a very crude alternative to using python-magic, and libmagic that i used for learning purposes

# included magic bytes (file signatures) 

| signature | extension | description |
| ----- | --------- | ----- |  
| \x89\x50\x4e\x47\x0d\x0a\x1a\x0a | png | portable network graphics format |
| \x7b\x5c\x72\x74\x66\x31 | rtf | rich text format |
| \x4c\x5a\x49\x50 | lz | lzip compressed file |  
| \x37\x7a\xbc\xaf\x27\x1c | 7z | 7-Zip file format | 
| \xfd\x37\x7a\x58\x5a\x00 | xz | XZ compression utility using LZMA2 compression |
| \x1f\x8b\x08 | gz | GZIP compressed file | 
| \x42\x5a\x68 | bz2 | compressed file using Bzip2 algorithm | 
| \x50\x4b\x03\x04 | zip | zip file format and formats based on it like jar, xlsx, docx, apk, etc | 

# requirements

Python v3.2+ because [unicode](https://nedbatchelder.com/text/unipain.html) is [~~hard~~](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)

# status

development

# example

```
$ python3 ./determine_archive_filetype.py
directory: /Users/josh/dev/python/determine-archive-filetype
file: test-doc.rtf, type: rtf
file: .DS_Store, type: no match
file: tar-cjf.tar.gz, type: bz2
file: screenshot.png, type: png
file: test-doc.docx.lz, type: lz
file: test.tar.xz, type: xz
file: test-zip.zip, type: zip
file: test-doc.docx.7z, type: 7z
file: test-doc.docx, type: zip
file: determine_archive_filetype.py, type: likely text
file: tar-zcvf.tar.gz, type: gz
```

# license

project license can be found [here](https://github.com/joshschmelzle/determine-archive-filetype/blob/master/LICENSE)

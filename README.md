# evernote-to-markdown
A VERY rough, first-pass Evernote-text-notes converter to Markdown files that I wrote two years ago, as of 2015-10-05. USE AT YOUR OWN RISK. Consider it pre-alpha. At the time, it seemed to do the job fine for plaintext Evernote notes.

### Instructions

1. To run this, you need to install Python (I initially only used it with version 3.3, theoretically any version +3.0 should work), and the late Aaron Swartz's Python script [html2text](https://github.com/aaronsw/html2text) as a subdirectory in the folder hosting this code, aka into subdirectory "html2text". RIP Aaron.

2. Create a subdirectory `output`, where it will put ALL notes, with no subdirectories.

3. Run `python convert.py <Evernote_output_file>.enex`

4. All Evernote notes should be converted into Markdown files in the `output` folder

I have NO idea if this works with the current Evernote .ENEX filetype. Theoretically, you can go to the website for your account / web client, and export at least whole notebooks of Notes as .ENEX files, maybe even individual notes.

IIRC, there's some kind of space thing, where I had to split my .ENEX files into different files no bigger than 60ish MB. This is easy since the .ENEX was (is?) just a specialized XML file type -- in other words, you can open it and play with it using any text editor like Notepad.

From converting these files into Markdown, I found it pretty easy to convert them to Org-mode, etc. [Pandoc](http://pandoc.org/) is your friend, and can do relatively painless conversion between Markdown and Org-mode, etc., a million other formats.

I have no plans to provide updates myself, like for realsies, but I'll gladly respond to / accept pull requests, etc., or co-work on a feature if someone wants it that badly.

Future possibilities that would require more than 15 minutes of work:

1. Interpret and save image files from inside Evernote notes
2. Keep up-to-date with the Evernote .ENEX filetype
3. Clean up the super ugly code.

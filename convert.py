#!/usr/bin/python

# UGH. I guess I'll just do it myself. Give something back to the world.
# made for py3.3, recently adapted for 3.5?

from html2text.html2text import html2text
# import html2text.
import os
import re
import sys

# from ipdb import set_trace
from xml.dom import minidom


def main(argv):
    # evernote_notes = minidom.parse(open("backup_2014_02_06.enex"))
    # ipdb.set_trace()

    evernote_notes = minidom.parse(open(argv[0]))
    
    notes = evernote_notes.getElementsByTagName('note')
    
    for ii in range(0, len(notes)):
        # Rules about titles/filenames: NO commas, colons, slashes, spaces
        # So just mainly periods, hyphens, underscores.
        # You print XML element values with this. srsly? I know, it's insanity
        file_note_name = notes[ii].getElementsByTagName('title')[0].firstChild.nodeValue
        # Because capital letters on the command line are lame.
        file_note_name = file_note_name.lower()
        file_note_name = re.sub(',', '', file_note_name)
        file_note_name = re.sub(':', '', file_note_name)
        # This ugly thing is for forwardslashes as used in Unix.
        file_note_name = re.sub('[[\]/]', '-', file_note_name)
        file_note_name = re.sub(' ', '-', file_note_name)
        file_note_name = re.sub('/', '-', file_note_name)
        print(file_note_name)
    
        if (file_note_name[0] == '-'):
            file_note_name = file_note_name[1:len(file_note_name)]
    
        if not os.path.exists('output/' + file_note_name + '.md'):
            with open('output/' + file_note_name + '.md', 'a') as f_note:
    
                # Title metadata
                f_note.write("Note Title: " + '`' + file_note_name + '`')
    
                # I'm delimiting subday times with semicolons instead of colons, as is normal, due to some obscurities in a vim plugin I use for interfacing with them.
    
                # Created time metadata
                f_note.write("\n")
                created = notes[ii].getElementsByTagName('created')[0].firstChild.nodeValue
                created = created[0:4] + '_' + created[4:6] + '_' + \
                    created[6:8] + '-' + created[9:11] + ';' + created[11:13] + \
                    ';' + created[13:15]
                f_note.write("Note Created: " + '`' + created + '`')
    
                # Updated time metadata
                f_note.write("\n")
                updated = notes[ii].getElementsByTagName('updated')[0].firstChild.nodeValue
                updated = updated[0:4] + '_' + updated[4:6] + '_' + \
                    updated[6:8] + '-' + updated[9:11] + ';' + updated[11:13] + \
                    ';' + updated[13:15]
                f_note.write("Note Updated: " + '`' + updated + '`')
    
                # Tags metadata
                f_note.write("\n")
                f_note.write("Note Tags: ")
                for jj in range(0, len(notes[ii].getElementsByTagName('tag'))):
                    print(notes[ii].getElementsByTagName('tag')[jj].firstChild.nodeValue)
    
                    f_note.write("^" + notes[ii].getElementsByTagName('tag')[jj].firstChild.nodeValue + "^" + ", ")
    
                # Actual Body content
                f_note.write("\n")
                f_note.write("Note Body:")
                f_note.write("\n")
                f_note.write("\n")
                body = notes[ii].getElementsByTagName('content')[0].firstChild.nodeValue
    
    
                # Notes: Raw image information seems to be encoded with <data encoding="base64">. 
                # Based on a search `/encoding="base[^6]` returning nothing, all the image codes appear to be this same base, which is very common.
                # Near/before the raw image data there is also a "file-name" element that would be extremely helpful.
                # However, there's other resource metadata scattered around the "data" element for an image, like "resource-attributes" and "resource", so while parsing images and saving both them to file and inserting markdown links to said data file is possible, it will be a ton of work.
                # Not to mention the question of what format to do it - do you put them in a separate `fig` folder? Just make a copy of the image in the output? Put the images in a new folder with the same name as the note?
                # This is a moderately-sized hole in Austinote at the moment, but I don't really use images in notes that much (or want to reference them absolutely somewhere else), and so I'm not going to deal with it at the moment.
                # I think for the time being I will just have a "figures" folder to allow absolute path linkage in markdown to specific figures on the OS, but I will do this manually.
    
                # Clean up the very ugly body unicode in XML to plain ASCII
                body = re.sub(u'\xa0', '', body)
                body = html2text(body)
                # body = html2text.html2text(body)
    
                # Then turn Aaron's ugly occasional unicode further to ASCII
                # vim gives this as 'e2 80 98', which is the byte hex version of '\xe2\x80\x98', and, through http://www.ltg.ed.ac.uk/~richard/utf-8.cgi?input=e2+80+99&mode=bytes , is apparently unicode '\u2019'
                # body = re.sub(u'\xe2\x80\x98', '\'', body)
                # this works! finally! This should solve all Unicode worries, post-html2text and post-Evernote
                body = re.sub(u'\u2019', '\'', body)
                body = re.sub(u'\u2018', '\'', body)
                # we also have what's in ————————————————————————————————————————————— to deal with, which is e2 80 94, or \u2014
                body = re.sub(u'\u2014', '----', body)
                body = re.sub(u'\u201c', '\"', body)
                body = re.sub(u'\u201d', '\"', body)
    
                body = re.sub('\\\\', '', body)
    
                f_note.write(body)
                f_note.close()
    
        # print(html2text.html2text("<p> Hello world </p>"))

if __name__ == "__main__":
    main(sys.argv[1:])

# Even though Windows and macOS sometimes hide them, most files have file extensions, a suffix that starts with a period (.) at the end of their name. For instance, file names for GIFs end with .gif, and file names for JPEGs end with .jpg or .jpeg. When you double-click on a file to open it, your computer uses its file extension to determine which program to launch.

# Web browsers, by contrast, rely on media types, formerly known as MIME types, to determine how to display files that live on the web. When you download a file from a web server, that server sends an HTTP header, along with the file itself, indicating the file’s media type. For instance, the media type for a GIF is image/gif, and the media type for a JPEG is image/jpeg. To determine the media type for a file, a web server typically looks at the file’s extension, mapping one to the other.

# See developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types for common types.

# In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip

val = input("File name")

val = val.lower().strip()

if "jpg" in val :
    print("image/jpeg")
elif "jpeg" in val :
    print("image/jpeg")
elif "gif" in val :
    print("image/gif")
elif "pdf" in val :
    print("application/pdf")
elif "png" in val :
    print("image/png")
elif "txt" in val :
    print("text/plain")
elif "zip" in val :
    print("application/zip")
elif "bin" in val :
    print("application/octet-stream")
else :
    print("application/octet-stream")


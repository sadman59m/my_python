"""
When we need to handle in memory file, in other words we don't want to save a file
as a file, rather create in memory and do what we want to do with it.
For example, if we want to parse string data from some object and attach the data as a text file
to an email without saving the data as a text file, we can use the in memory tricks.  
"""

# for handling string data, we can use StringIO
from io import StringIO
import base64

# NOTE: if we work with binary data directly, we can use BytesIO from io.ß
buffer = StringIO()

# Lets say we have a messages object which have some messages
messages = [
    "Message text 1",
    "Message text 2",
]

for message in messages:
    buffer.write(f"{message}")
    
# Now, turn the sting buffer into binary byte stings using utf-8. utf-8 represents each characters into a 8 bit/1byte data.
# base64 only takes binary byte data as input.

file_content_bytes = buffer.read().encode('uft-8')

# turn the binary data into the ASCII and then sting
encoded_data = base64.b64encode(file_content_bytes).decode()

# Now we can attach this encoded data as a file content.

"""
We need to do the similar kinds of this while reading from a file. But, We
can read from a file as binary data using 'rb'. So, one step less.
"""
file_data = None
with open("some_file.txt", "rb") as file:
    file_data = file.read()
    
encoded_data = base64.b64encode(file_data).decode()
# CRC-Python
A call-and-response chatbot for python
CRC (or Kirk, as I call it for a human name) is a chatbot that learns from answers. When it does not find something in its dictioary, it asks the user to tell it what to say next time.

CRC works by storing calls and responses in a dictionary. (it's called RespondDict) When it starts, it asks the user if they have a data json file. If they do, then it asks for the name, and loads it. At the end, it saves it again.

CRC is aimed kind of towards teaching kids machine learning, but can be used in everyday projects like controling a MySQL database. Every release comes with a pre-trained data.json module.

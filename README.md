# Thesis
Web fingerprinting using Tor- //
This project focuses in identifying the type of users, inspecting the network traffic of the Tor browser using tools like dumpcap to parse the traffic and t-shark to analyse the traffic.
This involves in collecting a wide range of URLs in different settings such as performing actions using various Tor browser versions, redirecting the pages, clicking on the buttons or links. which helps in creating a difference in the Network traffic that is being collected.
Ideas collecting wide-variety of data:
pefrom actions thru different settings - to make the traffic complicated and classify it based on the differences or the Route it has chosen to reach the server with in the onion network ( menaing: which particular node does it used to respond to the request made )
Use linux tools like sublist3r to gather list of URLs (subdomains) and use it to generate traffic to determine the users based on the Protocol header information.

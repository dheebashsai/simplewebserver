# EX01 Developing a Simple Webserver
## Date:

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
//Html

	<!DOCTYPE html>
	<html>
	
	    <head>
	        <title>TCP/IP Protocol Suite</title>
	        <link rel="stylesheet" href="style.css" />
	        <link rel="stylesheet"
	            href="https://fonts.googleapis.com/css?family=Roboto">
	    </head>
	
	    <body>
	        <div class="container">
	            <h1>TCP/IP Protocol Suite</h1>
	            <table>
	                <tr>
	                    <th>
	                        <h2>Layers</h2>
	                    </th>
	                    <th>
	                        <h2>Protocols</h2>
	                    </th>
	                </tr>
	                <tr>
	                    <td>
	                        <h2>Application Layer</h2>
	                    </td>
	                    <td>
	                        <ul>
	                            <li>HTTP (Hypertext Transfer Protocol)</li>
	                            <li>FTP (File Transfer Protocol)</li>
	                            <li>SMTP (Simple Mail Transfer Protocol)</li>
	                            <li>DNS (Domain Name System)</li>
	                            <li>DHCP (Dynamic Host Configuration Protocol)</li>
	                        </ul>
	                    </td>
	                </tr>
	                <tr>
	                    <td>
	                        <h2>Transport Layer</h2>
	                    </td>
	                    <td>
	                        <ul>
	                            <li>TCP (Transmission Control Protocol)</li>
	                            <li>UDP (User Datagram Protocol)</li>
	                        </ul>
	                    </td>
	                </tr>
	                <tr>
	                    <td>
	                        <h2>Internet Layer</h2>
	                    </td>
	                    <td>
	                        <ul>
	                            <li>IP (Internet Protocol)</li>
	                            <li>ICMP (Internet Control Message Protocol)</li>
	                            <li>ARP (Address Resolution Protocol)</li>
	                        </ul>
	                    </td>
	                </tr>
	                <tr>
	                    <td>
	                        <h2>Network Access Layer</h2>
	                    </td>
	                    <td>
	                        <ul>
	                            <li>Ethernet</li>
	                            <li>Wi-Fi (IEEE 802.11)</li>
	                            <li>PPP (Point-to-Point Protocol)</li>
	                        </ul>
	                    </td>
	                </tr>
	            </table>
	        </div>
	    </body>
	
	</html>
	
	//CSS
	
	body {
		font-family: 'Roboto';	
	font-size: 14px;
	margin: 0px;
	padding: 8px;
	background-color: #f5f5f5;
	}
	.container {
		max-width: 800px;
		margin: 0 auto;
		background: white;
		padding: 16px;
		border-radius: 8px;
		box-shadow: 0 0 10px rgba(0,0,0,0.1);
	}
	.container h1 {
		font-size: 18px;
		padding: 16px 0px;
	}
	.container h2 {
		font-size: 16px;
		padding: 0px;
	}
	table {
	    width: 100%;
	    border-collapse: collapse;
	}
		th, td {
		    border: 1px solid #ddd;
		    padding: 4px 16px;
	    text-align: left;
	}
	th {
	    background-color: #000;
	    color: white;
	}
	ul {
		margin:4px;	
	    padding: 4px 12px ;    
	    border-radius: 5px;
	}
	li {
	    padding: 4px;
	    font-size: 16px;    
	}
	//python
	from http.server import SimpleHTTPRequestHandler
	import socketserver
	
	PORT = 8000
	
	class MyRequestHandler(SimpleHTTPRequestHandler):
	    def do_GET(self):
	        if self.path == "/":
	            self.path = "index.html"
	        return SimpleHTTPRequestHandler.do_GET(self)
	
	# Start the HTTP server
	with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
	    print(f"Serving on port {PORT}...")    
	    try:
	        httpd.serve_forever()
	    except KeyboardInterrupt:
	        print("\nShutting down server...")
	        httpd.shutdown()

## OUTPUT:
![terminal](Terminal.png)
![Output](TCP-IP-List.png)
## RESULT:
The program for implementing simple webserver is executed successfully.

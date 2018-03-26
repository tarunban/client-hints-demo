# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2


class MainPage(webapp2.RequestHandler):
    def get(self):
    	self.response.headers['Accept-CH-Lifetime'] = '300'
        self.response.headers['Accept-CH'] = 'device-memory, dpr, width, viewport-width'

        self.response.write('''
            <!DOCTYPE html>\n
            <html>
            <head>
            <title>Client Hints Demo</title>
            </head>
            <body>
            ''');

        self.response.write('''
            <style>
            li{
            margin: 10px 0;
            }
            </style>
            ''')

        self.response.write('''
            <h1>Background</h1>
            <p style="line-height:1.5">
            Available in 
            <a href="https://www.chromestatus.com/feature/5713139295322112">Chrome 67+</a>.
            </p>

            <p style="line-height:1.5">
            This demo illustrates the use of the
            <a href="https://tools.ietf.org/html/draft-ietf-httpbis-client-hints-05#section-2.2.1">
            Accept-CH
            </a>
            and
            <a href="https://tools.ietf.org/html/draft-ietf-httpbis-client-hints-05#section-2.2.2">
            Accept-CH-Lifetime
            </a>
            response headers to indicate to 
            the user agent which Client Hint request headers should be sent on requests.
            </p>
            ''');

        self.response.write('''
            <h1>Example</h1>
            <p style="line-height:1.5">
            <font face="arial">
            Accept-CH: DPR, Viewport-Width<br>
            Accept-CH-Lifetime: 86400<br>
            </font>
            </p>

            <p style="line-height:1.5">
            A user agent that receives above Accept-CH and Accept-CH-Lifetime response headers,
            or via HTML meta element with http-equiv attribute, should append DPR and
            Viewport-Width request header fields and remember this preference for 86400 seconds.
            If the Accept-CH-Lifetime duration is omitted, then the opt-in only applies for subresource
            requests of the document advertising the Accept-CH policy.
            </p>
            ''');

        self.response.write('''
            <h2>Supported Hints</h2>
            <ol>
            <li>
            <a href="https://tools.ietf.org/html/draft-ietf-httpbis-client-hints-05#section-3.1">
            DPR</a>:
                Indicates the client's current Device Pixel Ratio (DPR).
            </li>
            <li>
            <a href="https://tools.ietf.org/html/draft-ietf-httpbis-client-hints-05#section-3.3">
                Viewport-Width</a>:
                Indicates the layout viewport width in CSS px.
            </li>
            <li><a href="https://tools.ietf.org/html/draft-ietf-httpbis-client-hints-05#section-3.2">
                Width</a>:
                Indicates the desired resource width in physical px (i.e. intrinsic size of an image).
            </li>
            <li><a href="https://w3c.github.io/device-memory/">Device-Memory</a>:
                Indicates device capability for memory i.e. device RAM, in order to 
                enable web apps to customize content depending on device memory constraints.
            </li>
            <li><a href="http://wicg.github.io/netinfo/#save-data-client-hint-request-header-field">
                Save-Data</a>:
                Indicates user agent's preference for reduced data usage.
            </li>
            </ol>
            ''');

        self.response.write('''
            <h2>Under development</h2>
            <ol>
            <li><a href="http://wicg.github.io/netinfo/#-dfn-rtt-dfn-attribute">RTT</a>:
                Indicates the effective round-trip time estimate in milliseconds,
                rounded to nearest multiple of 25 milliseconds, and is based on recently observed
                application-layer RTT measurements across recently active connections.
            </li>
            <li><a href="http://wicg.github.io/netinfo/#-dfn-downlink-dfn-attribute">Downlink</a>:
                Indicates the effective bandwidth estimate in
                <a href="http://wicg.github.io/netinfo/#dfn-mbit-s">megabits per second</a>,
                rounded to nearest multiple of 25 kilobits per second, and is based on recently
                observed application layer throughput across recently active connections.
            </li>
            <li><a href="http://wicg.github.io/netinfo/#effective-connection-types">ECT</a>:
                Represents the
                <a href="http://wicg.github.io/netinfo/#-dfn-effectiveconnectiontype-dfn-enum">
                effective connection type</a> of the current connection.
            </li>
            </ol>
            ''');

        self.response.write('''
            <h1>Demo</h1>
            <p style="line-height:1.5">
            On every visit to this webpage, the server sets
            <b><font face=\"arial\">Accept-CH</font></b> response header to
            <b><font face=\"arial\">device-memory, DPR, width, Viewport-Width</font></b>
            and
            <b><font face=\"arial\">Accept-CH-Lifetime</font></b> response header
            to
            <b><font face=\"arial\">300</font></b> seconds.


            If the user revisits the webpage within 300 seconds of last visit, the browser
            would
            set device-memory, DPR, Viewport-Width on the request headers to the main frame
            as well
            as subresources.

            You can also use
            <a href="https://developers.google.com/web/tools/chrome-devtools/\
            network-performance/reference#headers">
            Chrome Devtools
            </a>
            to see the request and response headers.
            </p>
            ''');
        
        self.response.write("<h2>Main frame client hints received</h2>");
        for key in self.request.headers:
            if key.lower() == 'device-memory' or key.lower() == "dpr" or\
                key.lower() == "width" or key.lower() == "viewport-width" or\
                key.lower() == "rtt" or key.lower() == "downlink" or\
                key.lower() == "ect":
    	            self.response.write("<b>" + key+": " +"</b>")	;        
    	            self.response.write(self.request.headers[key]);
    	            self.response.write("<br><br>");
        self.response.write("<p id=\"toWrite\"></p>");
        self.response.write("<script src=\"subresource.js\"></script>");
        self.response.write('''
            </body>
            <hr>
            <font size=2>
            <a href="https://github.com/tarunban/client-hints-demo">View on GitHub</a>.
            </font>
            </html>
            ''');

class IFramePage(webapp2.RequestHandler):
    def get(self):
    	toWrite = "<h2>Subresource client hints received</h2>"
        for key in self.request.headers:
            if key.lower() == 'device-memory' or key.lower() == "dpr" or\
                key.lower() == "width" or key.lower() == "viewport-width" or\
                key.lower() == "rtt" or key.lower() == "downlink" or\
                key.lower() == "ect":
                    toWrite = toWrite + "<b>" + key+ ": " +"</b>";
                    toWrite = toWrite +  self.request.headers[key] ;
                    toWrite = toWrite + "<br><br>";
	        
        self.response.write("document.getElementById(\"toWrite\").innerHTML =\"" + toWrite  + "\"")

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/subresource.js', IFramePage),
], debug=True)

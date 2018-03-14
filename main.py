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
    	self.response.headers['Accept-CH-Lifetime'] = '3600'
        self.response.headers['Accept-CH'] = 'device-memory, dpr, width, viewport-width'

        self.response.write("<!DOCTYPE html>\n");        
        self.response.write("<html>");
        self.response.write("<body>");
        self.response.write("""The server sets <b><font face=\"arial\"> Accept-CH </font></b> response header to
         <b><font face=\"arial\">device-memory, dpr, width, viewport-width </font></b>and
          <b><font face=\"arial\"> Accept-CH-Lifetime </font></b> response header to 
          <b><font face=\"arial\">3600</font></b> seconds.""")
        self.response.write("<p><h1>Main frame client hints received:</h1></p>");
        for key in self.request.headers:
            if key.lower() == 'device-memory' or key.lower() == "dpr" or key.lower() == "width" or key.lower() == "viewport-width" :
	            self.response.write("<b>" + key+": " +"</b>")	;        
	            self.response.write(self.request.headers[key]);
	            self.response.write("<br><br>");
        self.response.write("<p id=\"toWrite\"></p>");
        self.response.write("<script src=\"subresource.js\"></script>");
        self.response.write("</body></html>");

class IFramePage(webapp2.RequestHandler):
    def get(self):
    	toWrite = "<h1>Subresource client hints received:</h1>"
        for key in self.request.headers:
            if key.lower() == 'device-memory' or key.lower() == "dpr" or key.lower() == "width" or key.lower() == "viewport-width" :
                toWrite = toWrite + "<b>" + key+ ": " +"</b>";
                toWrite = toWrite +  self.request.headers[key] ;
                toWrite = toWrite + "<br><br>";
	        
        self.response.write("document.getElementById(\"toWrite\").innerHTML =\"" + toWrite  + "\"")

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/subresource.js', IFramePage),
], debug=True)

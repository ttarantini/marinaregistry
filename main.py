#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
from main_page import FrontPage
from scrape_page import ScrapePage
from admin_console import Admin
from send_email import SendMail
from yuri_listings import YuriList
from marina_listings import MarinaList
from both_listings import BothList
	
app = webapp2.WSGIApplication([
    ('/', FrontPage),
    ('/scrape_page', ScrapePage),
    ('/admin', Admin),
    ('/send_email', SendMail),
    ('/yuri', YuriList),
    ('/marina', MarinaList),
    ('/both', BothList),
], debug=True)

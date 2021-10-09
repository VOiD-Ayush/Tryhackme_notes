# NIS_Cloud_essentials 

> VOiD | Thursday 29 July 2021 08:08:30 PM IST

# What is 'the cloud'?
The cloud is one of the more current ranges of services offered by the likes of:

Google (GCP)
Amazon (AWS)
Microsoft (Azure)
It involves the usage of on-demand resources that a third-party organisation hosts. Its users can access those resources over the Internet.

Most businesses think about cost and in most cases having a cloud-first approach seems cheaper.

For example, in some countries, organisations must comply with mandatory regulations to operate without inflicting penalties or potentially risk being out of operation. In these cases, risk assessments are carried out to assess the current security controls and whether they are fit for purpose.

It's becoming more common to see computing infrastructures such as servers, software, storage, networking appliances, and databases in the cloud. During the following tasks, we'll explore Amazon AWS and Microsoft Azure Rules of Engagements for penetration testing.

==========================================================

# Firewalls 101
Firewalls are the first line of defence when it comes to majority corporate environments. A very basic and general security configuration for organisations would look similar to this:

network diagram
(image created by Chevalier)

But an ideal approach would look something like this:

network diagram
(image created by Chevalier)

More and more organisations start understanding the importance of having redundancy in the network, but this applies to both network and cloud configurations, which we will cover in just a second. In the end, be aware that budget is always the key influencer when it comes to security. On the other hand, you have your risk assessments that organisations carry out to assess the current security controls and whether they are fit for purpose.

There are a few types of physical firewalls, but most people will classify them in a few major categories:

Packet filtering firewalls
Stateful inspection firewalls
Next-generation firewalls or NGFW
Each of them offers its level of protection, but the more protection a firewall offers, the higher the cost associated with it. An NGFW will be a good choice in most situations, but the cost of supporting and maintaining one is high. On the other hand, a packet filtering firewall is cheaper, and many users are familiar with them as they have been working the same over the years.

The choice of firewall is dependant on a business' or user's risk assessment and budget. In other words, you need to look at:

What dangers am I protected from?
What is the benefit?
How much it costs me to license it?
What's the maintenance cost of maintaining it?
Host devices such as PCs and laptops can also be equipped with firewalls, but in most cases, they are software-based firewalls, and let's not forget about cloud environments! There are Cloud Firewalls available from different providers that you can set up in the cloud environment. You can find out more on the marketplace of the cloud provider you use:

AWS
AZURE
Google
Firewalls all follow the same approach:

Check if the packet matches a rule; if it matches, drop or allow a packet until you hit the default deny or the default allow at the bottom of the firewall ruleset. A very simple explanation of firewalls is below:

network diagram
(image created by Chevalier)

When it comes to NGFirewalls and Cloud Firewalls, they are application-aware, and they are able to track attackers/viruses that try bypassing rules that are set in place in case of a packet filtering firewall.

==========================================================

# Firewalls continued
There is a multitude of firewall solutions available. Each vendor's flagship firewall has its benefits and downsides. Hardware costs, the upfront cost of setting it up, and licensing fees can significantly differ between commercial firewall solutions. All the firewalls mentioned below are available in at least one of the major cloud providers marketplace.

The most common firewalls that you see in organisations nowadays are:

Cisco ASA (Adaptive Security Appliance) or Firepower
Meraki MX (part of Cisco)
FortiGate
Palo Alto
Cisco
Cisco
Cisco
(Image taken from: Wikipedia)

ASAs have been around for a while, and for a good reason. This is partly due to the firewall's functionality, wide availability, and Cisco's support and community. This is a firewall many network engineers or administrators have been exposed to.

For further reading into the benefits of such an appliance, please see the below link:

ASA Firewalls

Cisco Firepower is either a standalone device or a module you can add to your firewall to increase its functionality. This comes with a cost associated and a number of benefits.

The Firepower (appliance or module) assists with traffic filtering and ensuring that the traffic that is allowed throughout the device is compliant with your organisation's guidelines. A significant benefit of Firepower is the Firepower Management Console, where you can apply configuration changes to all your devices with the click of a button, making global deployments and scheduled downtimes easy to conduct and manage.

Meraki MX Firewalls
Meraki

(Image taken from Wikipedia)

Meraki was bought by Cisco in 2012. The Meraki MX line is a solution that is easy to implement and comes with secure default configurations. This type of firewall comes with the benefit of allowing the network team to manage the devices remotely from anywhere in the world from a central console!

The MX firewalls are technically NGFWs that can operate at Layer 7. They are application-aware, which allows the administrator of the device to filter traffic in accordance with the organisation's policies at a granular level.

For more details about the product offerings and costs, check the below link:
Meraki

FortiGate
Fortigate

(Image taken from Real Solutions Technologies)

FortiGate is a brand of firewalls provided by Fortinet. This firewall is less known than the previous one mentioned. Fortinet delivers high-quality products at a cheaper price point. A Fortigate offers the same range of services such as Packet Filtering, Content Filtering, and Unified Threat Management at a good value.

For more details about the product offerings and costs, check the below link:
FortiGate

Palo Alto
Palo Alto
(Image taken from Palo Alto Networks)

Palo Alto offers an expensive range of products compared to the solutions previously mentioned. PAN‑OS is Palo Alto's proprietary software that runs on all Palo Alto's NGFWs, which allows many advanced features compared to its competitors. Palo Alto also offers integrations with SIEM (Security Information and Event Management) solutions such as Splunk, Qradar, and much more. This gives organisations the ability to monitor incidents and possible threats on the network easily.

More details are available on their website:

Palo Alto



There are also free variations such as pfSense.

pfSense
(Image taken from wikipedia)

pfSense can either run on bare-metal or as a virtual machine. There aren't any hidden fees for features, no arbitrary licensing fees, no artificial user limitations for pfSense. There are many packages available to add features to pfSense. For example, IDS (Intrusion Detection Systems) / IPS (Intrusion Protection Systems) / NSM (Network Security Monitoring) integrations such as Snort or Suricata are available for an additional layer of security.

More details about the open-source project are available here:

pfSense

To summarise all the information from this task:

All firewalls fulfil the same purpose of filtering traffic
Each of them uses its own operating system with different commands
Each of them has its benefits and downsides
There is no one size fits all
Firewalls are your first layer of security against an outsider.

=========================================================

# The History of Redundancy and Colocations
Historically speaking, to achieve off-site redundancy for on-premises infrastructure, organisations would either need to design and deploy the redundant infrastructure at another physical location they've owned or rent.

Colocation (also known as 'colo') services have existed for a long time to address business redundancy and disaster recovery needs. These services gained a lot of traction around the e-commerce boom in the mid to late 1990s. Colo services have expanded from just being a place to rent rack space and easy access to an ISP (Internet Service Provider). Typically the bare minimum provides by a colo is power, cooling, and physical security. That said, many colocation providers have started to offer cloud computing, disaster recovery, and even multi-cloud solutions.

Redundancy
Redundancy is something that many organisations had struggled with for years before cloud solutions became readily available. Hosting services and colocation services were available before cloud solutions took off. However, options like this were far from the turn-key compared to the 'have it your way' solutions providers such as Amazon, Google, and Microsoft offer today.

Reputation
Reputation is one of the most important assets for organisations.

You can use websites such as www.rankingthebrands.com or fortune.com to check for brand reputation and changes over the year, and you can see how it fluctuates over time depending on the number of breaches and server failures certain organisations have.

To mitigate these risks, people have added compensating controls to ensure that the risk of having the public-facing assets down is kept to a minimum.

Companies have added redundant load balancers, content delivery networks, cloud gateways and, in the end, multiple web servers to be able to withstand the load! The possibilities are endless with cloud computing, and with Infrastructure as Code (IaC), you can provision extra virtual machines as needed. For instance, if you just need to burst the resources of a host, you can simply do so either from an admin panel or from the console as you see fit.

Load Balancers
Load balancers are what they sound like! They balance the load received by servers by passing a client request, usually to the least busy server.

A non-redundant setup will look like this:

Non redundant setup
(image from Nginx)

A client makes a request over the Internet that gets directed to a Software Load Balancer or Hardware Load Balancer, which then sends over the request to the least busy webserver/application server.

Redundant Load Balancers

Depending on how busy the application is, organisations may add a second load balancer or even create a cluster of load balancers. This could help ensure there is enough capacity to spread the load, ensures failover in the event one of the load balancers stops working, or maintain uptime during scheduled load balancer maintenance.

The image below shows a similar concept as the above image; however, the load is passed to one of the load balancers that passes the load to one of the web servers/application servers.

Redundant setup
(image from e2enetworks.com)

Redundancy can be one of two types:

Active/Passive
Active/Active
In an Active/Passive setup, one of the load balancers is always active, and the second load balancer will wait until the primary load balancer flats out and cannot take any more requests. Then the second load balancer takes the lead and starts delivering the requests to the web servers.

In an Active/Active setup, both load balancers are active, and the load will be distributed evenly to the load balancers.

Load balancers can be of two types:

Software Load Balancers
Hardware Load Balancers
The key differences are cost, setup and use cases.

Content Delivery Network (CDN)
Content delivery networks are beneficial when you have a website that is accessed by many users on a daily basis. The function of a CDN is to cache content from a website and deliver it to the clients from its cache. This helps speed up the process of delivering content to the users; however, some queries and data access might go to the website if the query is not cached.






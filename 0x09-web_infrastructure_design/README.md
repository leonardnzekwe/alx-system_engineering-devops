# Web Infrastructure Design
An ALX SWE Project on Web Infrastructure Design

## Task 0: Simple Web Stack
A design for a one-server web infrastructure to host the website reachable via www.foobar.com Here's a breakdown of the components and their roles, followed by an explanation of the concepts and issues involved.

**Components and Their Roles:**

1. **Server:** A server is a powerful computer system that provides resources and services to other computers, known as clients, over a network. In this case, the server hosts all the necessary components for the website.

2. **Domain Name:** The domain name is a human-readable address that is used to access websites. It serves as a user-friendly alternative to IP addresses. In this setup, the domain name is "foobar.com", and the "www" subdomain is configured to point to the server's IP address (8.8.8.8).

3. **DNS Record for www:** The DNS (Domain Name System) record for the "www" subdomain in www.foobar.com is a CNAME (Canonical Name) record that points to the main domain name, foobar.com. It acts as an alias, allowing users to reach the same destination using different subdomains.

4. **Web Server (Nginx):** The web server's role is to handle incoming HTTP requests from users' browsers and serve them the appropriate content. It acts as an intermediary between the user and the application server. Nginx is a popular web server known for its performance and scalability.

5. **Application Server:** The application server hosts the codebase of the website and processes dynamic content. It takes the user's request, interacts with the database if necessary, and generates the HTML or data to be sent back to the user. This separation of concerns enhances maintainability and scalability.

6. **Application Files (Code Base):** These are the files containing the website's code, including HTML, CSS, JavaScript, and server-side scripts. They are hosted on the application server and are responsible for generating the dynamic content of the website.

7. **Database (MySQL):** The database stores and manages the website's data, such as user information, posts, or any other relevant data. MySQL is a popular relational database management system that efficiently stores and retrieves data.

**Communication Flow:**

When a user wants to access the website via www.foobar.com, the following steps occur:

1. The user's computer sends a DNS query to resolve the domain name www.foobar.com into an IP address. The DNS system returns the server's IP address (8.8.8.8).

2. The user's browser sends an HTTP request to the server (8.8.8.8) for the webpage associated with www.foobar.com.

3. Nginx, the web server, receives the request. It forwards the request to the application server, where the dynamic content is generated.

4. The application server interacts with the MySQL database if needed, retrieves the required data, and generates the HTML content for the webpage.

5. The application server sends the HTML content back to Nginx.

6. Nginx sends the HTML content as an HTTP response to the user's browser.

**Issues with the Infrastructure:**

1. **Single Point of Failure (SPOF):** This setup has a single server, meaning that if the server experiences any hardware or software issues, the entire website could become inaccessible. Redundancy measures, like load balancing and server failover, are missing.

2. **Downtime during Maintenance:** Deploying new code requires restarting the web server. During this time, the website might be temporarily inaccessible. Implementing rolling deployments or a redundant setup can help minimize downtime.

3. **Scalability:** With only one server, it's challenging to handle a significant increase in incoming traffic. As the user base grows, the server might become overloaded. Horizontal scaling (adding more servers) and vertical scaling (upgrading server resources) are needed for scalability.

In conclusion, while this one-server infrastructure is a good starting point, it has limitations in terms of reliability, scalability, and potential downtime during maintenance. To address these issues, introducing redundancy, load balancing, and a scalable architecture would be necessary. Additionally, using cloud services could provide more flexibility and resources to handle varying traffic loads.


## Task 1: Distributed Web Infrastructure
A design for a more robust three-server web infrastructure to host the website www.foobar.com. I'll explain the reasoning behind each element added, the specifics of the setup, and address the issues associated with this infrastructure.

**Components and Their Roles:**

1. **Server 1:** This will act as the primary web server.
2. **Server 2:** This will act as the secondary web server.
3. **Server 3 (Load Balancer):** This server will distribute incoming traffic among the two web servers using HAProxy.
4. **Web Server (Nginx):** The web server handles incoming HTTP requests and serves static content efficiently.
5. **Application Server:** This server processes dynamic content and generates HTML/data for users' requests.
6. **Load Balancer (HAProxy):** The load balancer distributes incoming traffic to the web servers based on a predefined algorithm, increasing scalability and redundancy.
7. **Application Files (Code Base):** These files contain the website's code, including HTML, CSS, JavaScript, and server-side scripts.
8. **Database (MySQL):** The database stores and manages the website's data, such as user information and posts.

**Reasoning Behind Each Element:**

1. **Additional Servers:** Adding multiple servers increases redundancy, fault tolerance, and allows load distribution for better performance and availability.

2. **Load Balancer:** The load balancer evenly distributes incoming traffic among the web servers, preventing overloading and enhancing scalability.

3. **Database Primary-Replica Cluster:** A primary-replica cluster improves database performance, redundancy, and data recovery capabilities.

**Load Balancer Configuration:**

- **Distribution Algorithm:** The load balancer (HAProxy) is configured with a Round Robin distribution algorithm. This algorithm sequentially sends requests to each web server in a cyclical manner.

- **Active-Active Setup:** The load balancer enables an active-active setup, where both web servers actively handle incoming requests simultaneously.

**Primary-Replica Database Cluster:**

A Primary-Replica (Master-Slave) database cluster involves two nodes:

- **Primary Node:** This node handles write operations and updates to the database. It's responsible for maintaining the most up-to-date version of the data.

- **Replica Node:** The replica node(s) handle read operations and are synchronized with the primary node's data. They provide redundancy and improve read scalability.

**Differences Between Primary and Replica Nodes:**

- **Primary Node:** Handles write operations, updates, and modifications to the database. It's crucial for maintaining data integrity and consistency.

- **Replica Node:** Handles read operations, providing faster data retrieval and allowing the primary node to offload some read traffic. However, it cannot handle write operations.

**Issues with the Infrastructure:**

1. **Single Point of Failure (SPOF):** Despite the redundancy in the web servers and database, the load balancer remains a potential single point of failure. Implementing a redundant load balancer setup could mitigate this issue.

2. **Security Issues:** The absence of a firewall and HTTPS leaves the infrastructure vulnerable to attacks and data interception. Implementing a firewall and enabling HTTPS (SSL/TLS) encryption is essential for security.

3. **No Monitoring:** Without proper monitoring tools, it's challenging to identify performance bottlenecks, resource utilization, and potential issues. Implementing monitoring solutions helps ensure the health and performance of the infrastructure.

In summary, the three-server infrastructure with load balancing, a primary-replica database cluster, and redundancy addresses many of the limitations of the previous setup. However, the issues related to SPOF, security, and monitoring still need to be properly addressed to create a truly robust and secure environment.


## Task 2: Secured and Monitored Web Infrastructure
A design for a secure and monitored three-server web infrastructure for www.foobar.com. I'll explain the rationale behind each addition, the significance of certain elements, and then delve into the specifics of the setup.

**Components and Their Roles:**

1. **Server 1 (Primary Web Server):** Serves as the primary web server.
2. **Server 2 (Secondary Web Server):** Acts as a secondary web server for redundancy.
3. **Server 3 (Load Balancer):** Distributes incoming traffic and terminates SSL encryption.
4. **Firewalls:** Placed to protect servers from unauthorized access and cyber threats.
5. **SSL Certificate:** Enables HTTPS for secure and encrypted data transfer.
6. **Monitoring Clients:** Gather data about server performance and health for monitoring purposes.

**Reasoning Behind Each Element:**

1. **Firewalls:** Firewalls are added to bolster security by controlling incoming and outgoing network traffic. They act as barriers against malicious attempts to compromise the servers.

2. **SSL Certificate:** An SSL certificate is crucial to enable HTTPS, which encrypts the communication between users' browsers and the server, ensuring data confidentiality and integrity.

3. **Monitoring Clients:** Monitoring is essential for identifying performance issues, security breaches, and other abnormalities in real-time, allowing for timely intervention and optimization.

**Traffic Encryption with HTTPS:**

- **Why HTTPS:** Serving traffic over HTTPS is essential to ensure the security and privacy of users' data during transmission. It prevents eavesdropping, data tampering, and man-in-the-middle attacks.

**Monitoring and Data Collection:**

- **Purpose of Monitoring:** Monitoring helps to proactively identify and address issues affecting server performance, security, and availability.

- **Monitoring Tool Data Collection:** The monitoring tool collects data through monitoring clients deployed on each server. These clients gather information about CPU usage, memory utilization, network traffic, response times, and other relevant metrics.

**Monitoring Web Server QPS:**

To monitor web server QPS (Queries Per Second):

1. Set up monitoring tools to collect data from the web servers.
2. Monitor the incoming request rate on each web server, which can provide insight into the QPS.
3. Analyze the collected data to understand trends and patterns in request rates, helping to optimize server resources.

**Issues with the Infrastructure:**

1. **Terminating SSL at Load Balancer Level:** Terminating SSL at the load balancer could expose sensitive data to potential attacks within the network. To address this, SSL should be terminated at the application servers instead, ensuring end-to-end encryption.

2. **Single MySQL Server Capable of Accepting Writes:** Relying on a single MySQL server for write operations poses a single point of failure. Implementing a primary-replica MySQL cluster with a master-slave setup could offer redundancy and fault tolerance.

3. **Identical Components on All Servers:** Having all servers with the same components (database, web server, and application server) could lead to resource contention and bottlenecks. Differentiating server roles by distributing components based on their specific functions can improve performance and resource utilization.

In conclusion, this design aims to create a secure, encrypted, and monitored web infrastructure for www.foobar.com. By incorporating firewalls, SSL certificates, monitoring clients, and addressing key issues, we enhance the security, availability, and performance of the system.


## Task 3: Scale up
This setup will include two servers with a load balancer (HAProxy) configured as a cluster, each server containing specific components. I'll explain the rationale behind each addition.

**Components and Their Roles:**

1. **Server 1 (Web Server):** This server hosts the web server (Nginx) component, handling incoming HTTP requests and serving static content efficiently.

2. **Server 2 (Application Server):** This server hosts the application server component, processing dynamic content and generating HTML/data for users' requests.

3. **Server 3 (Database):** This server hosts the database component (MySQL), storing and managing the website's data.

4. **Load Balancer Cluster:** HAProxy load balancer is configured as a cluster to distribute incoming traffic evenly across the web and application servers for load distribution and high availability.

**Reasoning Behind Each Element:**

1. **Separate Servers for Components:** Separating components onto different servers enhances modularity, scalability, and resource isolation. It also reduces potential conflicts and allows for optimized configuration for each component.

2. **Load Balancer Cluster:** The load balancer cluster ensures even distribution of incoming traffic among the web and application servers. This enhances performance, fault tolerance, and high availability by eliminating a single point of failure.

In summary, this design divides the infrastructure into three separate servers, each dedicated to a specific component (web server, application server, and database), and implements a load balancer cluster for distributing incoming traffic. This architecture enhances scalability, performance, and reliability.

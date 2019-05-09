# IST303-G4-GroupProject
<h2>Team Name:</h2>
QuEST
<h2>Team Members:</h2> Eunice Kang, Quan Zhou, Sahith Cheera

<h2>How to run the application:</h2>
<h3>Requirements:</h3>
<ul>
  <li>Python 3.7.1</li>
  <li>pip 19.0.3</li>
  <li>Virtual Environment 16.4.0</li>
</ul>
  
<h3>Run Application:</h3>
<ol>
  <li>In the application root folder,
<pre><code>
# In Windows
.\virtenv\Scripts\activate
# In Mac
source virtenv/Scripts/activate
</code></pre>
    You might have to <code>pip install -r requirements.txt</code> due to OS differences.
  </li>
  <li>Now, run the app Django server.<br>
    <code>
      python manage.py runserver
    </code>
  </li>
  <li>Something like this should show up:
<pre><code>
System check identified no issues (0 silenced).
April 03, 2019 - 14:24:08
Django version 2.1.7, using settings 'quest.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
</code></pre>
  </li>
  <li>Copy the http link given and paste into a web browser.</li>
  <li>To stop server: Ctrl+C</li>
  <li>Deactivate the virtual environment</li>
</ol>

<h3>Run Discord Monitor script:</h3>
(Will not work properly do to disconnected services)<br>
In the application root folder, run <code>python monitor.py</code>

<h3>Tests:</h3>
In the application root folder, run <code>pytest</code>

<h2>Application Concept: </h2>

A universal product monitor. Capable of monitoring any site for products based on keywords or brand/shop. Optimized for Shopify. Sends alerts via Discord when products are restocked or dropped.

<h2>Stakeholders: </h2>
Buyers/Users - people using the website to monitor a product.
Shops/Companies - people will be directed to their own websites to purchase the monitored products


<h2>User Stories:</h2>

<h3>1. Product Search - priority 20 - 6 days</h3>
As a user, I can search for products.

<h3>2. Product Browsing - priority 20 - 12 days</h3>
As a user, I can browse the websites for products.

<h3>3. User Account - priority 40 - 5 days</h3>
As a user, I can login and save user information.

<h3>4. Monitor Product - priority 30 - 14 days</h3>
As a user, I can save products to monitor.

<h3>5. Receive Notification - priority 30 - 5 days</h3>
As a user, I will receive notifications when a product restocks or a new product drops.

<h3>6. Catalog - priority 10 - 12 days</h3>
As an admin, I can choose products for the site catalog.

<h2>Decomposition of User Stories:</h2>
<ol>
<li>As a user, I can search for products. (6 days) - priority: 20
  <ul>
    <li>Search interface (Eunice)</li>
    <li>Search function and optimization (Eunice) </li>
  </ul>
</li>
<li>As a user, I can browse the websites for products. (12 days) - priority: 20
  <ul>
    <li>Home, brand, products page (Sahith)</li>
    <li>Filter and sort (Sahith)</li>
    <li>Database for products (Quan)</li>
  </ul>
</li>
<li>As a user, I can login and save user information. (5 days) - priority: 40
  <ul>
    <li>Registration and login page (Sahith)</li>
    <li>Database for user information (Quan)</li>
  </ul>
</li>
<li>As a user, I can save products to monitor. (14 days) - priority: 30
  <ul>
    <li>Add products (Sahith)</li>
    <li>Register with the monitor (Quan)</li>
  </ul>
</li>
<li>As a user, I will receive notifications when a product restocks or a new product drops. (5 days) - priority: 30
  <ul>
    <li>Page monitor (Quan)</li>
    <li>Notification (Eunice)</li>
  </ul>
</li>
<li>As an admin, I can choose products for the site catalog. (12 days) - priority: 10
  <ul>
    <li>Admin interface for managing users and content (Eunice)</li>
  </ul>
</li>
</ol>

<h2>Milestone 1.0:</h2>
<ol>
  <li>Catalog
    <ul>
      <li>Admin interface</li>
    </ul>
  </li>
  <li>Product Browsing
    <ul>
      <li>Home, brand, products pages</li>
      <li>Filter and sort</li>
      <li>Products database</li>
    </ul>
  </li> 
  <li>Product Search
    <ul>
      <li>Search interface</li>
      <li>Search function and optimization</li>
    </ul>
  </li>
</ol>

<h3>2 Iterations for Milestone 1.0: (30 days)</h3>
<ul>
  <li>Iteration 1: (15 days)
     <ul>
       <li>Admin interface</li>
       <li>Search interface</li>
       <li>Home, brand, & products page</li>
     </ul>
  </li>
  <li>Iteration 2: (15 days)
    <ul>
      <li>Products database</li>
      <li>Search function and optimization</li>
      <li>Filter and sort</li>
    </ul>
  </li>
</ul>

<h2>Milestone 2.0:</h2>
<ol>
  <li>User Registration
    <ul>
      <li>Registration, login, and user profile pages</li>
      <li>Custom table for user information</li>
    </ul>
  </li>
  <li>Product Monitor
    <ul>
      <li>Save product to profile</li>
      <li>Notification script</li>
    </ul>
  </li> 
</ol>

<h3>2 Iterations for Milestone 2.0: (30 days)</h3>
<ul>
  <li>Iteration 1: (15 days)
     <ul>
       <li>Custom table for user information</li>
       <li>Registration, login, and user profile pages</li>
     </ul>
  </li>
  <li>Iteration 2: (15 days)
    <ul>
      <li>Save product to profile</li>
      <li>Notification script</li>
    </ul>
  </li>
</ul>

<h2>Velocity:</h2>
  Timeline: 34 days until Milestone 1.0 is due, 62 days until Milestone 2.0 is due <br>
  Velocity: 33%

<h2>Burn Down Chart:</h2>
https://app.zenhub.com/workspaces/quest-5c7773a304004e3ba48b73b3/reports/burndown?milestoneId=4095391&selectedPipelines=5c7773a304004e3ba48b73b2

<h2>Stand Up Meetings:</h2>
https://docs.google.com/document/d/1Mx9A8oGmECCpuB7SF3sfGk1WLctAKHb8VLbcBaVW2fk/edit?usp=sharing

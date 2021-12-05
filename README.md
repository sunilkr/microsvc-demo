# A MicroService demo using NGINX and Flask

## Services

### Gateway

Gateway is a NGINX instace used a reverse proxy. It passes client requests to downstream services based on path.

### UserSvc

This is a user service for maintianing user credentials. This will act as Authentication Proxy and session management.

### Library

This serves books already purchased by the user. __Requires a valid session.__

### ShopeSvc
This service allows user's to purchanse books or subscriptions. __Requires a valid session.__

### CatalogueSvc
This shows book catalougues to users. Can be accessed without valid session. Shall tack visited items.

# Working

* Services are loaded and can be called by direct ports+url.

# Not Working

* Looks like NGINX config issue.

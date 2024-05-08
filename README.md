# django_sso_jwt
messy implementation of SSO UI authentication using CAS and JWT

due to sso ui behavior, `django-cas-ng` library is forked directly into the project to supply the `User-Agent` header to the cas clients ticket verification request

general flow of cas authentication:
1. User logs into the /login endpoint
2. App redirects to CAS Client via /login endpoint
3. CAS Client authenticates the user, and fetches to the /login endpoint, passing a ticket.
4. /login handler validates the ticket against the CAS server.
6. CAS server validates the ticket, and returns a response containing the user data
7. handler updates or creates a session ticket associating with the CAS ticket
8. if configured for CAS proxy functionality, handler updates or deletes the proxy-granting tickets (PGT) as necessary.

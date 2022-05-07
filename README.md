# Dentasis

## About this project

This is a demo api for caries diagnosis and detection.
This demo is deployed on heroku but its api is not available for its integration with any client application because of its CORS settings:

- API: https://dentasisapi.herokuapp.com/api/
- Swagger docs: https://dentasisapi.herokuapp.com/swagger/

### API Documentation

In order to use the swagger docs, you must follow this steps:

- Go to the API Documentation provided with swagger: https://dentasisapi.herokuapp.com/swagger/
- Register on [(POST) /accounts/register/] with a real email.
- Go to the link that was send to your email and it will activate the account.
- Login on [(POST) /accounts/login/] with your credentials
- The previous step will provide a token. Copy the token and authorize your access into swagger by clicking the "Authorize" green button on the upper right section of the interface and insert the token with this format:

```bash
Bearer (Token)
```

- You are now authenticated on the swagger interface and you have the authorization of using most of the api endpoints. Some are reserved for staff only.


## Configure .env file

In order to run locally, you must create a .env file on the root folder and set these configurations:

```bash
SECRET_KEY=A$$S0M3-$3CR3T-K3Y # set this to whatever random string
DEBUG=1 # set this to 1 for development configuration. 0 for production.
ALLOWED_HOSTS=localhost 127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost http://127.0.0.1

# You must set a email and enable "Less secure app access" on that account
# if its an gmail account: https://support.google.com/accounts/answer/6010255#zippy=
PAULSOFT_EMAIL_USER=email@email.com
PAULSOFT_EMAIL_PASSWORD=password
EMAIL_VERIFICATION_URL=http://localhost:3000/activate/

# Set the configuration of your local mssql DB
DB_LOCAL_NAME=dentasisdb
DB_LOCAL_USER=sa # set your own credentials
DB_LOCAL_PASSWORD=password # set your own credentials
DB_LOCAL_HOST=localhost
DB_LOCAL_PORT=
```

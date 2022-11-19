# Flask Web App Development

## Overview

For this project Flask and Next JS is combined to build a full stack web app. Next Js build is used to generate the staic files required for flask app

Contains the following features

- Next JS web app - Authentication UI - Tailwind | Typescript | React Hook Form
- Flask MongoDb integration
- Flask User Authentication - Login / Signup / Forgot Password
- Login with Google
- Login with Github
- Session
- Protected Pages
- Image Compressor | Protected

## File Structure

-- app ( Flask APP )
-- frontend ( Next JS APP)
-- venv ( Virtual Enviroment for Python)
-- transfer.py ( Used to transfer next js build to flask app)

## How to use ?

### Flask APP

---

1. Activate the venv --> `. venv/etc/activate`
2. Open the app folder --> `cd app`
3. Run the flask app --> `flask --debug run --port=5001 --host=0.0.0.0`

### Next JS APP

---

1. Switch to frontend folder --> `cd frontend`
2. Run the next js app --> `npm run dev` to build use `npm run build`

Note : It creates a `templates` folder inside the next js app

### Move Build to flask app

---

Once build is ready swich to main directory and run `tranfer.py` this will transfer the `templates` folder to flask and static files inside the `templates` folders is moved to flasks static folder `/_next/static`

### Configs

Create the enviroment variables on your system for
`MONGO_SERVER_URI`

eg for mac it's
`export MONGO_SERVER_URI=mongodb+srv://username:password@database.ajods1ldsdskc.mongodb.net/?retryWrites=true&w=majority`

for windows : https://www.computerhope.com/issues/ch000549.htm
for linux : https://www.freecodecamp.org/news/how-to-set-an-environment-variable-in-linux/

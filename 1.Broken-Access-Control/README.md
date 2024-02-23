### Node Environment Installation
- #### Node installation on Windows

  Just go on [official Node.js website](https://nodejs.org/) and download the installer (Latest).
Also, be sure to have `git` available in your PATH, `npm` might need it (You can find git [here](https://git-scm.com/)).


If the installation was successful, you should be able to run the following command.

    // node --version
    v8.11.3

    // npm --version
    6.1.0


###
## Installation and Setup Instructions

Follow these steps to set up the project environment and start the server.

### Step 1: Install NPM Libraries

To install the necessary npm libraries, run the following command in your terminal:

```bash
npm install

```

### Step 2: Configure Environment Variables

Create a `.env` file in the root directory of the project and configure the required details. Make sure to include the Postgres database configurations:

```
# Example of .env content
PORT="3555"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "DarkSideNoMore"
SECRET = "123"
DB_PORT = "5432"
DB_USERNAME = "postgres"
DB_HOST = "localhost"
DB_NAME = "wierd-securitatis"
DB_PASSWORD = "123"

### Step 3: Initialize the Database

Run `initDB.js` to initialize the database using the following command:

### Step 4: Start the Express.js Server

Finally, start the Express.js server by executing `index.js`:

```bash
node index.js
```

After running this command, your server should be listening on the port specified in your `.env` file.

---
##Story
Access Control Mishap:

In the expansive galaxy of digital systems, the Null InfoSec Chapter shines as a guiding star in cybersecurity. Armed with unmatched expertise, they defend the integrity of our digital realm against all threats, known and unknown.

As active participants in this cosmic battle, you are not mere contenders but guardians of the digital frontier. The Null InfoSec Chapter raises the alarm – an Access Control Mishap jeopardizes the very essence of our digital presence. Fragments of a potent artifact, scattered across distant planets, face the risk of falling into malevolent hands.

In this pivotal moment, the Null InfoSec Chapter summons your expertise and creativity to reinforce defenses against the Access Control Mishap. Together, we must mend the chinks in our digital armor, ensuring that only those with rightful permissions can access the artifact fragments.

By aiding the Null InfoSec Chapter in this mission, you not only bolster the security of the digital cosmos but also uphold the values of integrity and accountability in the realm of cybersecurity. Let us unite to confront this challenge and protect the secrets of the galaxy from exploitation by those who seek to misuse them.







### Flag:

```
`NULL{"Controlled_Entrance_Flag"}`
```
---
### HINTS:


#### 1. "May the Force be with you as you unravel the secret. Patience, persistence, and a Jedi's calm mind are your allies. Attempt each combination, but efficiency matters. Use the Force to guide your systematic exploration." (-10)
#### 2.  "Decrypt the secret within the Jedi's encrypted holocron by delving into the art of key generation in the Force. Common practices hold the wisdom you seek. Trust the Force to reveal the way." (-5)
#### 3.  "Use the strength of the Dark Side to brute force the secret, a 3-digit Sith passcode. Channel your inner Sith Lord and let no combination escape your power." (-30)


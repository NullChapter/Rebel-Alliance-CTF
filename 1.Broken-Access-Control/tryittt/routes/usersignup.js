const bcrypt = require('bcrypt');
const { createUser } = require("../db");


module.exports = async (req, res) => {
    try {
        const { username, password } = req.body;

        if (username === "admin") {
            throw new Error("Admin user already exists!");
        }

        // Hash the password before storing it
        const saltRounds = 10; // Adjust the salt rounds as needed
        const hashedPassword = await bcrypt.hash(password, saltRounds);

        // Call createUser with the hashed password
        const ret = await createUser(username, hashedPassword);

        if (ret !== -1) {
            return res.json({ "message": "User registered successfully!" });
        } else {
            return res.json({ "message": "User exists" });
        }
    } catch (err) {
        // Proper error handling to understand the error
        console.error("Error during user registration:", err);
        return res.status(500).json({ "error": err.message || "Internal Server Error" });
    }
};

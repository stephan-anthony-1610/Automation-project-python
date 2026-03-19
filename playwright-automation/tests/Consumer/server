const express = require('express');
const app = express();

app.use(express.json());

// Store data in memory (for testing)
let database = {};

app.patch('/employees/:id', (req, res) => {
    const empId = req.params.id;
    const data = req.body;

    // Store/update data
    database[empId] = {
        ...(database[empId] || {}),
        ...data
    };

    console.log("PATCH received:", empId, data);

    res.json({
        status: "updated",
        empId: empId,
        updatedData: database[empId]
    });
});

// Optional: GET to verify updates
app.get('/employees/:id', (req, res) => {
    res.json(database[req.params.id] || {});
});

app.listen(3000, () => console.log("Server running"));
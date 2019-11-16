const express = require("express");
const spawn = require("child_process").spawn;

const app = express();


app.use(express.static(__dirname + "/public"));

app.use(express.json());





app.get("/", (req, res) => {
  let arg1 = "Moro kaikki";
  const pythonProcess = spawn('python3',["./script.py", arg1]);
  pythonProcess.stdout.on('data', (data) => {
    console.log("Python is being executed");
    console.log(data.toString());
    });
  res.end();
});


const port = process.env.PORT || 8080;
app.listen(port, () => console.log(`App is listening on port ${port}...`));
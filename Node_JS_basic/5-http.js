const http = require('http');
const fs = require('fs');

const database = process.argv[2];

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.statusCode = 200;
    res.end('Hello Holberton School!');
    return;
  }

  if (req.url === '/students') {
    res.statusCode = 200;
    res.write('This is the list of our students\n');

    fs.readFile(database, 'utf8', (err, data) => {
      if (err) {
        res.end('Cannot load the database');
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);

      res.write(`Number of students: ${students.length}\n`);

      const fields = {};

      students.forEach((line) => {
        const parts = line.split(',');
        const firstname = parts[0];
        const field = parts[parts.length - 1];

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });

      Object.keys(fields).forEach((field) => {
        res.write(
          `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`,
        );
      });

      res.end();
    });
    return;
  }

  res.statusCode = 404;
  res.end();
});

app.listen(1245);

module.exports = app;

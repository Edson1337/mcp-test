const http = require('http');

const port = 3000;

const tools = {
  sum: (a, b) => a + b,
  divide: (a, b) => {
    if (b === 0) throw new Error('Division by zero');
    return a / b;
  }
};

const server = http.createServer((req, res) => {
  if (req.method === 'POST' && req.url === '/tool') {
    let body = '';
    req.on('data', chunk => { body += chunk.toString(); });
    req.on('end', () => {
      try {
        const { tool, a, b } = JSON.parse(body);
        if (!tools[tool]) {
          res.statusCode = 400;
          return res.end('Tool not found');
        }
        const result = tools[tool](a, b);
        res.end(JSON.stringify({ result }));
      } catch (e) {
        res.statusCode = 400;
        res.end('Invalid input or error: ' + e.message);
      }
    });
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});

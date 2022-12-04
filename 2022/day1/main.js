const fs = require('fs');
data = fs.readFileSync("input.txt", "utf8");
calories = data.split('\n\n').map(e => e.trim().split('\n')).map(e => e.map(c => parseInt(c))).map(e => e.reduce((a, b) => a + b)).sort((a, b) => b - a);
console.log("Part 1:", calories[0]);
console.log("Part 2:", calories[0] + calories[1] + calories[2]);

const fs = require("fs");
let raw = fs.readFileSync("entries.json", "utf8");
let entries = JSON.parse(raw);
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("give me your blood sugar: ", x => {
	const entry = x;
        entries.push({
		amount: entry.slice(0,3),
		time: entry.slice(5,9),
		date: entry.slice(10,19),
	})
        var outt = entries.map(item => {return `it was ${item.amount} mg/dl in ${item.time} of the day ${item.date}`}); console.log(outt);
	let neww = JSON.stringify(entries, null, 4);
	fs.writeFileSync("entries.json", neww, "utf8") 
	rl.close(); });



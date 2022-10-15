console.log("hello");
var fs = require("fs");
var exec = require("child_process");
const process = require("process");

let rawdata = fs.readFileSync("dataset.json");
let repos = JSON.parse(rawdata);

Object.entries(repos).forEach(([key, value]) => {
	// // Shallow clone Git repository
	exec.exec(
		`git clone --depth=1 ${value.url} ${value.user.name}-${value.name}`
	);
	// // Create new folder COMPENDIUM ISSUE MULTIPLE SAME NAME THINGS
	fs.mkdirSync(`${value.user.name}-${value.name}-Results`);
	//Redirect to new folder
	process.chdir(`./${value.user.name}-${value.name}-Results`);
	// Note, need to make a whole path variable to here and need to store it. Thing can't find with just the name of repo C:/Users/Kinan/Documents/Homework/P4P/analyse/
	// C:\Users\Kinan\Documents\Homework\P4P\analyse\\
	exec.exec(
		`clang --analyze -Xclang -analyzer-checker=wasm ../${value.user.name}-${value.name}/**/*`
	);
	// Exit out of current directory
	process.chdir("../");
});

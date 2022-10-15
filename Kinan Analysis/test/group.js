const fs = require("fs");
const path = require("path");
// Get all files with a .c or .cpp, or .h extension in all subfolders recursively

let map = {};

let id = 0;

const getDirectoryContents = (basePath, output) => {
	const files = fs.readdirSync(basePath);

	for (const file of files) {
		const filePath = path.join(basePath, file);
		const fileInfo = fs.lstatSync(filePath);
		if (fileInfo.isDirectory()) {
			getDirectoryContents(filePath, output);
		} else if (fileInfo.isFile()) {
			const fileExt = file.split(".")[file.split(".").length - 1];
			if (["c", "cpp", "h"].includes(fileExt)) {
				map[`${id}.${fileExt}`] = filePath;

				fs.copyFileSync(filePath, `${output}/${id}.${fileExt}`);
				id++;
			}
		}
	}
};

const regex = /#include "(.*)"/g;

const fixRelativeIncludes = (output) => {
	const json = JSON.parse(fs.readFileSync(`${output}/out.json`));

	const reverseFileLookup = Object.entries(json).reduce((acc, [key, value]) => {
		acc[value] = key;
		return acc;
	}, {});

	for (const [file, originalPath] of Object.entries(json)) {
		const contents = fs.readFileSync(`${output}/${file}`, "utf-8");

		let finalContents = contents;
		let array1;
		while ((array1 = regex.exec(contents)) !== null) {
			const includePath = array1[1];

			// resolve actual path
			const actualPath = path.join(
				originalPath.replace(/\/[^\/]+$/, ""),
				includePath
			);

			// get new name of actual file
			const newPath = reverseFileLookup[actualPath];

			finalContents = finalContents.replace(includePath, newPath);
		}

		fs.writeFileSync(
			`${output}/${file}`,
			`// ${originalPath}\n${finalContents}`
		);
	}
};

const flattenRepo = (name) => {
	const output = `output/${name}`;
	fs.mkdirSync(output, { recursive: true });
	getDirectoryContents(name, output);

	fs.writeFileSync(`${output}/out.json`, JSON.stringify(map, null, 2));
	fixRelativeIncludes(output);
	map = {};
	id = 0;
};

const runOnFolders = () => {
	const files = fs.readdirSync(".");
	fs.mkdirSync("output", { recursive: true });

	for (const file of files) {
		const fileInfo = fs.lstatSync(file);
		if (fileInfo.isDirectory() && file !== "output") {
			flattenRepo(file);
		}
	}
};

runOnFolders();

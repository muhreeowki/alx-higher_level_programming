#!/usr/local/bin/node

const initialList = require("./100-data").list;
const newList = initialList.map((val, index) => val * index);
console.log(initialList);
console.log(newList);
#!/usr/bin/node

const req = require('request');
let url = "https://swapi-api.alx-tools.com/api/films/3/";
let data = {};

req.get(url, (error, response, body) => {
	if (error) {
        console.error('Error:', error);
    } else if (response.statusCode === 200) {
        data = JSON.parse(body);
	    for (let i = 0; i < data["characters"].length; i++) {
        		req.get(data["characters"][i], (e, r, b) => {
				if (e) {
					console.error('Error:', e);
				}
				else if (r.statusCode === 200) {
					console.log(JSON.parse(b)["name"]);
				} else {
					console.log("failed with a status code:" , r.statusCode);
				}
			});
		}
    } else {
        console.log('Failed with status code:', response.statusCode);
    }
});

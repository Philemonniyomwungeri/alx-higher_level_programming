#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
	if (error) {
		console.error('error:', error);
	} else if (response.statusCode !== 200) {
		console.error(`Error: ${response.statusCode}`);
	} else {
		const tasks = JSON.parse(body);
		const completedTasks = {};

		tasks.forEach(task => {
			if (task.completed) {
				if (!completedTasks[task.userId]) {
					completedTasks[task.userId] = 0;
										        }
					completedTasks[task.userId]++;
			}
					});

		console.log(completedTasks);
		}
});

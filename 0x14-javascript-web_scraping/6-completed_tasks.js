#!/usr/bin/node

/* use requests */
const request = require('request');

/* set variables */
const urlTodos = process.argv[2];

request(urlTodos, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const tasks = JSON.parse(body);
  const userCompleted = {};
  for (const task of tasks) {
    if (task.completed) {
      if (userCompleted[task.userId]) {
        userCompleted[task.userId] += 1;
      } else {
        userCompleted[task.userId] = 1;
      }
    }
  }
  console.log(userCompleted);
});

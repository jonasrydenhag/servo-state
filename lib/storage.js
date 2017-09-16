'use strict';

var config = require('../config.json');
var firebase = require('firebase-admin');
var Promise = require('promise');

var serviceAccount = require('../firebase-account.json');

firebase.initializeApp({
  credential: firebase.credential.cert(serviceAccount),
  databaseURL: config.firebase.databaseURL
});

var db = firebase.database();
var statesRef = db.ref("states");

function pushState(state) {
  if (state !== "on" && state !== "off") {
    throw new Error("Invalid state: " + state);
  }

  return statesRef
    .push({
      state: state,
      createDate: firebase.database.ServerValue.TIMESTAMP
    });
}

function lastState() {
  return new Promise(function (resolve, reject) {
    statesRef
      .orderByChild("createDate")
      .limitToLast(1)
      .once("value", function (snapshot) {
        if (snapshot.hasChildren() === true) {
          snapshot.forEach(function (data) {
            resolve(data.val().state);
          });
        } else {
          resolve(null);
        }
      })
      .catch(function (ex) {
        reject(ex);
      });
  });
}

module.exports = {
  push: pushState,
  state: lastState
};

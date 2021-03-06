#!/usr/bin/env node

'use strict';

var debug = require('debug')('servoState');
var led = require('../led');
var Promise = require('promise');
var servo = require('../blueServo');
var storage = require('./lib/storage');

function on () {
  return changeState("on");
}

function off () {
  return changeState("off");
}

function currentState () {
  return storage.state();
}

function changeState (state) {
  return new Promise(function (resolve, reject) {
    if (state !== undefined && state !== "on" && state !== "off") {
      throw new Error("Invalid state: " + state);
    }

    currentState()
      .then(function (currentState) {
        if (state === currentState) {
          resolve(state);
        } else {
          if (state === undefined) {
            state = currentState === "on" ? "off" : "on"
          }

          servo.press()
            .then(function () {
              storage.push(state);

              resolve(state);

              if (state === "on") {
                led.on();
              } else {
                led.off();
              }
            })
            .catch(function (ex) {
              reject(ex);
            });
        }
      })
      .catch(function (ex) {
        reject(ex);
      });
  });
}

(function(){
  module.exports.change = changeState;
  module.exports.on = on;
  module.exports.off = off;
  module.exports.state = currentState;

  if (module.parent === null) {
    var state = process.argv[2];

    changeState(state)
      .then(function (newState) {
        debug(newState);
        process.exit();
      })
      .catch(function (ex) {
        debug(ex);
        process.exit(1);
      });
  }
})();

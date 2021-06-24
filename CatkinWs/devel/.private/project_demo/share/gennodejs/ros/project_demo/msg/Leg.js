// Auto-generated. Do not edit!

// (in-package project_demo.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Leg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.tigh = null;
      this.knee = null;
      this.foot = null;
    }
    else {
      if (initObj.hasOwnProperty('tigh')) {
        this.tigh = initObj.tigh
      }
      else {
        this.tigh = 0.0;
      }
      if (initObj.hasOwnProperty('knee')) {
        this.knee = initObj.knee
      }
      else {
        this.knee = 0.0;
      }
      if (initObj.hasOwnProperty('foot')) {
        this.foot = initObj.foot
      }
      else {
        this.foot = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Leg
    // Serialize message field [tigh]
    bufferOffset = _serializer.float32(obj.tigh, buffer, bufferOffset);
    // Serialize message field [knee]
    bufferOffset = _serializer.float32(obj.knee, buffer, bufferOffset);
    // Serialize message field [foot]
    bufferOffset = _serializer.float32(obj.foot, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Leg
    let len;
    let data = new Leg(null);
    // Deserialize message field [tigh]
    data.tigh = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [knee]
    data.knee = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [foot]
    data.foot = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'project_demo/Leg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5da4b1c2eb62b548b44603075da2f338';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    #tigh
    float32 tigh
    #knee
    float32 knee
    #foot
    float32 foot
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Leg(null);
    if (msg.tigh !== undefined) {
      resolved.tigh = msg.tigh;
    }
    else {
      resolved.tigh = 0.0
    }

    if (msg.knee !== undefined) {
      resolved.knee = msg.knee;
    }
    else {
      resolved.knee = 0.0
    }

    if (msg.foot !== undefined) {
      resolved.foot = msg.foot;
    }
    else {
      resolved.foot = 0.0
    }

    return resolved;
    }
};

module.exports = Leg;

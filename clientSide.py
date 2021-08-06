const device = new Twilio.Device();
device.setup(token, options);

// or (deprecated singleton behavior)...

Twilio.Device.setup(token, options);
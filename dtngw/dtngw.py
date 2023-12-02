import time

import paho.mqtt.client as mqtt

import influxdb_client


bucket = "cse696"
org = "cse696"
token = "t01PaLAFZRMdUnJjsf-bY1ugx7jOEPltDRO4CQaxVLVVsC2DWplQ228AjiG5fVvPgswW9JmYb-up8mZhJYdgOw=="
# Store the URL of your InfluxDB instance
url = "http://home:8086/"

db_client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org,
    debug=True
)

write_api = db_client.write_api()


# The callback for when the client receives a CONNACK response from the server.
def on_connect(mqtt_client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    mqtt_client.subscribe("temperature")
    mqtt_client.subscribe("pressure")
    mqtt_client.subscribe("heartRate")
    mqtt_client.subscribe("spO2")


# The callback for when a PUBLISH message is received from the server.
def on_message(mqtt_client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    p = influxdb_client.Point("dtngw").tag("topic", msg.topic).field("value", float(msg.payload)).time(time.time_ns())
    write_api.write(bucket=bucket, org=org, record=p)


mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.username_pw_set("admin", "password")

mqtt_client.connect("home", 1883, 60)
mqtt_client.loop_forever()

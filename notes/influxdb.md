# InfluxDB

Making the InfluxDB have a data retention policy and a way to average the data

<https://docs.influxdata.com/influxdb/v1.7/guides/downsampling_and_retention/>

`CREATE RETENTION POLICY "two_years" ON "sensor_data" DURATION 104w REPLICATION 1`

This is for "dev01" written nicely:

CREATE CONTINUOUS QUERY "cq_60m" ON "sensor_data" BEGIN
  SELECT mean("altitude_mm") as "mean_altitude_mm", mean("gas_resistance_Ohm") as "mean_gas_resistance_Ohm", mean("pressure_Pa") as "mean_pressure_Pa", mean("rel_humidity_100x_perc") as "mean_rel_humidity_100x_perc", mean("temperature_100x_C") as "mean_temperature_100x_C"
  INTO "two_years"."downsampled_orders"
  FROM "dev01"
  GROUP BY time(60m)
END


As a one liner:

CREATE CONTINUOUS QUERY "cq_60m" ON "sensor_data" BEGIN SELECT mean("altitude_mm") as "mean_altitude_mm", mean("gas_resistance_Ohm") as "mean_gas_resistance_Ohm", mean("pressure_Pa") as "mean_pressure_Pa", mean("rel_humidity_100x_perc") as "mean_rel_humidity_100x_perc", mean("temperature_100x_C") as "mean_temperature_100x_C" INTO "two_years"."downsampled_orders" FROM "dev01" GROUP BY time(60m) END

CREATE CONTINUOUS QUERY "cq_60m" ON "sensor_data" BEGIN SELECT mean("altitude_mm") as "mean_altitude_mm", mean("gas_resistance_Ohm") as "mean_gas_resistance_Ohm", mean("pressure_Pa") as "mean_pressure_Pa", mean("rel_humidity_100x_perc") as "mean_rel_humidity_100x_perc", mean("temperature_100x_C") as "mean_temperature_100x_C" INTO "two_years"."downsampled_orders" FROM "dev02" GROUP BY time(60m) END

Doesn't like running 2. Need to have them together? Or just have them seperate with a better name.

CREATE RETENTION POLICY "dev01_2years" ON "sensor_data" DURATION 104w REPLICATION 1
CREATE RETENTION POLICY "dev02_2years" ON "sensor_data" DURATION 104w REPLICATION 1

CREATE CONTINUOUS QUERY "cq_60m_dev01" ON "sensor_data" BEGIN SELECT mean("altitude_mm") as "mean_altitude_mm", mean("gas_resistance_Ohm") as "mean_gas_resistance_Ohm", mean("pressure_Pa") as "mean_pressure_Pa", mean("rel_humidity_100x_perc") as "mean_rel_humidity_100x_perc", mean("temperature_100x_C") as "mean_temperature_100x_C" INTO "dev01_2years"."downsampled_orders" FROM "dev01" GROUP BY time(60m) END
CREATE CONTINUOUS QUERY "cq_60m_dev02" ON "sensor_data" BEGIN SELECT mean("altitude_mm") as "mean_altitude_mm", mean("gas_resistance_Ohm") as "mean_gas_resistance_Ohm", mean("pressure_Pa") as "mean_pressure_Pa", mean("rel_humidity_100x_perc") as "mean_rel_humidity_100x_perc", mean("temperature_100x_C") as "mean_temperature_100x_C" INTO "dev02_2years"."downsampled_orders" FROM "dev02" GROUP BY time(60m) END

## dropping it
show continuous query
drop continuous query cq_60m on sensor_data

## run on old data
<https://community.influxdata.com/t/backfilling-a-continuous-query/1960>
Which is basically running a normal query and placing the data in the database

CREATE CONTINUOUS QUERY "1h_event_count"
ON "db_name"
BEGIN
SELECT sum(“count”) as "count"
INTO “2_years”."events"
FROM “6_months”."events"
GROUP BY time(1h)
END;

Backfill the measurement using:

SELECT sum(“count”) as "count"
INTO “2_years”."events"
FROM “6_months”."events"
where time > and time < "End Time"
GROUP BY time(1h)


SELECT mean("altitude_mm") as "mean_altitude_mm", mean("gas_resistance_Ohm") as "mean_gas_resistance_Ohm", mean("pressure_Pa") as "mean_pressure_Pa", mean("rel_humidity_100x_perc") as "mean_rel_humidity_100x_perc", mean("temperature_100x_C") as "mean_temperature_100x_C" INTO "dev01_2years"."downsampled_orders" FROM "dev01" GROUP BY time(60m);
SELECT mean("altitude_mm") as "mean_altitude_mm", mean("gas_resistance_Ohm") as "mean_gas_resistance_Ohm", mean("pressure_Pa") as "mean_pressure_Pa", mean("rel_humidity_100x_perc") as "mean_rel_humidity_100x_perc", mean("temperature_100x_C") as "mean_temperature_100x_C" INTO "dev02_2years"."downsampled_orders" FROM "dev02" GROUP BY time(60m);

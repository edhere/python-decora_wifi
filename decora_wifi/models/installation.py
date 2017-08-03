# Leviton Cloud Services API model Installation.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from decora_wifi.base_model import BaseModel


class Installation(BaseModel):
    def __init__(self, session, model_id=None):
        super(Installation, self).__init__(session, model_id)

    def count(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def count_action_blocks(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/actionBlocks/count"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def count_actions(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/actions/count"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def count_activities(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/activities/count"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def count_activity_triggers(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/activityTriggers/count"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def count_area_snapshots(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/areaSnapshots/count"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def count_areas(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/areas/count"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def count_controllers(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/controllers/count"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def count_feed_items(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/feedItems/count"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def count_load_snapshots(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/loadSnapshots/count"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def count_loads(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/loads/count"
        return session.call_api(api, attribs, 'get')

    def count_location_installations(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/installations/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def count_schedules(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/schedules/count"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def count_sensor_snapshots(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/sensorSnapshots/count"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def count_sensors(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/sensors/count"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def count_shades(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/shades/count"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def count_thermostat_snapshots(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/thermostatSnapshots/count"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def count_thermostats(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/thermostats/count"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def count_touchscreens(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/touchscreens/count"
        return session.call_api(api, attribs, 'get')

    def create(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def create_action_blocks(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/actionBlocks"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create_actions(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/actions"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create_activities(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/activities"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create_activity_triggers(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/activityTriggers"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create_area_snapshots(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/areaSnapshots"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create_areas(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/areas"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create_controllers(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/controllers"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create_load_snapshots(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/loadSnapshots"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create_loads(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/loads"
        return session.call_api(api, attribs, 'post')

    def create_location_installations(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/installations".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many_location_installations(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/installations".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def create_schedules(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/schedules"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create_sensor_snapshots(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/sensorSnapshots"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create_sensors(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/sensors"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create_shades(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/shades"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create_thermostat_snapshots(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/thermostatSnapshots"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create_thermostats(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/thermostats"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def create_touchscreens(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/touchscreens"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def delete_action_blocks(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/actionBlocks"
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def delete_actions(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/actions"
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def delete_activities(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/activities"
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def delete_activity_triggers(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/activityTriggers"
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def delete_area_snapshots(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/areaSnapshots"
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def delete_areas(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/areas"
        return session.call_api(api, attribs, 'delete')

    def delete_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    @classmethod
    def delete_controllers(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/controllers"
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def delete_load_snapshots(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/loadSnapshots"
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def delete_loads(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/loads"
        return session.call_api(api, attribs, 'delete')

    def delete_location_installations(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/installations".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    @classmethod
    def delete_schedules(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/schedules"
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def delete_sensor_snapshots(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/sensorSnapshots"
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def delete_sensors(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/sensors"
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def delete_shades(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/shades"
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def delete_thermostat_snapshots(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/thermostatSnapshots"
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def delete_thermostats(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/thermostats"
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def delete_touchscreens(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/touchscreens"
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_action_blocks(cls, session, action_block, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/actionBlocks/{0}".format(action_block)
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_actions(cls, session, action, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/actions/{0}".format(action)
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_activities(cls, session, activity, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/activities/{0}".format(activity)
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_activity_triggers(cls, session, activity_trigger, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/activityTriggers/{0}".format(activity_trigger)
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_area_snapshots(cls, session, area_snapshot, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/areaSnapshots/{0}".format(area_snapshot)
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_areas(cls, session, area, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/areas/{0}".format(area)
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_controllers(cls, session, controller, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/controllers/{0}".format(controller)
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_load_snapshots(cls, session, load_snapshot, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/loadSnapshots/{0}".format(load_snapshot)
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_loads(cls, session, load, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/loads/{0}".format(load)
        return session.call_api(api, attribs, 'delete')

    def destroy_by_id_location_installations(self, installation, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/installations/{1}".format(self._id, installation)
        return self._session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_schedules(cls, session, schedule, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/schedules/{0}".format(schedule)
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_sensor_snapshots(cls, session, sensor_snapshot, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/sensorSnapshots/{0}".format(sensor_snapshot)
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_sensors(cls, session, sensor, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/sensors/{0}".format(sensor)
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_shades(cls, session, shade, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/shades/{0}".format(shade)
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_thermostat_snapshots(cls, session, thermostat_snapshot, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/thermostatSnapshots/{0}".format(thermostat_snapshot)
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_thermostats(cls, session, thermostat, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/thermostats/{0}".format(thermostat)
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_touchscreens(cls, session, touchscreen, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/touchscreens/{0}".format(touchscreen)
        return session.call_api(api, attribs, 'delete')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_action_blocks(cls, session, action_block, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/actionBlocks/{0}".format(action_block)
        return session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_actions(cls, session, action, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/actions/{0}".format(action)
        return session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_activities(cls, session, activity, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/activities/{0}".format(activity)
        return session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_activity_triggers(cls, session, activity_trigger, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/activityTriggers/{0}".format(activity_trigger)
        return session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_area_snapshots(cls, session, area_snapshot, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/areaSnapshots/{0}".format(area_snapshot)
        return session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_areas(cls, session, area, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/areas/{0}".format(area)
        return session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_controllers(cls, session, controller, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/controllers/{0}".format(controller)
        return session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_feed_items(cls, session, feed_item, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/feedItems/{0}".format(feed_item)
        return session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_load_snapshots(cls, session, load_snapshot, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/loadSnapshots/{0}".format(load_snapshot)
        return session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_loads(cls, session, load, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/loads/{0}".format(load)
        return session.call_api(api, attribs, 'get')

    def find_by_id_location_installations(self, installation, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/installations/{1}".format(self._id, installation)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_schedules(cls, session, schedule, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/schedules/{0}".format(schedule)
        return session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_sensor_snapshots(cls, session, sensor_snapshot, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/sensorSnapshots/{0}".format(sensor_snapshot)
        return session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_sensors(cls, session, sensor, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/sensors/{0}".format(sensor)
        return session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_shades(cls, session, shade, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/shades/{0}".format(shade)
        return session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_thermostat_snapshots(cls, session, thermostat_snapshot, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/thermostatSnapshots/{0}".format(thermostat_snapshot)
        return session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_thermostats(cls, session, thermostat, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/thermostats/{0}".format(thermostat)
        return session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_touchscreens(cls, session, touchscreen, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/touchscreens/{0}".format(touchscreen)
        return session.call_api(api, attribs, 'get')

    def find_one(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/findOne".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.set_model_data(data)
        return self

        return self._session.call_api(api, attribs, 'get')

    def get_action_block_installation(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActionBlocks/{0}/installation".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_action_blocks(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/actionBlocks"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def get_actions(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/actions"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def get_activities(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/activities"
        return session.call_api(api, attribs, 'get')

    def get_activity_installation(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Activities/{0}/installation".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_activity_triggers(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/activityTriggers"
        return session.call_api(api, attribs, 'get')

    def get_area_installation(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/installation".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get_area_snapshot_installation(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/AreaSnapshots/{0}/installation".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_area_snapshots(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/areaSnapshots"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def get_areas(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/areas"
        return session.call_api(api, attribs, 'get')

    def get_controller_installation(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/{0}/installation".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_controllers(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/controllers"
        return session.call_api(api, attribs, 'get')

    def get_feed_item_installation(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/FeedItems/{0}/installation".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_feed_items(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/feedItems"
        return session.call_api(api, attribs, 'get')

    def get_load_installation(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Loads/{0}/installation".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get_load_snapshot_installation(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/LoadSnapshots/{0}/installation".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_load_snapshots(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/loadSnapshots"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def get_loads(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/loads"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def get_location(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/location"
        return session.call_api(api, attribs, 'get')

    def get_location_installations(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/installations".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_schedules(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/schedules"
        return session.call_api(api, attribs, 'get')

    def get_sensor_installation(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Sensors/{0}/installation".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get_sensor_snapshot_installation(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/SensorSnapshots/{0}/installation".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_sensor_snapshots(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/sensorSnapshots"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def get_sensors(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/sensors"
        return session.call_api(api, attribs, 'get')

    def get_shade_installation(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Shades/{0}/installation".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_shades(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/shades"
        return session.call_api(api, attribs, 'get')

    def get_thermostat_installation(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/{0}/installation".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get_thermostat_snapshot_installation(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ThermostatSnapshots/{0}/installation".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_thermostat_snapshots(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/thermostatSnapshots"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def get_thermostats(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/thermostats"
        return session.call_api(api, attribs, 'get')

    def get_touchscreen_installation(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Touchscreens/{0}/installation".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_touchscreens(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/touchscreens"
        return session.call_api(api, attribs, 'get')

    def register_controller(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/registerController".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def replace_or_create(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/replaceOrCreate".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def update_attributes(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id"
        return session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_action_blocks(cls, session, action_block, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/actionBlocks/{0}".format(action_block)
        return session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_actions(cls, session, action, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/actions/{0}".format(action)
        return session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_activities(cls, session, activity, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/activities/{0}".format(activity)
        return session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_activity_triggers(cls, session, activity_trigger, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/activityTriggers/{0}".format(activity_trigger)
        return session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_area_snapshots(cls, session, area_snapshot, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/areaSnapshots/{0}".format(area_snapshot)
        return session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_areas(cls, session, area, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/areas/{0}".format(area)
        return session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_controllers(cls, session, controller, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/controllers/{0}".format(controller)
        return session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_load_snapshots(cls, session, load_snapshot, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/loadSnapshots/{0}".format(load_snapshot)
        return session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_loads(cls, session, load, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/loads/{0}".format(load)
        return session.call_api(api, attribs, 'put')

    def update_by_id_location_installations(self, installation, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Locations/{0}/installations/{1}".format(self._id, installation)
        return self._session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_schedules(cls, session, schedule, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/schedules/{0}".format(schedule)
        return session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_sensor_snapshots(cls, session, sensor_snapshot, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/sensorSnapshots/{0}".format(sensor_snapshot)
        return session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_sensors(cls, session, sensor, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/sensors/{0}".format(sensor)
        return session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_shades(cls, session, shade, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/shades/{0}".format(shade)
        return session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_thermostat_snapshots(cls, session, thermostat_snapshot, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/thermostatSnapshots/{0}".format(thermostat_snapshot)
        return session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_thermostats(cls, session, thermostat, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/thermostats/{0}".format(thermostat)
        return session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_touchscreens(cls, session, touchscreen, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/:id/touchscreens/{0}".format(touchscreen)
        return session.call_api(api, attribs, 'put')

    def upsert(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations".format(self._id)
        return self._session.call_api(api, attribs, 'put')

    def upsert_with_where(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/upsertWithWhere".format(self._id)
        return self._session.call_api(api, attribs, 'post')


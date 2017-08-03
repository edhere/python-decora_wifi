# Leviton Cloud Services API model Thermostat.
# Auto-generated by api_scraper.py.
#
# Copyright 2017 Tim Lyakhovetskiy <tlyakhov@gmail.com>
#
# This code is released under the terms of the MIT license. See the LICENSE
# file for more details.
from decora_wifi.base_model import BaseModel


class Thermostat(BaseModel):
    def __init__(self, session, model_id=None):
        super(Thermostat, self).__init__(session, model_id)

    def count(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def count_activity_triggers(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id/activityTriggers/count"
        return session.call_api(api, attribs, 'get')

    def count_area_thermostats(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostats/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def count_controller_thermostats(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/{0}/thermostats/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def count_feed_items(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id/feedItems/count"
        return session.call_api(api, attribs, 'get')

    def count_installation_thermostats(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/thermostats/count".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def count_thermostat_snapshots(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id/thermostatSnapshots/count"
        return session.call_api(api, attribs, 'get')

    def create(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def create_activity_triggers(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id/activityTriggers"
        return session.call_api(api, attribs, 'post')

    def create_area_thermostats(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostats".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_controller_thermostats(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/{0}/thermostats".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_installation_thermostats(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/thermostats".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many_area_thermostats(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostats".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many_controller_thermostats(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/{0}/thermostats".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def create_many_installation_thermostats(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/thermostats".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def create_thermostat_snapshots(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id/thermostatSnapshots"
        return session.call_api(api, attribs, 'post')

    @classmethod
    def delete_activity_triggers(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id/activityTriggers"
        return session.call_api(api, attribs, 'delete')

    def delete_area_thermostats(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostats".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_controller_thermostats(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/{0}/thermostats".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    def delete_installation_thermostats(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/thermostats".format(self._id)
        return self._session.call_api(api, attribs, 'delete')

    @classmethod
    def delete_thermostat_snapshots(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id/thermostatSnapshots"
        return session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_activity_triggers(cls, session, activity_trigger, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id/activityTriggers/{0}".format(activity_trigger)
        return session.call_api(api, attribs, 'delete')

    def destroy_by_id_area_thermostats(self, thermostat, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostats/{1}".format(self._id, thermostat)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_controller_thermostats(self, thermostat, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/{0}/thermostats/{1}".format(self._id, thermostat)
        return self._session.call_api(api, attribs, 'delete')

    def destroy_by_id_installation_thermostats(self, thermostat, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/thermostats/{1}".format(self._id, thermostat)
        return self._session.call_api(api, attribs, 'delete')

    @classmethod
    def destroy_by_id_thermostat_snapshots(cls, session, thermostat_snapshot, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id/thermostatSnapshots/{0}".format(thermostat_snapshot)
        return session.call_api(api, attribs, 'delete')

    def exists(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/{0}/exists".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/{0}".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_activity_triggers(cls, session, activity_trigger, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id/activityTriggers/{0}".format(activity_trigger)
        return session.call_api(api, attribs, 'get')

    def find_by_id_area_thermostats(self, thermostat, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostats/{1}".format(self._id, thermostat)
        return self._session.call_api(api, attribs, 'get')

    def find_by_id_controller_thermostats(self, thermostat, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/{0}/thermostats/{1}".format(self._id, thermostat)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_feed_items(cls, session, feed_item, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id/feedItems/{0}".format(feed_item)
        return session.call_api(api, attribs, 'get')

    def find_by_id_installation_thermostats(self, thermostat, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/thermostats/{1}".format(self._id, thermostat)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def find_by_id_thermostat_snapshots(cls, session, thermostat_snapshot, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id/thermostatSnapshots/{0}".format(thermostat_snapshot)
        return session.call_api(api, attribs, 'get')

    def find_one(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/findOne".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/{0}".format(self._id)
        data = self._session.call_api(api, attribs, 'get')

        self.set_model_data(data)
        return self

        return self._session.call_api(api, attribs, 'get')

    def get_activity_trigger_thermostat(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ActivityTriggers/{0}/thermostat".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_activity_triggers(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id/activityTriggers"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def get_area(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id/area"
        return session.call_api(api, attribs, 'get')

    def get_area_thermostats(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostats".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get_controller_thermostats(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/{0}/thermostats".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_device_definition(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id/deviceDefinition"
        return session.call_api(api, attribs, 'get')

    def get_feed_item_thermostat(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/FeedItems/{0}/thermostat".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_feed_items(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id/feedItems"
        return session.call_api(api, attribs, 'get')

    @classmethod
    def get_installation(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id/installation"
        return session.call_api(api, attribs, 'get')

    def get_installation_thermostats(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/thermostats".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    def get_thermostat_snapshot_device_definition(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/ThermostatSnapshots/{0}/deviceDefinition".format(self._id)
        return self._session.call_api(api, attribs, 'get')

    @classmethod
    def get_thermostat_snapshots(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id/thermostatSnapshots"
        return session.call_api(api, attribs, 'get')

    def replace_by_id(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/{0}/replace".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    def replace_or_create(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/replaceOrCreate".format(self._id)
        return self._session.call_api(api, attribs, 'post')

    @classmethod
    def update_attributes(cls, session, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id"
        return session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_activity_triggers(cls, session, activity_trigger, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id/activityTriggers/{0}".format(activity_trigger)
        return session.call_api(api, attribs, 'put')

    def update_by_id_area_thermostats(self, thermostat, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Areas/{0}/thermostats/{1}".format(self._id, thermostat)
        return self._session.call_api(api, attribs, 'put')

    def update_by_id_controller_thermostats(self, thermostat, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Controllers/{0}/thermostats/{1}".format(self._id, thermostat)
        return self._session.call_api(api, attribs, 'put')

    def update_by_id_installation_thermostats(self, thermostat, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Installations/{0}/thermostats/{1}".format(self._id, thermostat)
        return self._session.call_api(api, attribs, 'put')

    @classmethod
    def update_by_id_thermostat_snapshots(cls, session, thermostat_snapshot, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/:id/thermostatSnapshots/{0}".format(thermostat_snapshot)
        return session.call_api(api, attribs, 'put')

    def upsert(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats".format(self._id)
        return self._session.call_api(api, attribs, 'put')

    def upsert_with_where(self, attribs=None):
        if attribs is None:
            attribs = {}
        api = "/Thermostats/upsertWithWhere".format(self._id)
        return self._session.call_api(api, attribs, 'post')

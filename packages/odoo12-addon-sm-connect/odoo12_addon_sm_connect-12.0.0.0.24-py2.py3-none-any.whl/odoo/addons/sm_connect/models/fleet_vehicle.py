from odoo import models, fields, api
from odoo.tools.translate import _
from odoo.exceptions import UserError
from odoo.addons.sm_connect.models.models_sm_fleetio_api_utils import sm_fleetio_api_utils
import logging
import time

_logger = logging.getLogger(__name__)


class FleetVehicle(models.Model):
    _name = 'fleet.vehicle'
    _inherit = 'fleet.vehicle'

    maintenance = fields.Boolean(
        string=_("Maintenance"),
        help=_("This car will be synchronized to other Services")
    ) # This field has to be deleted in the next sprint
    maintenance_external_app = fields.Boolean(
        string="Maintenance in External App",
        help=_("This car will be synchronized to other Services"),
        readonly=False,
        related="maintenance",
        store=True
    )
    fleetio_id = fields.Char(string="Fleetio ID")
    fleetio_archived = fields.Boolean(string="Archived in Fleetio")
    
    @api.model
    def create(self, vals):
        vehicle = super(FleetVehicle, self).create(vals)

        if vehicle.maintenance_external_app:
            sm_fleetio_api_utils.drop_instance()
            fleetio_api_utils = sm_fleetio_api_utils.get_instance(self)
            if fleetio_api_utils.check_api_settings():
                if vehicle.vin_sn and vehicle.license_plate:
                    if vehicle.fleetio_id:
                        fleetio_api_utils.update_vehicle(vehicle)
                    else:
                        fleetio_api_utils.create_vehicle(vehicle)
                else:
                    raise UserError("You have to set at least the license plate or the Vehicle Identification Number")
            else:
                raise UserError("No proper Fleetio API credentials found. If you have entered them correctly, make sure you save the configuration.")

        return vehicle

    def write(self, vals):
        res = super(FleetVehicle, self).write(vals)

        if not (len(set(vals.keys())) == 1 and set(vals.keys()).pop()=="fleetio_id"):
            for vehicle in self:
                sm_fleetio_api_utils.drop_instance()
                fleetio_api_utils = sm_fleetio_api_utils.get_instance(self)
                if vehicle.maintenance_external_app:
                    if fleetio_api_utils.check_api_settings():
                        if vehicle.fleetio_archived and vehicle.fleetio_id:
                            # Vehicle that was archived and now needs to be restored
                            fleetio_api_utils.restore_vehicle(vehicle)
                            fleetio_api_utils.update_vehicle(vehicle)

                        else:
                            # Actual Upload
                            if vehicle.vin_sn and vehicle.license_plate:
                                if vehicle.fleetio_id:
                                    fleetio_api_utils.update_vehicle(vehicle)
                                else:
                                    fleetio_api_utils.create_vehicle(vehicle)
                            else:
                                raise UserError("You have to set at least the license plate or the Vehicle Identification Number")
                    else:
                        raise UserError("No proper Fleetio API credentials found. If you have entered them correctly, make sure you save the configuration.")
                elif vehicle.fleetio_id:
                    # Then we need to archive on Fleetio
                    if not vehicle.fleetio_archived:
                        fleetio_api_utils.archive_vehicle(vehicle)

        return res
    
    @api.model
    def get_fleetio_instance(self):
        sm_fleetio_api_utils.drop_instance()
        return sm_fleetio_api_utils.get_instance(self)
    
    @api.model
    def retrieve_fleetio_vehicle_list(self):
        fleetio_instance = self.get_fleetio_instance()
        return fleetio_instance.search_vehicles()
    
    @api.multi
    def update_fields_from_fleetio(self, field_mapping):
        """
        A method that retrieves the list of vehicles and tries to update
        Odoo's vehicles according the field_mapping argument

        field_mapping = [
            ("odoo_field", "fleetio_field"),
            ("odoo_field_2", "fleetio_field_2"),
            ("odoo_field_3", "fleetio_field_3"),
        ]
        """
        if not field_mapping:
            _logger.error("Wrong field_mapping argument for the function: " + str(field_mapping) + "read the documentation of the method.")
            raise UserError("Wrong field_mapping argument for the function: " + str(field_mapping) + "read the documentation of the method.")
        vehicles_json = self.retrieve_fleetio_vehicle_list()
        if not vehicles_json:
            return False
        for vehicle in self:
            if vehicle.license_plate and vehicle.fleetio_id:
                record = vehicles_json.get(vehicle.license_plate)
                if record:

                    # now for each mapping we combine the changes and then write them

                    change_vals = {}
                    for odoo_field, fleetio_field in field_mapping:
                        gathered_field = record.get(fleetio_field)
                        if gathered_field is not None:
                            change_vals.update({odoo_field: gathered_field})
                        else:
                            _logger.warning(f'No {fleetio_field} found for: ' + vehicle.license_plate)
                    if change_vals:
                        vehicle.write(change_vals)
                        time.sleep(6)

                else:
                    _logger.warning("The vehicle with license_plate: " + vehicle.license_plate + " wasn't found on fleetio")
            else:
                _logger.error("The vehicle with id: " + vehicle.id + " is not properly setup on Odoo")

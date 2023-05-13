from your_project.models import Device
from your_project import db

class DeviceManager:
    def add_device(self, tenant_id, ip, community, version, poll_interval, oids):
        device = Device(tenant_id=tenant_id, ip=ip, community=community, version=version, poll_interval=poll_interval, oids=oids)
        db.session.add(device)
        db.session.commit()

    # Other DeviceManager methods

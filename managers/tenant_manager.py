from models import Tenant
from extensions import db

class TenantManager:
    def __init__(self):
        pass

    def create_tenant(self, name):
        tenant = Tenant(name=name)
        db.session.add(tenant)
        db.session.commit()
        return tenant

    def get_tenant(self, tenant_id):
        return Tenant.query.get(tenant_id)

    def add_device(self, tenant_id, ip, community, version, poll_interval, oids):
        device = Device(tenant_id=tenant_id, ip=ip, community=community, version=version, poll_interval=poll_interval, oids=oids)
        db.session.add(device)
        db.session.commit()
        return device

    def update_device(self, device_id, ip=None, community=None, version=None, poll_interval=None, oids=None):
        device = Device.query.get(device_id)
        if ip:
            device.ip = ip
        if community:
            device.community = community
        if version:
            device.version = version
        if poll_interval:
            device.poll_interval = poll_interval
        if oids:
            device.oids = oids
        db.session.commit()

    def remove_device(self, device_id):
        device = Device.query.get(device_id)
        db.session.delete(device)
        db.session.commit()

    def add_user(self, tenant_id, username, password):
        user = User(tenant_id=tenant_id, username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return user

    def update_user(self, user_id, username=None, password=None):
        user = User.query.get(user_id)
        if username:
            user.username = username
        if password:
            user.password = password
        db.session.commit()

    def remove_user(self, user_id):
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()

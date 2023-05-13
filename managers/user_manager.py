class UserManager:
    def __init__(self, app, db):
        self.login_manager = LoginManager(app)
        self.login_manager.login_view = 'login'
        self.login_manager.login_message = 'Please log in to access this page.'
        self.login_manager.login_message_category = 'info'

        user_manager = FlaskUserManager(app, db, User)
        app.user_manager = user_manager

        @self.login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

    def create_user(self, username, password, tenant_id):
        user = User(username=username, password=user_manager.hash_password(password), tenant_id=tenant_id)
        db.session.add(user)
        db.session.commit()
        return user

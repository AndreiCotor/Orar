from OrarCovid19 import db

class postare(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    subject=db.Column(db.String(100),nullable=False)
    date=db.Column(db.DateTime,nullable=False)

    def __repr__(self):
        return f"Curs('{self.subject}','{self.date}')"

from main import db
from sqlalchemy import func
from sqlalchemy.orm import validates


class Computer(db.Model):
    __tablename__ = 'computers'
    id = db.Column(db.Integer, primary_key=True)
    budget = db.Column(db.String(1000))
    price = db.Column(db.String(1000))
    model = db.Column(db.String(1000))
    cpu = db.Column(db.String(1000))
    graphics = db.Column(db.String(1000))
    ram = db.Column(db.String(1000))
    drive = db.Column(db.String(1000))
    display = db.Column(db.String(1000))
    battery = db.Column(db.String(1000))
    quality = db.Column(db.String(1000))
    weight = db.Column(db.String(1000))
    thickness = db.Column(db.String(1000))
    price_normalized = db.Column(db.String(1000))
    operating_system = db.Column(db.String(1000))
    battery_normalized = db.Column(db.String(1000))
    harddrive_normalized = db.Column(db.String(1000))
    memory_normalized = db.Column(db.String(1000))
    size_normalized = db.Column(db.String(1000))



    def __repr__(self):
        return '#%d: Budget: %s, Price: %s, Model: %s, CPU: %s, Graphics: %s, RAM: %s, Drive: %s, Display: %s, Battery: %s, Quality: %s, Weight: %s, Thickness: %s, Price Normalized: %s, Operating System: %s, Battery Normalized: %s, Hard Drive Normalized: %s, Memory Normalized: %s, Size Normalized: %s' % (self.id, self.budget, self.price, self.model, self.cpu, self.graphics, self.ram, self.drive, self.display, self.battery, self.quality, self.weight, self.thickness, self.price_normalized, self.operating_system, self.battery_normalized, self.harddrive_normalized, self.memory_normalized, self.size_normalized)


class Weights(db.Model):
    __tablename__ = 'weights'
    id = db.Column(db.Integer, primary_key=True)
    operating_system = db.Column(db.Float(10))
    battery = db.Column(db.Float(10))
    harddrive = db.Column(db.Float(10))
    budget = db.Column(db.Float(10))
    memory = db.Column(db.Float(10))
    size = db.Column(db.Float(10))